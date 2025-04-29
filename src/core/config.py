from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Student Growth Backend"
    db_url: str

    class Config:
        env_file = ".env"

settings = Settings()
