import os
import discord
from dotenv import load_dotenv

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


async def user_has_access(
    interaction: discord.Interaction, role_id: int, minimum: bool = False
):
    """Check if the user has the required role to access the command.

    Args:
        interaction (discord.Interaction): The interaction object.
        role_id (int): The role ID to check.
        minimum (bool, optional): If True, checks if the user has a role equal to or higher than the target role.

    Returns:
        bool: True if the user has the role, False otherwise.
    """

    try:
        target_role = interaction.guild.get_role(int(role_id))
        if target_role is None:
            raise NameError(
                f"{role_id} is not a valid role id. Does it exist in the server?"
            )
    except ValueError:
        raise NameError(f"{role_id} is not a valid role id. It must be an integer.")

    fail = False
    message = ""
    command = interaction.data["name"]

    if minimum:
        fail = interaction.user.top_role < target_role
        message = f"You don't have permission for /{command}, {target_role.mention} or higher is required"
    else:
        fail = target_role not in interaction.user.roles
        message = f"You don't have permission for /{command}, {target_role.mention} is required"

    if fail:
        await interaction.response.send_message(
            message,
            ephemeral=True,
            delete_after=15,
        )
        return False
    else:
        return True
