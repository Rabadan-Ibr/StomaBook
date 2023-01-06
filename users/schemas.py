from pydantic import BaseModel, validator

from dependency import get_db
from users.models import User


class TokenData(BaseModel):
    id: int
    username: str


class UserBaseSchem(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    phone: int


class UserCreateSchem(UserBaseSchem):
    password: str

    @validator('username')
    def username_must_unique(cls, v: str):
        db = next(get_db())
        username = v.lower()
        db_item = db.query(User).filter_by(username=username).first()
        if db_item is not None:
            raise ValueError('must be unique')
        return username

    @validator('email')
    def email_must_unique(cls, v: str):
        db = next(get_db())
        email = v.lower()
        db_item = db.query(User).filter_by(email=email).first()
        if db_item is not None:
            raise ValueError('must be unique')
        return email

    @validator('phone')
    def phone_must_unique(cls, v: int):
        db = next(get_db())
        db_item = db.query(User).filter_by(phone=v).first()
        if db_item is not None:
            raise ValueError('must be unique')
        return v


class UserSchem(UserBaseSchem):
    id: int
    is_active: bool
    role: str

    class Config:
        orm_mode = True
