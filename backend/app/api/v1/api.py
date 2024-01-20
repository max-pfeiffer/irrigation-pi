from fastapi import APIRouter

from app.api.v1.endpoints import schedules

api_router = APIRouter()
api_router.include_router(schedules.router, prefix="/schedules", tags=["schedules"])
