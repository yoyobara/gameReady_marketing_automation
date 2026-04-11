# pydantic settings from env

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", validate_default=True)

    heygen_api_key: str
    webhook_url: HttpUrl


settings = Settings()
