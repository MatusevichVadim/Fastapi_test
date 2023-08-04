from pydantic_settings import BaseSettings
from pydantic import model_validator


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_PORT: int
    DB_HOST: str
    DB_NAME: str

    def get_database_url(self):
        SQLALCHEMY_DATABASE_URL = (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
                                   f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
        return SQLALCHEMY_DATABASE_URL

    class Config:
        env_file = ".env"


settings = Settings()

