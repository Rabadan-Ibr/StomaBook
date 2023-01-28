from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db import Base


class ClientDB(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    email = Column(String)
    note = Column(String)

    receptions = relationship('ReceptionDB', backref='client')


class ToothDB(Base):
    __tablename__ = 'teeth'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    diagnoses = relationship('DiagReceptionDB', backref='tooth')
    procedures = relationship('ProcReceptionDB', backref='tooth')


class DiagnosisDB(Base):
    __tablename__ = 'diagnoses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    detail = Column(Boolean, default=True)

    def __str__(self):
        return self.__tablename__


class ProcedureDB(Base):
    __tablename__ = 'procedures'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    detail = Column(Boolean, default=True)


class DiagReceptionDB(Base):
    __tablename__ = 'diag_reception'

    id = Column(Integer, primary_key=True, index=True)
    diag_id = Column(ForeignKey('diagnoses.id'), nullable=False)
    reception_id = Column(ForeignKey('receptions.id'), nullable=False)
    tooth_id = Column(ForeignKey('teeth.id'))
    note = Column(String)


class ProcReceptionDB(Base):
    __tablename__ = 'proc_reception'

    id = Column(Integer, primary_key=True, index=True)
    proc_id = Column(ForeignKey('procedures.id'), nullable=False)
    reception_id = Column(ForeignKey('receptions.id'), nullable=False)
    tooth_id = Column(ForeignKey('teeth.id'))
    note = Column(String)


class ReceptionDB(Base):
    __tablename__ = 'receptions'

    id = Column(Integer, primary_key=True, index=True)
    event_date = Column(DateTime, default=func.now())
    note = Column(String)
    doctor_id = Column(ForeignKey('users.id'), nullable=False)
    client_id = Column(ForeignKey('clients.id'), nullable=False)

    diagnoses = relationship('DiagReceptionDB', backref='reception')
    procedures = relationship('ProcReceptionDB', backref='reception')

