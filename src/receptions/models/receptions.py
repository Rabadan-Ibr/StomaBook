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
    procedure: Procedure

    class Config:
        orm_mode = True


class DiagRecordCreate(RecordBase):
    diag_id: int


class DiagRecord(RecordBase):
    diagnosis: Diagnosis

    class Config:
        orm_mode = True


class ReceptionBase(BaseModel):
    event_date: Optional[datetime] = None
    note: Optional[str] = None


class ReceptionCreate(ReceptionBase):
    client_id: int
    procedures: Optional[List[ProcRecordCreate]] = None
    diagnoses: Optional[List[DiagRecordCreate]] = None


class ReceptionCreateDB(ReceptionBase):
    client_id: int
    doctor_id: int


class ReceptionEditDB(ReceptionBase):
    client_id: int


class Reception(ReceptionBase):
    id: int
    client: Client
    doctor: User
    procedures: Optional[List[ProcRecord]] = None
    diagnoses: Optional[List[DiagRecord]] = None

    class Config:
        orm_mode = True
