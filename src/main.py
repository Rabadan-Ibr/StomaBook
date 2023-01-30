from fastapi import APIRouter, FastAPI

from receptions.routers import receptions_router
from users.routers import users_route

v1 = APIRouter(prefix='/api/v1')
v1.include_router(receptions_router)
v1.include_router(users_route)

app = FastAPI(title='StomaBook', description='Книга учета пациентов.')
app.include_router(v1)
