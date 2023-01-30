from fastapi import APIRouter

from .users import user_router


users_route = APIRouter()
users_route.include_router(user_router)