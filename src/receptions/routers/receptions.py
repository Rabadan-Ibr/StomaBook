from fastapi import APIRouter, Depends, Response
from starlette import status

from users.models.users import Role
from users.services.auth import AuthService
from users.tables import UserDB
from ..models.receptions import Reception, ReceptionCreate
from ..services.receptions import ReceptionsService

reception_router = APIRouter(
    prefix='/receptions',
    tags=['Receptions']
)


@reception_router.get('/', response_model=list[Reception])
def read_receptions(
        reception_service: ReceptionsService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    pass


@reception_router.post('/', response_model=Reception)
def create_reception(
        reception_data: ReceptionCreate,
        reception_service: ReceptionsService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    pass
