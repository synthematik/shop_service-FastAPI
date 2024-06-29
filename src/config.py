from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    ACCESS_KEY: str
    SECRET_KEY: str
    ENDPOINT_URL: str
    BUCKET_NAME: str

    ALGORITHM: str
    SECRET_KEY: str

    def get_database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    def get_secret_key(self):
        return f"{self.SECRET_KEY}"

    def get_endpoint_url(self):
        return self.ENDPOINT_URL

    def get_bucket_name(self):
        return self.BUCKET_NAME

    def get_access_key(self):
        return self.ACCESS_KEY

    class Config:
        env_file = ".env"


settings = Settings()
