"""
Configs
"""

import environ


@environ.config()
class Config:
    """
    Config class inherited from environ.config.
    """

    token: str = environ.var(converter=str, name="TOKEN", help="Access token for bot")


def read_config_from_env() -> Config:
    """
    Generate Config object from environ variables.

    Returns:
        Config
    """
    # Reads from os.environ by default
    env: Config = environ.to_config(Config)
    return env
