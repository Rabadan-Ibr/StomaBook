from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType, EmailType

from config import Base, ROLES


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(EmailType, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    phone = Column(Integer, unique=True, nullable=False)
    role = Column(ChoiceType(ROLES))

    receptions = relationship('Reception', backref='user')
