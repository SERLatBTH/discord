import asyncio
import os

import discord
from dotenv import load_dotenv
from typing import Protocol, runtime_checkable

load_dotenv()


def get_env_variable(name, default=None, required=False):
    """Get an environment variable or raise an error if required and missing.

    Args:
        name (str): The name of the environment variable.
        default (any, optional): The default value to return if the variable is not set. Defaults to None.
        required (bool, optional): If True, raises an error if the variable is missing. Defaults to False.

    Returns:
        str: The value of the environment variable.

    Raises:
        NameError: If the required variable is missing.
    """
    try:
        return os.environ[name]
    except KeyError:
        if required:
            raise NameError(f"{name} environment variable is missing and is required.")
        return default

@runtime_checkable
class SupportsIntCast(Protocol):
    def __int__(self) -> int:
        ...


async def user_has_access(
    interaction: discord.Interaction, role_id: SupportsIntCast, minimum: bool = False
) -> bool:
    """Check if the user has the required role to access the command.

    Args:
        interaction (discord.Interaction): The interaction object.
        role_id (int): The role id required to access the command.
        minimum (bool, optional): If True, checks if the user has a role equal to or higher than the target role.

    Returns:
        bool: True if the user has the role, False otherwise.
    """
    try:
        role_id = int(role_id)
    except ValueError:
        print(f"{role_id} is not a valid role id. It must be an integer.")
        return False

    target_role = interaction.guild.get_role(role_id)
    if target_role is None:
        print(f"{role_id} is not a valid role id. Does it exist in the server?")
        return False

    command = interaction.data["name"]

    has_no_permission_level = interaction.user.top_role < target_role
    has_no_permission_role = target_role not in interaction.user.roles
    failed_permission = (minimum and has_no_permission_level) or has_no_permission_role

    if failed_permission:
        message = f"You don't have permission for /{command}, {target_role.mention} {'or higher' if minimum else ''} is required"
        await interaction.response.send_message(
            message,
            ephemeral=True,
            delete_after=15,
        )
        return False

    return True


async def user_has_confirmed(
    interaction: discord.Interaction,
    bot: discord.Client,
    content: str = "Are you sure you want to proceed?",
) -> bool:
    """Check if the user has confirmed the action by typing 'yes' or 'no'.

    Args:
        interaction (discord.Interaction): The interaction object.
        bot (discord.Client): The bot object.
        content (str, optional): The message to display to the user. Defaults to "Are you sure you want to proceed?".

    Returns:
        bool: True if the user has confirmed, False otherwise.
    """

    is_author_same_as_user = lambda message: message.author == interaction.user and message.channel == interaction.channel

    try:
        message = await interaction.channel.send(
            content + "\nPlease type `yes` or `no` to confirm.", delete_after=15
        )
        response = await interaction.channel.fetch_message(message.id)
        response = await bot.wait_for("message", check=is_author_same_as_user, timeout=15)

        is_confirm = response.content.lower() == "yes"

        if not is_confirm:
            await interaction.followup.send("Action cancelled.", ephemeral=True)
            await message.delete()
            return False

        await response.delete()
        await message.delete()
        return True
    except asyncio.TimeoutError:
        await interaction.followup.send("Action timed out.", ephemeral=True)
        return False
