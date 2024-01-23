"""Services for handling persistence of Schedule objects."""
from app.api.v1.models import ScheduleCreate, ScheduleResponse, ScheduleUpdate


def service_get_schedule(primary_key: int) -> ScheduleResponse:
    """Service returns a Schedule object.

    :param int primary_key: Primary key
    :return ScheduleResponse:
    """
    pass


def service_get_schedules() -> list[ScheduleResponse]:
    """Service returns a list of Schedule objects.

    :return list[ScheduleResponse]:
    """
    pass


def service_create_schedule(data: ScheduleCreate):
    """Services creates and persists a Schedule object.

    :param ScheduleCreate data:
    :return:
    """
    pass


def service_update_schedule(data: ScheduleUpdate):
    """Service updates and persists a Schedule object.

    :param ScheduleUpdate data:
    :return:
    """
    pass


def service_delete_schedule(primary_key: int):
    """Service deletes a persisted Schedule object.

    :param int primary_key:
    :return:
    """
    pass
