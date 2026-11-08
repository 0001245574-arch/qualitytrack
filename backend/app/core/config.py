from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    database_url: str = "sqlite:///./qualitytrack.db"
    secret_key: str = "dev-only-change-this-secret"
    access_token_minutes: int = 480
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    @property
    def allowed_origins(self): return [x.strip() for x in self.cors_origins.split(",") if x.strip()]
settings = Settings()
