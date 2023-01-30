from typing import List

from fastapi import Depends, HTTPException
from starlette import status

from db import SessionLocal, get_session
from ..models.procedures import ProcedureCreate
from ..tables import ProcedureDB
from common.orm.mixins import CRUDMixin


class ProceduresService(CRUDMixin):
    _table = ProcedureDB

    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session

    def list(self) -> List[_table]:
        return self._get_list()

    def create(self, data: ProcedureCreate) -> _table:
        exists = self._get_by_field('name', data.name)
        if exists:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return self._create_item(data.dict())

    def edit(self, proc_id: int, data: ProcedureCreate) -> _table:
        procedure = self._get_item(proc_id)
        if procedure is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return self._edit_item(procedure, data.dict())

    def delete(self, proc_id: int):
        procedure = self._get_item(proc_id)
        if procedure is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        self._delete_item(procedure)
