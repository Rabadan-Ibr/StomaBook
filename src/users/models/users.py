from enum import Enum

from pydantic import BaseModel


class Role(str, Enum):
    DOC = 'doc'
    ADMIN = 'admin'


class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    phone: int


class UserCreate(UserBase):
    password: str


class UserEdit(UserBase):
    pass


class UserEditAdmin(BaseModel):
    is_active: bool
    role: str


class UserToDB(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    is_active: bool
    role: str

    class Config:
        orm_mode = True
