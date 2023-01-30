from fastapi import APIRouter

from .diagnoses import diagnosis_router
from .procedures import procedure_router
from .clients import client_router
from .receptions import reception_router

receptions_router = APIRouter()
receptions_router.include_router(procedure_router)
receptions_router.include_router(diagnosis_router)
receptions_router.include_router(client_router)
receptions_router.include_router(reception_router)
