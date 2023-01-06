from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from dependency import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Body
from users.schemas import UserSchem, UserCreateSchem, UserBaseSchem, TokenData
from cruds import get_list, get_by_id
from users.models import User
from config import pwd_context
from users.utils import create_access_token


user_router = APIRouter(tags=['users'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


@user_router.get('/users/', response_model=list[UserSchem])
def read_users(db: Session = Depends(get_db)):
    return get_list(db, User)


@user_router.post('/users/', response_model=UserSchem)
def create_user(user_schem: UserCreateSchem, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user_schem.password)
    user = UserBaseSchem(**user_schem.dict())
    db_user = User(**user.dict(), hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@user_router.get('/users/{user_id}', response_model=UserSchem)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_by_id(db, user_id, User)


@user_router.post('/users/login/')
def user_login(
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user = db.query(User).filter_by(username=form_data.username).first()
    if user is None:
        raise HTTPException(status_code=400, detail='Wrong password or username.')
    if not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail='Wrong password or username.')
    token_data = TokenData(id=user.id, username=user.username).dict()
    token = create_access_token(token_data)
    return {"access_token": token, "token_type": "bearer"}
