from pydantic import BaseModel


class ProcedureBase(BaseModel):
    name: str
    detail: bool


class ProcedureCreate(ProcedureBase):
    pass


class Procedure(ProcedureBase):
    id: int

    class Config:
        orm_mode = True

