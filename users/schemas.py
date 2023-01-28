from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


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


class UserDBSchem(UserBaseSchem):
    hashed_password: str


class UserSchem(UserBaseSchem):
    id: int
    is_active: bool
    role: str

    class Config:
        orm_mode = True
