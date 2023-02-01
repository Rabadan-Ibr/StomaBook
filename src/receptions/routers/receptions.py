from fastapi import APIRouter, Depends, Response
from starlette import status

from users.models.users import Role
from users.services.auth import AuthService
from users.tables import UserDB
from ..models.receptions import Reception, ReceptionCreate
from ..services.clients import ClientsService
from ..services.diagnoses import DiagnosesService
from ..services.procedures import ProceduresService
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
    return reception_service.list()


@reception_router.post('/', response_model=Reception)
def create_reception(
        reception_data: ReceptionCreate,
        reception_service: ReceptionsService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC)),
        proc_service: ProceduresService = Depends(),
        diag_service: DiagnosesService = Depends(),
        client_service: ClientsService = Depends()
):
    return reception_service.create(
        reception_data, user, proc_service, diag_service, client_service
    )


@reception_router.get('/{reception_id}', response_model=Reception)
def read_reception(
        reception_id: int,
        reception_service: ReceptionsService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return reception_service.detail(reception_id)


@reception_router.put('/{reception_id}', response_model=Reception)
def update_reception(
        reception_id: int,
        reception_data: ReceptionCreate,
        reception_service: ReceptionsService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC)),
        proc_service: ProceduresService = Depends(),
        diag_service: DiagnosesService = Depends(),
        client_service: ClientsService = Depends()
):
    return reception_service.edit(
        reception_id,
        reception_data,
        user,
        proc_service,
        diag_service,
        client_service
    )
