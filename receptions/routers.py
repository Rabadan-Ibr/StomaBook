from fastapi import APIRouter, Depends, HTTPException
import receptions.schemas as sch
from cruds import get_by_id, get_list, create_item, edit_item
from receptions.models import DiagnosisDB, ProcedureDB, ClientDB, ToothDB
from exeptions import NotFoundException

reception_router = APIRouter(tags=['reception'])


@reception_router.get('/diagnoses/', response_model=list[sch.DiagnosisDTO])
def read_diagnoses():
    return get_list(DiagnosisDB)


@reception_router.get(
    '/diagnoses/{diag_id}', response_model=sch.DiagnosisDTO
)
def read_diagnosis(diag_id: int):
    try:
        result = get_by_id(diag_id, DiagnosisDB)
    except NotFoundException as err:
        raise HTTPException(status_code=404, detail=str(err))
    return result


@reception_router.post('/diagnoses/', response_model=sch.DiagnosisDTO)
def create_diagnosis(diag_schem: sch.DiagnosisCreateSchem):
    return create_item(diag_schem, DiagnosisDB)


@reception_router.put(
    '/diagnoses/{diag_id}', response_model=sch.DiagnosisDTO
)
def change_diagnosis(diag_id: int, diag_schem: sch.DiagnosisCreateSchem):
    return edit_item(diag_id, diag_schem, DiagnosisDB)


@reception_router.get('/procedures/', response_model=list[sch.ProcedureDTO])
def read_procedures():
    return get_list(ProcedureDB)


@reception_router.get(
    '/procedures/{proc_id}', response_model=sch.ProcedureDTO
)
def read_procedure(proc_id: int):
    try:
        result = get_by_id(proc_id, ProcedureDB)
    except NotFoundException as err:
        raise HTTPException(status_code=404, detail=str(err))
    return result


@reception_router.post('/procedures/', response_model=sch.ProcedureDTO)
def create_procedure(proc_schem: sch.ProcedureCreateSchem):
    return create_item(proc_schem, ProcedureDB)


@reception_router.put(
    '/procedures/{proc_id}', response_model=sch.ProcedureDTO
)
def change_procedure(proc_id: int, proc_schem: sch.ProcedureCreateSchem):
    return edit_item(proc_id, proc_schem, ProcedureDB)


@reception_router.get('/teeth/', response_model=list[sch.ToothDTO])
def read_teeth():
    return get_list(ToothDB)


@reception_router.get('/teeth/{tooth_id}', response_model=sch.ToothDTO)
def read_tooth(tooth_id: int):
    try:
        result = get_by_id(tooth_id, ToothDB)
    except NotFoundException as err:
        raise HTTPException(status_code=404, detail=str(err))
    return result


@reception_router.post('/teeth/', response_model=sch.ToothDTO)
def create_tooth(tooth_schem: sch.ToothCreateSchem):
    return create_item(tooth_schem, ToothDB)


@reception_router.put(
    '/teeth/{tooth_id}', response_model=sch.ToothDTO
)
def change_tooth(
        tooth_id: int,
        tooth_schem: sch.ToothCreateSchem
):
    return edit_item(tooth_id, tooth_schem, ToothDB)


@reception_router.get('/clients/', response_model=list[sch.ClientDTO])
def read_clients():
    return get_list(ClientDB)


@reception_router.get('/clients/{client_id}', response_model=sch.ClientDTO)
def read_client(client_id: int):
    try:
        result = get_by_id(client_id, ClientDB)
    except NotFoundException as err:
        raise HTTPException(status_code=404, detail=str(err))
    return result


@reception_router.post('/clients/', response_model=sch.ClientDTO)
def create_client(client_schem:sch.ClientCreateSchem):
    return create_item(client_schem, ClientDB)


@reception_router.put(
    '/clients/{client_id}', response_model=sch.ClientDTO
)
def change_client(
        client_id: int,
        client_schem: sch.ClientCreateSchem
):
    try:
        result = edit_item(client_id, client_schem, ClientDB)
    except NotFoundException as err:
        raise HTTPException(status_code=404, detail=str(err))
    return result
