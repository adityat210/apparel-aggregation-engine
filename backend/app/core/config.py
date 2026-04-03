from pydantic_settings import BaseSettings, SettingsConfigDict
#let's backend use SQLite for local fallback, Postgre when DATABASE_URL is provided by docker compose
class Settings(BaseSettings):
    database_url: str = "sqlite:///./app.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
#SQLite needs check_same_thread = False but Postgre doesn't