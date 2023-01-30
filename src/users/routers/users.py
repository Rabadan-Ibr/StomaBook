from fastapi import APIRouter, Depends
from ..models.users import User, UserCreate
from ..services.users import UserService

user_router = APIRouter(
    prefix='/users',
    tags=['User']
)


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







# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#
# from fastapi import APIRouter, Depends, HTTPException
# from users.schemas import UserSchem, UserCreateSchem, UserDBSchem, TokenData, Token
# from cruds import get_list, get_by_id, create_item, get_by_field
# from users.models import User
# from config import pwd_context
# from users.utils import create_access_token
#
#

#
#
# @user_router.post('/users/login/', response_model=Token)
# def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
#     try:
#         user = get_by_field('username', form_data.username, User)
#         if not pwd_context.verify(form_data.password, user.hashed_password):
#             raise Exception()
#     except (HTTPException, Exception):
#         raise HTTPException(status_code=400, detail='Wrong password or username.')
#     token_data = TokenData(id=user.id, username=user.username).dict()
#     token = create_access_token(token_data)
#     return {"access_token": token, "token_type": "bearer"}
