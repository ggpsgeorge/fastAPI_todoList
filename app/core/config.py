from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="./.env")
    secret_key: str = Field(default="DEFAULT_SECRET_KEY")
    database_url: str = Field(default="DEFAULT_DATABASE_URL")
    postgres_user: str = Field(default="DEFAULT_POSTGRES_USER")
    postgres_password: str = Field(default="DEFAULT_POSTGRES_PASSWORD")
    postgres_db: str = Field(default="DEFAULT_POSTGRES_DB")

settings = Settings()
