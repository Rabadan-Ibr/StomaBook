from ..tables import ClientDB
from .base_service import CRUDMixin, MainMixin


class ClientsService(MainMixin, CRUDMixin):
    _table = ClientDB
