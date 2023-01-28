from fastapi import APIRouter
from .procedures import procedure_router

receptions_router = APIRouter()
receptions_router.include_router(procedure_router)
