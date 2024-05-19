"""API endpoints for Schedule objects."""

from fastapi import APIRouter, Depends, Request
from sqlmodel import Session

from app.api.v1.models import ScheduleCreate, ScheduleResponse, ScheduleUpdate
from app.database.config import get_session
from app.services.schedule import (
    service_create_schedule,
    service_delete_schedule,
    service_get_schedule,
    service_get_schedules,
    service_update_schedule,
)

router = APIRouter()


@router.get("/{primary_key}")
def get_schedule(
    primary_key: int, database_session: Session = Depends(get_session)
) -> ScheduleResponse:
    """Get Schedule."""
    data: dict = service_get_schedule(database_session, primary_key)
    response: ScheduleResponse = ScheduleResponse(**data)
    return response


@router.get("/")
def get_schedules(
    database_session: Session = Depends(get_session),
) -> list[ScheduleResponse]:
    """Get Schedules."""
    data: list[dict] = service_get_schedules(database_session)
    response: list[ScheduleResponse] = [ScheduleResponse(**item) for item in data]
    return response


@router.post("/", responses={409: {"description": "An active schedule already exists"}})
def create_schedule(
    request: Request,
    schedule_data: ScheduleCreate,
    database_session: Session = Depends(get_session),
) -> int:
    """Create Schedule."""
    primary_key: int = service_create_schedule(
        database_session, request.app.state.scheduler, **schedule_data.model_dump()
    )
    return primary_key


@router.put(
    "/{primary_key}",
    responses={409: {"description": "An active schedule already exists"}},
)
def update_schedule(
    request: Request,
    primary_key: int,
    schedule_data: ScheduleUpdate,
    database_session: Session = Depends(get_session),
):
    """Update Schedule."""
    service_update_schedule(
        database_session,
        request.app.state.scheduler,
        primary_key,
        **schedule_data.model_dump(exclude_defaults=True),
    )


@router.delete("/{primary_key}")
def delete_schedule(
    request: Request, primary_key: int, database_session: Session = Depends(get_session)
):
    """Delete Schedule."""
    service_delete_schedule(database_session, request.app.state.scheduler, primary_key)
