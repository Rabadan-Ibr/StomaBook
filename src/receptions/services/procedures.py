from .base_service import BaseService
from ..tables import ProcedureDB
from ..models.procedures import ProcedureCreate


class ProceduresService(BaseService):
    _table = ProcedureDB
    _create_model = ProcedureCreate
