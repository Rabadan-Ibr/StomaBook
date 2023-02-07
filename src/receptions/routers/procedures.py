from typing import Optional

from fastapi import APIRouter, Depends, Response
from starlette import status

from users.models.users import Role
from users.services.auth import AuthService
from users.tables import UserDB
from ..models.procedures import Procedure, ProcedureCreate
from ..services.procedures import ProceduresService

procedure_router = APIRouter(
    prefix='/procedures',
    tags=['Procedures']
)


@procedure_router.get('/', response_model=list[Procedure])
def read_procedures(
        name: Optional[str] = None,
        procedure_service: ProceduresService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return procedure_service.list(name)


@procedure_router.post('/', response_model=Procedure)
def create_procedure(
        procedure_data: ProcedureCreate,
        procedure_service: ProceduresService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return procedure_service.create(procedure_data)


@procedure_router.put('/{proc_id}', response_model=Procedure)
def update_procedure(
        proc_id: int,
        procedure_data: ProcedureCreate,
        procedure_service: ProceduresService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return procedure_service.edit(proc_id, procedure_data)


@procedure_router.delete('/{proc_id}')
def delete_procedure(
        proc_id: int,
        procedure_service: ProceduresService = Depends(),
        user: UserDB = Depends(AuthService(Role.ADMIN))
):
    procedure_service.delete(proc_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)