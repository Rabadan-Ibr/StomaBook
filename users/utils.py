from datetime import timedelta, datetime

from jose import jwt
from config import settings


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=settings.TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )