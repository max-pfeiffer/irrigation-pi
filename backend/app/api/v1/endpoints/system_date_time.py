"""API endpoints for system date and time."""

from fastapi import APIRouter, Request

from app.api.v1.models import SystemDateTime
from app.services.system_date_time import (
    service_get_system_date_time,
    service_set_system_date_time,
)

router = APIRouter()


@router.get("/")
def get_system_date_time() -> SystemDateTime:
    """Get system date and time.

    :return:
    """
    return SystemDateTime(date_time=service_get_system_date_time())


@router.put(
    "/",
    responses={500: {"description": "Setting system date and time failed"}},
)
def set_system_date_time(request: Request, date_time_data: SystemDateTime) -> None:
    """Set system date and time.

    :param request:
    :param date_time_data:
    :return:
    """
    service_set_system_date_time(date_time_data.date_time, request.app.state.scheduler)
