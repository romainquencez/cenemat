from pydantic import BaseSettings


class Settings(BaseSettings):
    # Database
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_port: int
    postgres_host: str

    # FastAPI
    fastapi_allow_origin: str

    # JWT
    jwt_secret_key: str
    jwt_access_token_expire_minutes: int
    jwt_algorithm: str

    # Sentry
    sentry_dsn: str | None


settings = Settings()
