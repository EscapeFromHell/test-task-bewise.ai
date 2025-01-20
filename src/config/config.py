import aiokafka
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_V1_STR: str = "/api_v1"
    USER: str = "postgres"
    PASSWORD: str = "password"
    HOST: str = "applications-db"
    PORT: str = "5432"
    NAME: str = "applications"
    TEST_HOST: str = "test_applications-db"
    TEST_NAME: str = "test_applications"

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"

    @property
    def TEST_DB_URL(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.TEST_HOST}:{self.PORT}/{self.TEST_NAME}"

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost",
        "http://127.0.0.1",
    ]
    BACKEND_HOST_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost",
        "http://127.0.0.1",
    ]

    @field_validator("BACKEND_CORS_ORIGINS")
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
