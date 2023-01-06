from fastapi import HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from config import Base


def get_by_id(db: Session, item_id: int, model: Base):
    item = db.get(model, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail='Object not found.')
    return item


def get_list(db: Session, model: Base):
    return db.query(model).all()


def create_item(db: Session, scheme: BaseModel, model: Base):
    db_item = model(**scheme.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def change_item(db: Session, item_id: int, scheme: BaseModel, model: Base):
    db_item = get_by_id(db, item_id, model)
    for key, value in scheme:
        setattr(db_item, key, value)
    db.commit()
    return db_item
