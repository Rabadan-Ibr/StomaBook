from typing import List

from fastapi import APIRouter, Depends
from ..models.users import User, UserCreate
from ..services.auth import AuthService
from ..services.users import UserService
from ..tables import UserDB

user_router = APIRouter(
    prefix='/users',
    tags=['User']
)


@user_router.get('/', response_model=List[User])
def get_users(user_service: UserService = Depends()):
    return user_service.list()


@user_router.post('/', response_model=User)
def create_user(user_data: UserCreate, user_service: UserService = Depends()):
    return user_service.create_user(user_data)


@user_router.put('/{user_id}', response_model=User)
def update_user(
        user_id: int,
        user_data: UserCreate,
        user_service: UserService = Depends()
):
    return user_service.edit_user(user_id, user_data)


@user_router.get('/me', response_model=User)
def get_me(user: UserDB = Depends(AuthService())):
    return user
