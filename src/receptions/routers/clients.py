from typing import Optional

from fastapi import APIRouter, Depends, Response
from starlette import status

from users.models.users import Role
from users.services.auth import AuthService
from users.tables import UserDB
from ..models.clients import Client, ClientCreate
from ..services.clients import ClientsService

client_router = APIRouter(
    prefix='/clients',
    tags=['Clients']
)


def client_filters(
        phone: Optional[int] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None
):
    return {'phone': phone, 'first_name': first_name, 'last_name': last_name}


@client_router.get('/', response_model=list[Client])
def read_clients(
        filters: dict = Depends(client_filters),
        client_service: ClientsService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return client_service.list(filters)


@client_router.get('/{client_id}', response_model=Client)
def read_client(
        client_id: int,
        client_service: ClientsService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return client_service.detail(client_id)


@client_router.post('/', response_model=Client)
def create_client(
        client_data: ClientCreate,
        client_service: ClientsService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return client_service.create(client_data)


@client_router.put('/{client_id}', response_model=Client)
def update_client(
        client_id: int,
        client_data: ClientCreate,
        client_service: ClientsService = Depends(),
        user: UserDB = Depends(AuthService(Role.DOC))
):
    return client_service.edit(client_id, client_data)


@client_router.delete('/{client_id}')
def delete_client(
        client_id: int,
        client_service: ClientsService = Depends(),
        user: UserDB = Depends(AuthService(Role.ADMIN))
):
    client_service.delete(client_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
