from typing import List

from fastapi import HTTPException, Depends
from starlette import status

from src.db import SessionLocal, get_session


class BaseService:
    _table = None
    _create_model = None


    def __init__(self, session: SessionLocal = Depends(get_session)):
        self._session = session
        if self._table is None:
            raise ValueError('Необходимо задать аргумент _table.')
        if self._create_model is None:
            raise ValueError('Необходимо задать аргумент _create_model.')


    def _get_by_id(self, item_id: int) -> _table:
        item = self._session.get(self._table, item_id)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return item

    def get_list(self) -> List[_table]:
        items = self._session.query(self._table).all()
        return items

    def get_by_id(self, item_id: int) -> _table:
        return self._get_by_id(item_id)

    def create(self, item_data: _create_model) -> _table:
        item = self._table(**item_data.dict())
        self._session.add(item)
        self._session.commit()
        self._session.refresh(item)
        return item

    def edit(self, item_id: int, item_data: _create_model) -> _table:
        item = self._get_by_id(item_id)
        for key, value in item_data:
            setattr(item, key, value)
        self._session.commit()
        self._session.refresh(item)
        return item

    def delete(self, item_id: int):
        item = self._get_by_id(item_id)
        self._session.delete(item)
        self._session.commit()
