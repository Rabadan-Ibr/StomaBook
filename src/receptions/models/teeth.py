from pydantic import BaseModel


class ToothBase(BaseModel):
    name: int


class ToothCreate(ToothBase):
    pass


class Tooth(ToothBase):
    id: int

    class Config:
        orm_mode = True