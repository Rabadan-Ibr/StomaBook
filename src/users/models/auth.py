from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from .users import User


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class TokenData(BaseModel):
    exp: datetime
    sub: str
    user: Optional[User] = None
