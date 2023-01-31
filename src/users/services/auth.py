from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status

from db import SessionLocal, get_session
from settings import pwd_context, settings
from users.models.auth import Token, TokenData
from users.models.users import Role, User
from common.orm.mixins import RetrieveMixin
from users.tables import UserDB

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/sign_in')


class LoginService(RetrieveMixin):
    _table = UserDB

    @classmethod
    def create_token(cls, user: UserDB) -> Token:
        now = datetime.now()
        expire = now + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTE)
        token_data = TokenData(
            exp=expire,
            sub=str(user.id),
            user=user
        )
        token = jwt.encode(
            token_data.dict(), settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return Token(access_token=token)

    @classmethod
    def verify_password(cls, password: str, hashed_password: str) -> bool:
        return pwd_context.verify(password, hashed_password)

    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session

    def authenticate_user(self, username: str, password: str) -> Token:
        user = self._get_by_field('username', username)
        if user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        if not self.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return self.create_token(user)


class AuthService(RetrieveMixin):
    _table = UserDB

    @classmethod
    def decode_token(cls, token: str) -> dict:
        try:

            payload = jwt.decode(
                token, settings.SECRET_KEY, settings.ALGORITHM
            )
            return payload
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    def __call__(
            self,
            token: str = Depends(oauth2_scheme),
            session: SessionLocal = Depends(get_session)
    ):
        self._session = session
        token_data = self.decode_token(token)
        if token_data is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        user_from_token = User(**token_data.get('user'))
        user = self._get_by_field('username', user_from_token.username)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

        if self.role == Role.ADMIN and user.role != Role.ADMIN:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        return user

    def __init__(self, role: Optional[Role] = None):
        self.role = role
