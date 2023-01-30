from fastapi import Depends

from db import SessionLocal, get_session
from ..tables import ReceptionDB
from common.orm.mixins import CRUDMixin


class ReceptionsService(CRUDMixin):
    _table = ReceptionDB

    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session
