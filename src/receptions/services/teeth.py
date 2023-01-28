from ..tables import ToothDB
from .base_service import CRUDMixin, MainMixin


class TeethService(MainMixin, CRUDMixin):
    _table = ToothDB