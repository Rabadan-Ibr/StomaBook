from fastapi import APIRouter

from .diagnoses import diagnosis_router
from .procedures import procedure_router

receptions_router = APIRouter()
receptions_router.include_router(procedure_router)
receptions_router.include_router(diagnosis_router)
