from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./db.sqlite3"
    TRON_API_KEY: str

    class Config:
        env_file = (".env", ".env-example")


settings = Settings()
