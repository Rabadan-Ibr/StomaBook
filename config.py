from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Settings(BaseSettings):
    app_name: str = 'StomaBook'
    admin_email: str = 'raba@mail.ru'


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
