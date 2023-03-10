from typing import Optional

from pydantic import BaseModel


class ClientBase(BaseModel):
    first_name: str
    last_name: str
    phone: int
    email: Optional[str] = None
    note: Optional[str] = None


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True
