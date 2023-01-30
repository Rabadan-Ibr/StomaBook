from fastapi import Depends, HTTPException
from starlette import status

from common.orm.mixins import RetrieveMixin, CreateMixin, UpdateMixin
from db import SessionLocal, get_session
from settings import pwd_context
from users.models.users import UserCreate, UserToDB
from users.tables import UserDB


class UserService(RetrieveMixin, CreateMixin, UpdateMixin):
    _table = UserDB

    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session

    def create_user(self, data: UserCreate) -> _table:
        unique_fields: tuple = ('username', 'email', 'phone')
        for field in unique_fields:
            if self._get_by_field(field, getattr(data, field)):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        hashed_password = pwd_context.hash(data.password)
        user = UserToDB(**data.dict(), hashed_password=hashed_password)
        return self._create_item(user.dict())

    def edit_user(self, user_id: int, data: UserCreate) -> _table:
        unique_fields: tuple = ('username', 'email', 'phone')
        for field in unique_fields:
            if self._get_by_field(field, getattr(data, field)):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        user = self._get_item(user_id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        hashed_password = pwd_context.hash(data.password)
        user_data = UserToDB(**data.dict(), hashed_password=hashed_password)
        return self._edit_item(user, user_data.dict())
