from fastapi import APIRouter

from .users import user_router
from .auth import auth_router


users_route = APIRouter()
users_route.include_router(user_router)
users_route.include_router(auth_router)
