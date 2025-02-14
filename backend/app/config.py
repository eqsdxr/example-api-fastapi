from functools import lru_cache
from environs import Env

path_to_env = ".env"


@lru_cache
def get_config():
    """Load and cache configuration from .env.

    Raise errors if some value is missing or .env doesn't exist.
    """
    env = Env()
    env.read_env(path_to_env, recurse=False)

    class EnvData:
        environment: str = env.str("environment")
        database_url: str = env.str("database_url")
        jwt_secret_key: str = env.str("jwt_secret_key")
        jwt_algorithm: str = env.str("jwt_algorithm")
        first_user_username: str = env.str("first_user_username")
        first_user_password: str = env.str("first_user_password")
        access_token_duration_hours: int = env.int(
            "access_token_duration_hours"
        )

    env_data = EnvData()
    return env_data


main_config = get_config()
