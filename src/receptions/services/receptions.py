from fastapi import Depends, HTTPException
from starlette import status

from db import SessionLocal, get_session
from users.tables import UserDB
from .clients import ClientsService
from .diagnoses import DiagnosesService
from .procedures import ProceduresService
from ..models.receptions import ReceptionCreate, ReceptionToDB
from ..tables import ReceptionDB, DiagReceptionDB, ProcReceptionDB
from common.orm.mixins import CRUDMixin


class ReceptionsService(CRUDMixin):
    _table = ReceptionDB

    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session

    def list(self):
        return self._get_list()

    def get(self, reception_id: int):
        reception = self._get_item(reception_id)
        if reception is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return reception

    def detail(self, reception_id: int):
        return self.get(reception_id)

    def create(
            self,
            data: ReceptionCreate,
            user: UserDB,
            proc_service: ProceduresService,
            diag_service: DiagnosesService,
            client_service: ClientsService
    ):
        client_service.detail(data.client_id)
        reception_data = ReceptionToDB(**data.dict(), doctor_id=user.id)
        reception = self._create_item(reception_data.dict())
        for diag_record_data in data.diagnoses:
            diag = diag_service.get(diag_record_data.diag_id)
            diag_record = DiagReceptionDB(tooth=diag_record_data.tooth)
            diag_record.diagnosis = diag
            reception.diagnoses.append(diag_record)
        for proc_record_data in data.procedures:
            proc = proc_service.get(proc_record_data.proc_id)
            proc_record = ProcReceptionDB(tooth=proc_record_data.tooth)
            proc_record.procedure = proc
            reception.procedures.append(proc_record)
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
        client_service.detail(data.client_id)
        reception = self.get(reception_id)
        reception_data = ReceptionToDB(**data.dict(), doctor_id=user.id)
        reception = self._edit_item(reception, reception_data.dict())
        if reception.doctor_id != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        for proc in reception.procedures:
            self._session.delete(proc)
        for diag in reception.diagnoses:
            self._session.delete(diag)
        print(reception.procedures)
        for diag_record_data in data.diagnoses:
            diag = diag_service.get(diag_record_data.diag_id)
            diag_record = DiagReceptionDB(tooth=diag_record_data.tooth)
            diag_record.diagnosis = diag
            reception.diagnoses.append(diag_record)
        for proc_record_data in data.procedures:
            proc = proc_service.get(proc_record_data.proc_id)
            proc_record = ProcReceptionDB(tooth=proc_record_data.tooth)
            proc_record.procedure = proc
            reception.procedures.append(proc_record)
        self._session.commit()
        return reception
