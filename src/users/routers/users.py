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
# user_router = APIRouter(tags=['users'])
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
#
#
# @user_router.get('/users/', response_model=list[UserSchem])
# def read_users():
#     return get_list(User)
#
#
# @user_router.post('/users/', response_model=UserSchem)
# def create_user(user_schem: UserCreateSchem):
#     hashed_password = pwd_context.hash(user_schem.password)
#     user = UserDBSchem(**user_schem.dict(), hashed_password=hashed_password)
#     return create_item(user, User)
#
#
# @user_router.get('/users/{user_id}', response_model=UserSchem)
# def read_user(user_id: int):
#     return get_by_id(user_id, User)
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
