from fastapi import APIRouter

from app.api.api_v1.endpoints import rhtime, kubeburner


api_router = APIRouter()
api_router.include_router(rhtime.router, tags=["rhtime"])
api_router.include_router(kubeburner.router, prefix="/kubeburner", tags=["kubeburner"])