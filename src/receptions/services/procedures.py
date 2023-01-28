from ..tables import ProcedureDB
from .base_service import CRUDMixin, MainMixin


class ProceduresService(MainMixin, CRUDMixin):
    _table = ProcedureDB
