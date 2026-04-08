from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path

# Определяем путь к корню проекта (где лежит .env)
BASE_DIR = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    # Название проекта (SPay SeriousPay Engine)
    PROJECT_NAME: str = "SPay SeriousPay Engine"
    
    # PostgreSQL настройки из .env
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # 🔥 Async URL для FastAPI (использует asyncpg — асинхронный драйвер)
    @property
    def database_url_async(self) -> str:
        """URL для FastAPI: postgresql+asyncpg://... (async режим)"""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # 🔥 Sync URL для Alembic (использует psycopg2 — синхронный драйвер)
    @property
    def database_url_sync(self) -> str:
        """URL для Alembic: postgresql+psycopg2://... (sync режим)"""
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Указываем абсолютный путь к .env файлу
    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, ".env"))

# Создаём глобальный объект settings
settings = Settings()

