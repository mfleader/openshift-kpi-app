from fastapi import APIRouter

from app.api.api_v1.endpoints import rhtime

api_router = APIRouter()
api_router.include_router(rhtime.router, tags=["rhtime"])