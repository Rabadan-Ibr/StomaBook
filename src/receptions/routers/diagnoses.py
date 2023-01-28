from fastapi import APIRouter, Depends, Response
from starlette import status

from ..models.diagnoses import Diagnosis, DiagnosisCreate
from ..services.diagnoses import DiagnosesService

diagnosis_router = APIRouter(
    prefix='/diagnoses',
    tags=['Diagnoses']
)


@diagnosis_router.get('/', response_model=list[Diagnosis])
def read_diagnoses(
        diagnosis_service: DiagnosesService = Depends()
):
    return diagnosis_service.get_list()


@diagnosis_router.get('/{diag_id}', response_model=Diagnosis)
def read_diagnosis(
        diag_id: int,
        diagnosis_service: DiagnosesService = Depends()
):
    return diagnosis_service.get_item(diag_id)


@diagnosis_router.post('/', response_model=Diagnosis)
def create_diagnosis(
        diagnosis_data: DiagnosisCreate,
        diagnosis_service: DiagnosesService = Depends()
):
    return diagnosis_service.create_item(diagnosis_data.dict())


@diagnosis_router.put('/{diag_id}', response_model=Diagnosis)
def update_diagnosis(
        diag_id: int,
        diagnosis_data: DiagnosisCreate,
        diagnosis_service: DiagnosesService = Depends()
):
    return diagnosis_service.edit_item(diag_id, diagnosis_data.dict())


@diagnosis_router.delete('/{diag_id}')
def delete_diagnosis(
        diag_id: int,
        diagnosis_service: DiagnosesService = Depends()
):
    diagnosis_service.delete_item(diag_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)