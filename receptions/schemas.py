from pydantic import BaseModel, validator

from dependency import get_db
from receptions.models import Procedure, Diagnosis


class DiagnosisBaseSchem(BaseModel):
    name: str
    detail: bool


class DiagnosisCreateSchem(DiagnosisBaseSchem):

    @validator('name')
    def name_must_unique(cls, v: str):
        db = next(get_db())
        name = v.title()
        db_item = db.query(Diagnosis).filter_by(name=name).first()
        if db_item is not None:
            raise ValueError('must be unique')
        return name


class DiagnosisSchem(DiagnosisBaseSchem):
    id: int

    class Config:
        orm_mode = True


class ProcedureBaseSchem(BaseModel):
    name: str
    detail: bool


class ProcedureCreateSchem(ProcedureBaseSchem):

    @validator('name')
    def name_must_unique(cls, v: str):
        db = next(get_db())
        name = v.title()
        db_item = db.query(Procedure).filter_by(name=name).first()
        if db_item is not None:
            raise ValueError('must be unique')
        return name


class ProcedureSchem(ProcedureBaseSchem):
    id: int

    class Config:
        orm_mode = True


class ToothBaseSchem(BaseModel):
    name: int


class ToothCreateSchem(ToothBaseSchem):

    @validator('name')
    def name_must_unique(cls, v: int):
        db = next(get_db())
        db_item = db.query(Procedure).filter_by(name=v).first()
        if db_item is not None:
            raise ValueError('must be unique')
        return v


class ToothSchem(ToothBaseSchem):
    id: int

    class Config:
        orm_mode = True


class ClientCreateSchem(BaseModel):
    first_name: str
    last_name: str
    phone: int
    email: str = None
    note: str = None


class ClientSchem(ClientCreateSchem):
    id: int

    class Config:
        orm_mode = True
