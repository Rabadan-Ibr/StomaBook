from ..tables import ReceptionDB
from .base_service import CRUDMixin, MainMixin


class ReceptionsService(MainMixin, CRUDMixin):
    _table = ReceptionDB
