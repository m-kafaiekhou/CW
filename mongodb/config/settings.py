from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Book API"
    secret_key: str
    jwt_algorithm: str


settings = Settings()
