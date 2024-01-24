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
    data: dict = service_get_schedule(primary_key)
    response: ScheduleResponse = ScheduleResponse(**data)
    return response


@router.get("/")
def get_schedules() -> list[ScheduleResponse]:
    """Get Schedules."""
    data: list[dict] = service_get_schedules()
    response: list[ScheduleResponse] = [ScheduleResponse(**item) for item in data]
    return response


@router.post("/")
def create_schedule(schedule_data: ScheduleCreate) -> int:
    """Create Schedule."""
    primary_key: int = service_create_schedule(**schedule_data.model_dump())
    return primary_key


@router.put("/{primary_key}")
def update_schedule(primary_key: int, schedule_data: ScheduleUpdate):
    """Update Schedule."""
    service_update_schedule(
        primary_key=primary_key, **schedule_data.model_dump(exclude_defaults=True)
    )


@router.delete("/{primary_key}")
def delete_schedule(primary_key: int):
    """Delete Schedule."""
    service_delete_schedule(primary_key)
