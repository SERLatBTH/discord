import time
from typing import Literal, Optional

import commands as Command
from utility import get_env_variable, user_has_access, user_has_confirmed

import discord
from discord import app_commands


# Code inpired from: https://github.com/therealOri/TheAdministrator/blob/c2e74191eef7cf20960e23cb27e5b6004145045c/admin.py#L122
# +++++++++++ Client Setup +++++++++++ #
class Bot(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        guild_id = get_env_variable("GUILD_ID", required=True)

        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(id=guild_id)

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=self.guild)
        await self.tree.sync(guild=self.guild)

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")
        await self.setup_hook()


intents = discord.Intents.default()
intents.message_content = True
bot = Bot(intents=intents)
# +++++++++++ Client Setup +++++++++++ #

ADMIN_ROLE_ID = get_env_variable("ADMIN_ROLE_ID", required=True)
STAFF_ROLE_ID = get_env_variable("STAFF_ROLE_ID", required=True)


@bot.tree.command(description="Shows you what commands you can use.")
async def help(interaction: discord.Interaction):
    gold_colour = 0xFFD700
    PREFIX = "\u200B\n"  # 'Zero Width Space' & 'New Line'
    embed = discord.Embed(
        title="Commands  |  Help\n-=-=-=-=-=-=-=-=-=-=-=-=-=-", colour=gold_colour
    )
    embed.set_thumbnail(url=bot.user.display_avatar.url)
    embed.add_field(
        name=PREFIX + "/message <content>",
        value="Order me to send a message",
        inline=False,
    )
    embed.add_field(
        name=PREFIX + "/thread <name>",
        value="Order me to create a thread in current channel",
        inline=False,
    )
    embed.add_field(name=PREFIX + "/ping", value="Check my reflexes.", inline=True)
    embed.add_field(
        name=PREFIX + "/github",
        value="I'll give a link to my source code.",
        inline=True,
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(description="Check the latency of the bot.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"⏱️ Pong! ⏱️\nConnection speed is {round(bot.latency * 1000)}ms", ephemeral=True
    )


@bot.tree.command(description="Get link to the GitHub repository.")
async def github(interaction: discord.Interaction):
    github_url = "https://github.com/SERLatBTH/discord"
    view = discord.ui.View()
    button = discord.ui.Button(
        label="GitHub Repository", url=github_url, style=discord.ButtonStyle.link
    )
    view.add_item(button)
    await interaction.response.send_message(view=view, ephemeral=True)


@bot.tree.command(description="Send a message to the channel.")
async def confirm(interaction: discord.Interaction):
    await interaction.response.send_message("Amazing", ephemeral=True)
    if await user_has_confirmed(interaction, bot):
        await interaction.followup.send("Confirmed", ephemeral=True)


@bot.tree.command(description="Command me to send, change or delete my messages.")
@app_commands.describe(action="Select the type of action you want to perform.")
@app_commands.describe(target="Select the target ID to send, edit or delete.")
@app_commands.describe(
    source="Copy or move from source message ID to target channel ID."
)
async def message(
    interaction: discord.Interaction,
    action: Literal["send", "edit", "delete", "copy", "move"],
    target: Optional[str] = None,
    source: Optional[str] = None,
):
    if not await user_has_access(interaction, ADMIN_ROLE_ID, minimum=True):
        return

    message = Command.Message(bot=bot, interaction=interaction)
    await interaction.response.send_message(
        f"You selected to `{action}` a message", ephemeral=True
    )
    if action == "send":
        await message.send(target, source)
    elif action == "edit":
        await message.edit(target, source)
    elif action == "delete":
        await message.delete(target, source)
    elif action == "copy":
        await message.copy(target, source)
    elif action == "move":
        await message.move(target, source)


@bot.tree.command(description="Create a thread in the current channel.")
async def thread(interaction: discord.Interaction, name: str):
    thread = await interaction.channel.create_thread(
        name=name, auto_archive_duration=60
    )
    await interaction.response.send_message(
        f"Thread created: {thread.mention} or {thread.jump_url}", ephemeral=True
    )


if __name__ == "__main__":
    token = get_env_variable("DISCORD_TOKEN", required=True)
    bot.run(token, reconnect=True)
    print("Bot exited on " + time.strftime("%Y-%m-%d %H:%M:%S"))
