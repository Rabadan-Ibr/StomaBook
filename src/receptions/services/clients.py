from typing import List, Optional

from fastapi import Depends, HTTPException
from starlette import status

from src.db import SessionLocal, get_session
from ..models.clients import ClientCreate
from ..tables import ClientDB
from common.orm.mixins import CRUDMixin


class ClientsService(CRUDMixin):
    _table = ClientDB

    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session

    def list(self, filters: Optional[dict] = None) -> List[_table]:
        return self._get_list(filters)

    def detail(self, client_id: int) -> _table:
        client = self._get_item(client_id)
        if client is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return client

    def create(self, data: ClientCreate) -> _table:
        return self._create_item(data.dict())

    def edit(self, client_id: int, data: ClientCreate) -> _table:
        client = self.detail(client_id)
        return self._edit_item(client, data.dict())

    def delete(self, client_id: int):
        client = self.detail(client_id)
        self._delete_item(client)
