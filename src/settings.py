from passlib.context import CryptContext
from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    TOKEN_EXPIRE_HOURS = 2
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

settings = Settings()
