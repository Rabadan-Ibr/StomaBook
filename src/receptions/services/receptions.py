from fastapi import Depends

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
        print(reception)
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
