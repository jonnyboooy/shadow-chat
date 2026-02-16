from pathlib import Path

from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(PydanticBaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=Path(__file__).resolve().parent.parent / ".env",
        extra="ignore"
    )
