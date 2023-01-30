from pydantic import BaseModel
from .users import User


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class TokenData(User):
    pass
