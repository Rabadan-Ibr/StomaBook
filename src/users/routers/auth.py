from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..models.auth import Token


auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@auth_router.get('/sign_in', response_model=Token)
def sign_in(form_data: OAuth2PasswordRequestForm = Depends()):
    pass
