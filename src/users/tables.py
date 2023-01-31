from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.db import Base


class UserDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    phone = Column(Integer, unique=True, nullable=False)
    role = Column(String, default='doc')

    receptions = relationship('ReceptionDB', backref='doctor')
