from passlib.context import CryptContext
from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Settings(BaseSettings):
    app_name: str = 'StomaBook'
    admin_email: str = 'raba@mail.ru'
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    TOKEN_EXPIRE_HOURS = 2


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

ROLES = [
        ('admin', 'Admin'),
        ('doc', 'Doctor')
    ]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

settings = Settings()
