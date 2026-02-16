from utils.settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool
    ENVIRONMENT: str
    SERVICE_NAME: str
    ROOT_PATH: str


settings = Settings()
