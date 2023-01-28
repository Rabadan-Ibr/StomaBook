from fastapi import APIRouter, Depends, Response
from starlette import status

from ..models.procedures import Procedure, ProcedureCreate
from ..services.procedures import ProceduresService

procedure_router = APIRouter(
    prefix='/procedures',
    tags=['Procedures']
)


@procedure_router.get('/', response_model=list[Procedure])
def read_procedures(
        procedure_service: ProceduresService = Depends()
):
    return procedure_service.get_list()


@procedure_router.get('/{proc_id}', response_model=Procedure)
def read_procedure(
        proc_id: int,
        procedure_service: ProceduresService = Depends()
):
    return procedure_service.get_by_id(proc_id)


@procedure_router.post('/', response_model=Procedure)
def create_procedure(
        procedure_data: ProcedureCreate,
        procedure_service: ProceduresService = Depends()
):
    return procedure_service.create(procedure_data)


@procedure_router.put('/{proc_id}', response_model=Procedure)
def change_procedure(
        proc_id: int,
        procedure_data: ProcedureCreate,
        procedure_service: ProceduresService = Depends()
):
    return procedure_service.edit(proc_id, procedure_data)


@procedure_router.delete('/{proc_id}')
def delete_procedure(
        proc_id: int,
        procedure_service: ProceduresService = Depends()
):
    procedure_service.delete(proc_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)