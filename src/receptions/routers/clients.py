from fastapi import APIRouter, Depends, Response
from starlette import status

from ..models.clients import Client, ClientCreate
from ..services.clients import ClientsService

client_router = APIRouter(
    prefix='/clients',
    tags=['Clients']
)


@client_router.get('/', response_model=list[Client])
def read_clients(client_service: ClientsService = Depends()):
    return client_service.get_list()


@client_router.get('/{client_id}', response_model=Client)
def read_client(client_id: int, client_service: ClientsService = Depends()):
    return client_service.get_item(client_id)


@client_router.post('/', response_model=Client)
def create_client(
        client_data: ClientCreate,
        client_service: ClientsService = Depends()
):
    return client_service.create_item(client_data.dict())


@client_router.put('/{client_id}', response_model=Client)
def update_client(
        client_id: int,
        client_data: ClientCreate,
        client_service: ClientsService = Depends()
):
    return client_service.edit_item(client_id, client_data.dict())


@client_router.delete('/{client_id}')
def delete_client(client_id: int, client_service: ClientsService = Depends()):
    client_service.delete_item(client_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)