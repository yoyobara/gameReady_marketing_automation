# pydantic settings from env

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    port: int = 8000
    host: str = "0.0.0.0"
