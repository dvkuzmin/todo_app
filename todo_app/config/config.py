import os
from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent
os.path.join(BASE_DIR)

class Settings(BaseSettings):
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_ROOT_PASSWORD: str

    @property
    def db_uri(self) -> str:
        return f'mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:' \
               f'{self.MYSQL_PORT}/{self.MYSQL_DATABASE}'

    class Config:
        env_file = BASE_DIR / '.env'