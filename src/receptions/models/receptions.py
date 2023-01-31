from typing import Optional, List

from pydantic import BaseModel
from datetime import datetime
from .clients import Client
from users.models.users import User
from .teeth import Teeth
from .procedures import Procedure
from .diagnoses import Diagnosis


class RecordBase(BaseModel):
    tooth: Optional[Teeth] = None


class ProcRecordCreate(RecordBase):
    proc_id: int


class ProcRecord(RecordBase):
    proc_id: Procedure


class DiagRecordCreate(RecordBase):
    diag_id: int


class DiagRecord(RecordBase):
    diag_id: Diagnosis


class ReceptionBase(BaseModel):
    event_date: datetime
    note: Optional[str] = None


class ReceptionCreate(ReceptionBase):
    client_id: int
    procedures: List[ProcRecordCreate]
    diagnoses: List[DiagRecordCreate]


class Reception(ReceptionBase):
    id: int
    client_id: Client
    doctor_id: User
    procedures: List[ProcRecord]
    diagnoses: List[DiagRecord]

    class Config:
        orm_mode = True
