from ..tables import DiagnosisDB
from .base_service import CRUDMixin, MainMixin


class DiagnosesService(MainMixin, CRUDMixin):
    _table = DiagnosisDB
