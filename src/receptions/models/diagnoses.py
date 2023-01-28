from pydantic import BaseModel


class DiagnosisBase(BaseModel):
    name: str
    detail: bool


class DiagnosisCreate(DiagnosisBase):
    pass


class Diagnosis(DiagnosisBase):
    id: int

    class Config:
        orm_mode = True
