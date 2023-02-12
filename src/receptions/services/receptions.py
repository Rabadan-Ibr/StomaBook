from typing import List

from fastapi import Depends, HTTPException
from starlette import status

from db import SessionLocal, get_session
from users.tables import UserDB
from .clients import ClientsService
from .diagnoses import DiagnosesService
from .procedures import ProceduresService
from ..models.receptions import (ReceptionCreate,
                                 ReceptionCreateDB,
                                 ReceptionEditDB
                                 )
from ..tables import ReceptionDB, DiagReceptionDB, ProcReceptionDB
from common.orm.mixins import CRUDMixin


class ReceptionsService(CRUDMixin):
    _table = ReceptionDB

    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session

    def list(self) -> List[_table]:
        return self._get_list()

    def get(self, reception_id: int) -> _table:
        reception = self._get_item(reception_id)
        if reception is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return reception

    def detail(self, reception_id: int) -> _table:
        return self.get(reception_id)

    def _add_tooth_diag(
            self, data: List, reception: _table, service: DiagnosesService
    ):
        for record_data in data:
            diag = service.get(record_data.diag_id)
            if diag.detail and record_data.tooth is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
            diag_record = DiagReceptionDB(tooth=record_data.tooth)
            diag_record.diagnosis = diag
            reception.diagnoses.append(diag_record)

    def _add_tooth_proc(
            self, data: List, reception: _table, service: ProceduresService
    ):
        for record_data in data:
            proc = service.get(record_data.proc_id)
            if proc.detail and record_data.tooth is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
            proc_record = ProcReceptionDB(tooth=record_data.tooth)
            proc_record.procedure = proc
            reception.procedures.append(proc_record)

    def create(
            self,
            data: ReceptionCreate,
            user: UserDB,
            proc_service: ProceduresService,
            diag_service: DiagnosesService,
            client_service: ClientsService
    ):
        client_service.detail(data.client_id)
        reception_data = ReceptionCreateDB(**data.dict(), doctor_id=user.id)
        reception = self._create_item_m2m(reception_data.dict())

        self._add_tooth_diag(data.diagnoses, reception, diag_service)
        self._add_tooth_proc(data.procedures, reception, proc_service)

        self._session.commit()
        return reception

    def edit(
            self,
            reception_id: int,
            data: ReceptionCreate,
            user: UserDB,
            proc_service: ProceduresService,
            diag_service: DiagnosesService,
            client_service: ClientsService
    ):
        reception = self.get(reception_id)
        if reception.doctor_id != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        client_service.detail(data.client_id)
        reception_data = ReceptionEditDB(**data.dict())
        reception = self._edit_item_m2m(reception, reception_data.dict())

        for proc in reception.procedures:
            self._session.delete(proc)
        for diag in reception.diagnoses:
            self._session.delete(diag)

        self._add_tooth_diag(data.diagnoses, reception, diag_service)
        self._add_tooth_proc(data.procedures, reception, proc_service)

        self._session.commit()
        return reception
