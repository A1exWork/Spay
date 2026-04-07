from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path
# Определяем путь к корню проекта (где лежит .env)
BASE_DIR = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    PROJECT_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Указываем абсолютный путь к .env
    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, ".env"))

settings = Settings()

