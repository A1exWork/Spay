from pydantic_settings import BaseSettings, SettingsConfigDict

# 1. Описываем класс (чертеж) наших настроек
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

    model_config = SettingsConfigDict(env_file=".env")

# 2. Создаем ОБЪЕКТ настроек (именно его мы импортируем в main.py)
settings = Settings()
