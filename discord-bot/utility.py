import os
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
