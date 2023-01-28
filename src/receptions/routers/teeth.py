from fastapi import APIRouter, Depends, Response
from starlette import status

from ..models.teeth import Tooth, ToothCreate
from ..services.teeth import TeethService

tooth_router = APIRouter(
    prefix='/teeth',
    tags=['Teeth']
)


@tooth_router.get('/', response_model=list[Tooth])
def read_teeth(
        tooth_service: TeethService = Depends()
):
    return tooth_service.get_list()


@tooth_router.get('/{tooth_id}', response_model=Tooth)
def read_tooth(
        tooth_id: int,
        tooth_service: TeethService = Depends()
):
    return tooth_service.get_item(tooth_id)


@tooth_router.post('/', response_model=Tooth)
def create_tooth(
        tooth_data: ToothCreate,
        tooth_service: TeethService = Depends()
):
    return tooth_service.create_item(tooth_data.dict())


@tooth_router.put('/{tooth_id}', response_model=Tooth)
def update_tooth(
        tooth_id: int,
        tooth_data: ToothCreate,
        tooth_service: TeethService = Depends()
):
    return tooth_service.edit_item(tooth_id, tooth_data.dict())


@tooth_router.delete('/{tooth_id}')
def delete_tooth(
        tooth_id: int,
        tooth_service: TeethService = Depends()
):
    tooth_service.delete_item(tooth_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)