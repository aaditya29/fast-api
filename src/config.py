from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    # load variables from .env file
    model_config = SettingsConfigDict(env_file=".env",
                                      extra="ignore")
