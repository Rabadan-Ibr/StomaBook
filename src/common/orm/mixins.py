from typing import List

from sqlalchemy import select

from src.db import Base


class BaseMixins:
    _table: Base


class ListMixin(BaseMixins):

    def _get_list(self) -> List["ListMixin._table"]:
        items = self._session.query(self._table).all()
        return items


class RetrieveMixin(BaseMixins):

    def _get_item(self, item_id: int) -> 'RetrieveMixin._table':
        return self._session.get(self._table, item_id)

    def _get_by_field(self, field: str, value: str):
        stmt = select(self._table).where(getattr(self._table, field) == value)
        return self._session.scalar(stmt)


class CreateMixin(BaseMixins):

    def _create_item(self, item_data: dict) -> 'CreateMixin._table':
        item = self._table(**item_data)
        self._session.add(item)
        self._session.commit()
        self._session.refresh(item)
        return item


class DeleteMixin(BaseMixins):

    def _delete_item(self, item: Base):
        self._session.delete(item)
        self._session.commit()


class UpdateMixin(BaseMixins):

    def _edit_item(self, item: Base, item_data: dict) -> 'UpdateMixin._table':
        for key, value in item_data.items():
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
