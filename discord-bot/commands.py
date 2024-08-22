import discord
from typing import Optional, Tuple, Union
from utility import user_has_confirmed


class Message:
    def __init__(self, bot: discord.Client, interaction: discord.Interaction):
        self.bot = bot
        self.interaction = interaction
        self.is_author_same_as_user = (
            lambda message: message.author == interaction.user
            and message.channel == interaction.channel
        )

    # Used for send()
    async def _get_target_channel(
        self, target: Optional[str]
    ) -> Union[discord.abc.GuildChannel, discord.Thread, discord.abc.PrivateChannel]:
        if target is None:
            await self.interaction.followup.send(
                "Target channel ID not found. Message will be sent here instead.",
                ephemeral=True,
            )
            target = self.interaction.channel.id
        try:
            target_channel = self.bot.get_channel(int(target))
        except ValueError:
            await self.interaction.followup.send("Invalid channel ID.", ephemeral=True)
            return None
        if target_channel is None:
            await self.interaction.followup.send("Channel not found.", ephemeral=True)
            return None
        return target_channel

    # Used for edit() and delete()
    async def _validate_target_xor_source(
        self, target: Optional[str], source: Optional[str]
    ) -> Optional[discord.Message]:
        if target is None and source is None:
            await self.interaction.followup.send(
                "Target/Source message ID not found.", ephemeral=True
            )
            return None
        if target and source:
            await self.interaction.followup.send(
                "Target and Source should not both be defined! Use only one!",
                ephemeral=True,
            )
            return None
        try:
            target_message = await self.interaction.channel.fetch_message(
                int(target or source)
            )
        except (ValueError, discord.NotFound):
            await self.interaction.followup.send("Invalid message ID.", ephemeral=True)
            return None
        if target_message is None:
            await self.interaction.followup.send("Message not found.", ephemeral=True)
            return None
        return target_message

    # Used for edit(), delete() and move()
    async def _ensure_message_is_bot_owned(self, message: discord.Message):
        if message.author != self.bot.user:
            await self.interaction.followup.send(
                "You can only edit/delete messages created by me.", ephemeral=True
            )
            return False
        return True

    # Used for copy() and move()
    async def _validate_target_and_source(
        self, target: Optional[str], source: Optional[str]
    ) -> Optional[Tuple[discord.Message, discord.abc.GuildChannel]]:
        if source is None:
            await self.interaction.followup.send(
                "Source message ID missing.", ephemeral=True
            )
            return None
        if target is None:
            await self.interaction.followup.send(
                "Target channel ID not found. Message will be sent here instead.",
                ephemeral=True,
            )
            target = self.interaction.channel.id
        try:
            source_message = await self.interaction.channel.fetch_message(int(source))
            target_channel = self.bot.get_channel(int(target))
        except (ValueError, discord.NotFound):
            await self.interaction.followup.send(
                "Invalid message ID or channel ID.", ephemeral=True
            )
            return None
        if source_message is None:
            await self.interaction.followup.send("Message not found.", ephemeral=True)
            return None
        if target_channel is None:
            await self.interaction.followup.send("Channel not found.", ephemeral=True)
            return None
        return source_message, target_channel

    async def send(self, target: Optional[str] = None, source: Optional[str] = None):
        if source:
            await self.interaction.followup.send(
                "Source message ID not required for sending a message.", ephemeral=True
            )
            return
        target_channel = await self._get_target_channel(target)
        if target_channel is None:
            return
        await self.interaction.followup.send(
            "Please enter the content for the message:", ephemeral=True
        )
        new_message = await self.bot.wait_for(
            "message", check=self.is_author_same_as_user
        )
        await target_channel.send(new_message.content)
        await self.interaction.followup.send(
            f"Message sent to {target_channel.mention}", ephemeral=True
        )
        await new_message.delete()

    async def edit(self, target: Optional[str] = None, source: Optional[str] = None):
        target_message = await self._validate_target_xor_source(target, source)
        if target_message is None:
            return
        if not await self._ensure_message_is_bot_owned(target_message):
            return
        await self.interaction.followup.send(
            f"Editing {target_message.jump_url}...\nYou can right click a message and select 'Copy Text' to quickly edit",
            ephemeral=True,
        )
        await self.interaction.followup.send(
            "Please enter the new content for the message:", ephemeral=True
        )
        new_message = await self.bot.wait_for(
            "message", check=self.is_author_same_as_user
        )
        await target_message.edit(content=new_message.content)
        await self.interaction.followup.send(
            f"Message edited: {target_message.jump_url}", ephemeral=True
        )
        await new_message.delete()

    async def delete(self, target: Optional[str] = None, source: Optional[str] = None):
        target_message = await self._validate_target_xor_source(target, source)
        if target_message is None:
            return
        if not await self._ensure_message_is_bot_owned(target_message):
            return
        if not await user_has_confirmed(
            self.interaction, "Are you sure you want to delete this message?"
        ):
            return
        await target_message.delete()
        await self.interaction.followup.send(
            f"Message deleted: {target_message.jump_url}", ephemeral=True
        )

    async def copy(self, target: Optional[str] = None, source: Optional[str] = None):
        result = await self._validate_target_and_source(target, source)
        if result is None:
            return
        source_message, target_channel = result
        await target_channel.send(source_message.content)
        await self.interaction.followup.send(
            f"Message copied to {target_channel.mention}", ephemeral=True
        )

    async def move(self, target: Optional[str] = None, source: Optional[str] = None):
        result = await self._validate_target_and_source(target, source)
        if result is None:
            return
        source_message, target_channel = result
        if not await self._ensure_message_is_bot_owned(source_message):
            return
        if not await user_has_confirmed(
            self.interaction,
            self.bot,
            content=f"Are you sure you want to move {source_message.jump_url} to {target_channel.mention}?\nThe original message will be deleted!",
        ):
            return
        await target_channel.send(source_message.content)
        await source_message.delete()
        await self.interaction.followup.send(
            f"Message moved to {target_channel.mention}", ephemeral=True
        )
