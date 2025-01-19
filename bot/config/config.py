from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import ValidationError
from bot.utils import logger
import sys

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    PATH_TO_PROFILES: str = 'abcd'
    MAX_THREADS: int = 5
    USE_PROXY: bool = True
    HEADLESS: bool = False

try:
    settings = Settings()

except ValidationError as e:
    sys.exit(logger.error(f"Error in .env file: {e}"))

if settings.PATH_TO_PROFILES == 'abcd':
    sys.exit(logger.error(f"Please edit PATH_TO_PROFILES from .env file to continue."))

