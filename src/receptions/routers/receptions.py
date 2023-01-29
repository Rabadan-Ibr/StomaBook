from fastapi import APIRouter, Depends, Response
from starlette import status

from ..models.receptions import Reception, ReceptionCreate
from ..services.receptions import ReceptionsService

reception_router = APIRouter(
    prefix='/receptions',
    tags=['Receptions']
)


@reception_router.get('/', response_model=list[Reception])
def read_receptions(reception_service: ReceptionsService = Depends()):
    return reception_service.get_list()
