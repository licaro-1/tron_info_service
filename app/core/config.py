from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    DATABASE_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    TRON_API_KEY: str

    class Config:
        env_file = (
            BASE_DIR / ".env-example",
            BASE_DIR / ".env"
        )


settings = Settings()
