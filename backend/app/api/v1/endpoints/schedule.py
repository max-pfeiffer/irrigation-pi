"""API endpoints for Schedule objects."""
from fastapi import APIRouter

from app.api.v1.models import ScheduleCreate, ScheduleResponse, ScheduleUpdate
from app.services.schedule import (
    service_create_schedule,
    service_delete_schedule,
    service_get_schedule,
    service_get_schedules,
    service_update_schedule,
)

router = APIRouter()


@router.get("/{primary_key}")
def get_schedule(primary_key: int) -> ScheduleResponse:
    """Get Schedule."""
    return service_get_schedule(primary_key)


@router.get("/")
def get_schedules() -> list[ScheduleResponse]:
    """Get Schedules."""
    return service_get_schedules()


@router.post("/")
def create_schedule(schedule_data: ScheduleCreate) -> int:
    """Create Schedule."""
    return service_create_schedule(schedule_data)


@router.put("/")
def update_schedule(schedule_data: ScheduleUpdate):
    """Update Schedule."""
    return service_update_schedule(schedule_data)


@router.delete("/{primary_key}")
def delete_schedule(primary_key: int):
    """Delete Schedule."""
    return service_delete_schedule(primary_key)
