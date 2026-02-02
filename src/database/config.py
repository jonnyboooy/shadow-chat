from pydantic import computed_field

from ..core.settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.DATABASE_USER,
            self.DATABASE_PASSWORD,
            self.DATABASE_HOST,
            self.DATABASE_PORT,
            self.DATABASE_NAME
        )


settings = Settings()
