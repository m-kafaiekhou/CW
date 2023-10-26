from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Book API"
    secret_key: str
    jwt_algorithm: str

    class Config:
        env_file = '.env'

settings = Settings()


@lru_cache
def get_settings():
    return settings