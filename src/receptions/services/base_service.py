from typing import List

from fastapi import Depends, HTTPException
from starlette import status

from src.db import Base, SessionLocal, get_session


class BaseService:
    _table: Base = None

class MainMixin(BaseService):
    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session
        if self._table is None:
            raise ValueError('Необходимо задать аргумент _table.')

    def _get_by_id(self, item_id: int) -> "MainMixin._table":
        item = self._session.get(self._table, item_id)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return item


class ListMixin(BaseService):

    def get_list(self) -> List["ListMixin._table"]:
        items = self._session.query(self._table).all()
        return items


class RetrieveMixin(BaseService):

    def get_item(self, item_id: int) -> 'RetrieveMixin._table':
        return self._get_by_id(item_id)


class CreateMixin(BaseService):

    def create_item(self, item_data: dict) -> 'CreateMixin._table':
        item = self._table(**item_data)
        self._session.add(item)
        self._session.commit()
        self._session.refresh(item)
        return item


class DeleteMixin(BaseService):

    def delete_item(self, item_id: int):
        item = self._get_by_id(item_id)
        self._session.delete(item)
        self._session.commit()


class UpdateMixin(BaseService):

    def edit_item(self, item_id: int, item_data: dict) -> 'UpdateMixin._table':
        item = self._get_by_id(item_id)
        for key, value in item_data:
            setattr(item, key, value)
        self._session.commit()
        self._session.refresh(item)
        return item


class ReadOnlyMixin(RetrieveMixin, ListMixin):
    pass


class WriteOnlyMixin(CreateMixin, UpdateMixin):
    pass


class CRUDMixin(ReadOnlyMixin, WriteOnlyMixin, DeleteMixin):
    pass
