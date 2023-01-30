from typing import List

from fastapi import Depends, HTTPException
from starlette import status

from db import SessionLocal, get_session
from ..models.diagnoses import DiagnosisCreate
from ..tables import DiagnosisDB
from common.orm.mixins import CRUDMixin


class DiagnosesService(CRUDMixin):
    _table = DiagnosisDB

    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session

    def list(self) -> List[_table]:
        return self._get_list()

    def create(self, data: DiagnosisCreate) -> _table:
        exists = self._get_by_field('name', data.name)
        if exists:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return self._create_item(data.dict())

    def edit(self, diag_id: int, data: DiagnosisCreate) -> _table:
        diagnosis = self._get_item(diag_id)
        if diagnosis is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return self._edit_item(diagnosis, data.dict())

    def delete(self, diag_id: int):
        diagnosis = self._get_item(diag_id)
        if diagnosis is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        self._delete_item(diagnosis)
