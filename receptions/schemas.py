from pydantic import BaseModel


class DiagnosisBaseSchem(BaseModel):
    name: str
    detail: bool


class DiagnosisCreateSchem(DiagnosisBaseSchem):
    pass


class DiagnosisDTO(DiagnosisBaseSchem):
    id: int

    class Config:
        orm_mode = True


class ProcedureBaseSchem(BaseModel):
    name: str
    detail: bool


class ProcedureCreateSchem(ProcedureBaseSchem):
    pass


class ProcedureDTO(ProcedureBaseSchem):
    id: int

    class Config:
        orm_mode = True


class ToothBaseSchem(BaseModel):
    name: int


class ToothCreateSchem(ToothBaseSchem):
    pass


class ToothDTO(ToothBaseSchem):
    id: int

    class Config:
        orm_mode = True


class ClientCreateSchem(BaseModel):
    first_name: str
    last_name: str
    phone: int
    email: str = None
    note: str = None


class ClientDTO(ClientCreateSchem):
    id: int

    class Config:
        orm_mode = True
