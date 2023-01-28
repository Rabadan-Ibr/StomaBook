from fastapi import FastAPI, APIRouter
from receptions.routers import receptions_router


v1 = APIRouter(prefix='/api/v1')
v1.include_router(receptions_router)

app = FastAPI(title='StomaBook', description='Книга учета пациентов.')
app.include_router(v1)
