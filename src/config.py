from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False

    # Database
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "tzeffectivemobile"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"


    class Config:
        env_file = ".env"


settings = Settings()