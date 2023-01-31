from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..models.auth import Token
from ..services.auth import LoginService

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@auth_router.post('/sign_in', response_model=Token)
def sign_in(
        form_data: OAuth2PasswordRequestForm = Depends(),
        login_service: LoginService = Depends()
):
    return login_service.authenticate_user(
        form_data.username, form_data.password
    )
