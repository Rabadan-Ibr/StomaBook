from fastapi import FastAPI, APIRouter
from receptions.routers import reception_router
from users.routers import user_router


v1 = APIRouter(prefix='/api/v1')
v1.include_router(reception_router)
v1.include_router(user_router)

app = FastAPI(title='StomaBook', docs_url='/docs')
app.include_router(v1)
