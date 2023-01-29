from typing import Optional

from pydantic import BaseModel
from datetime import datetime
from .clients import Client
from src.users.models.users import User


class ReceptionBase(BaseModel):
    event_date: datetime
    note: Optional[str] = None


class ReceptionCreate(ReceptionBase):
    client_id: int


class Reception(ReceptionBase):
    id: int
    client_id: Client
    doctor_id: User

    class Config:
        orm_mode = True
