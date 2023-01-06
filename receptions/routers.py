from dependency import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
import receptions.schemas as sch
from cruds import get_by_id, get_list, create_item, change_item
from receptions.models import Diagnosis, Procedure, Tooth, Client


reception_router = APIRouter(tags=['reception'])


@reception_router.get('/diagnoses/', response_model=list[sch.DiagnosisSchem])
def read_diagnoses(db: Session = Depends(get_db)):
    return get_list(db, Diagnosis)


@reception_router.get(
    '/diagnoses/{diag_id}', response_model=sch.DiagnosisSchem
)
def read_diagnosis(diag_id: int, db: Session = Depends(get_db)):
    return get_by_id(db, diag_id, Diagnosis)


@reception_router.post('/diagnoses/', response_model=sch.DiagnosisSchem)
def create_diagnosis(
        diag_schem: sch.DiagnosisCreateSchem, db: Session = Depends(get_db)
):
    return create_item(db, diag_schem, Diagnosis)


@reception_router.put(
    '/diagnoses/{diag_id}', response_model=sch.DiagnosisSchem
)
def change_diagnosis(
        diag_id: int,
        diag_schem: sch.DiagnosisCreateSchem,
        db: Session = Depends(get_db)
):
    return change_item(db, diag_id, diag_schem, Diagnosis)


@reception_router.get('/procedures/', response_model=list[sch.ProcedureSchem])
def read_procedures(db: Session = Depends(get_db)):
    return get_list(db, Procedure)


@reception_router.get(
    '/procedures/{proc_id}', response_model=sch.ProcedureSchem
)
def read_procedure(proc_id: int, db: Session = Depends(get_db)):
    return get_by_id(db, proc_id, Procedure)


@reception_router.post('/procedures/', response_model=sch.ProcedureSchem)
def create_procedure(
        proc_schem: sch.ProcedureCreateSchem, db: Session = Depends(get_db)
):
    return create_item(db, proc_schem, Procedure)


@reception_router.put(
    '/procedures/{proc_id}', response_model=sch.ProcedureSchem
)
def change_procedure(
        proc_id: int,
        proc_schem: sch.ProcedureCreateSchem,
        db: Session = Depends(get_db)
):
    return change_item(db, proc_id, proc_schem, Procedure)


@reception_router.get('/teeth/', response_model=list[sch.ToothSchem])
def read_teeth(db: Session = Depends(get_db)):
    return get_list(db, Tooth)


@reception_router.get('/teeth/{tooth_id}', response_model=sch.ToothSchem)
def read_tooth(tooth_id: int, db: Session = Depends(get_db)):
    return get_by_id(db, tooth_id, Tooth)


@reception_router.post('/teeth/', response_model=sch.ToothSchem)
def create_tooth(
        tooth_schem: sch.ToothCreateSchem, db: Session = Depends(get_db)
):
    return create_item(db, tooth_schem, Tooth)


@reception_router.put(
    '/teeth/{tooth_id}', response_model=sch.ToothSchem
)
def change_tooth(
        tooth_id: int,
        tooth_schem: sch.ToothCreateSchem,
        db: Session = Depends(get_db)
):
    return change_item(db, tooth_id, tooth_schem, Tooth)


@reception_router.get('/clients/', response_model=list[sch.ClientSchem])
def read_clients(db: Session = Depends(get_db)):
    return get_list(db, Client)


@reception_router.get('/clients/{client_id}', response_model=sch.ClientSchem)
def read_client(client_id: int, db: Session = Depends(get_db)):
    return get_by_id(db, client_id, Client)


@reception_router.post('/clients/', response_model=sch.ClientSchem)
def create_client(
        client_schem:sch.ClientCreateSchem, db: Session = Depends(get_db)
):
    return create_item(db, client_schem, Client)


@reception_router.put(
    '/clients/{client_id}', response_model=sch.ClientSchem
)
def change_client(
        client_id: int,
        client_schem: sch.ClientCreateSchem,
        db: Session = Depends(get_db)
):
    return change_item(db, client_id, client_schem, Client)
