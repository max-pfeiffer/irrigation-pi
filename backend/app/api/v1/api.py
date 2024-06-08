"""API routers for API version 1.0."""

from fastapi import APIRouter

from app.api.v1.endpoints import info, relay, schedule

api_router = APIRouter()
api_router.include_router(schedule.router, prefix="/schedule", tags=["Schedule"])
api_router.include_router(relay.router, prefix="/relay", tags=["Relay"])
api_router.include_router(
    info.router, prefix="/info", tags=["Raspberry Pi Board Information"]
)
