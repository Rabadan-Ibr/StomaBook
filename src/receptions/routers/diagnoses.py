from typing import Optional

from fastapi import APIRouter, Depends, Response
from starlette import status

from users.models.users import Role
from users.services.auth import AuthService
from users.tables import UserDB
from ..models.diagnoses import Diagnosis, DiagnosisCreate
from ..services.diagnoses import DiagnosesService

diagnosis_router = APIRouter(
    prefix='/diagnoses',
    tags=['Diagnoses']
)


def diagnosis_filters(name: Optional[str] = None):
    return {'name': name}


@diagnosis_router.get('/', response_model=list[Diagnosis])
def read_diagnoses(
        filters: dict = Depends(diagnosis_filters),
        diagnosis_service: DiagnosesService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return diagnosis_service.list(filters)


@diagnosis_router.post('/', response_model=Diagnosis)
def create_diagnosis(
        diagnosis_data: DiagnosisCreate,
        diagnosis_service: DiagnosesService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return diagnosis_service.create(diagnosis_data)


@diagnosis_router.put('/{diag_id}', response_model=Diagnosis)
def update_diagnosis(
        diag_id: int,
        diagnosis_data: DiagnosisCreate,
        diagnosis_service: DiagnosesService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return diagnosis_service.edit(diag_id, diagnosis_data)


@diagnosis_router.delete('/{diag_id}')
def delete_diagnosis(
        diag_id: int,
        diagnosis_service: DiagnosesService = Depends(),
        user: UserDB = Depends(AuthService(Role.ADMIN))
):
    diagnosis_service.delete(diag_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
