"""Services for handling persistence of Schedule objects."""
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlmodel import Session

from app.database.config import database_engine
from app.database.models import Schedule
from app.repositories import ApSchedulerRepository, ScheduleRepository


def service_get_schedule(primary_key: int) -> dict:
    """Service returns a Schedule object.

    :param int primary_key: Primary key
    :return ScheduleResponse:
    """
    with Session(database_engine) as database_session, database_session.begin():
        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedule: Schedule = repo.get(primary_key)
        data: dict = schedule.model_dump()

    return data


def service_get_schedules() -> list[dict]:
    """Service returns a list of Schedule objects.

    :return list[ScheduleResponse]:
    """
    with Session(database_engine) as database_session, database_session.begin():
        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedules: list[Schedule] = repo.query()
        data: list[dict] = [item.model_dump() for item in schedules]

    return data


def service_create_schedule(scheduler: AsyncIOScheduler, **kwargs) -> int:
    """Services creates and persists a Schedule object.

    :param AsyncIOScheduler scheduler:
    :return:
    """
    with Session(database_engine) as database_session, database_session.begin():
        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedule: Schedule = repo.create(**kwargs)

        primary_key: int = schedule.id
        data: dict = schedule.model_dump()

        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        return_data: dict = ap_repo.create(data)

        repo.update(
            primary_key=primary_key,
            start_schedule_id=return_data["start_schedule_id"],
            stop_schedule_id=return_data["stop_schedule_id"],
        )

    return primary_key


def service_update_schedule(scheduler: AsyncIOScheduler, **kwargs):
    """Service updates and persists a Schedule object.

    :param AsyncIOScheduler scheduler:
    :return:
    """
    with Session(database_engine) as database_session, database_session.begin():
        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedule: Schedule = repo.update(**kwargs)

        data: dict = schedule.model_dump()

        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        return_data: dict = ap_repo.update(data)

        repo.update(
            primary_key=schedule.id,
            start_schedule_id=return_data["start_schedule_id"],
            stop_schedule_id=return_data["stop_schedule_id"],
        )


def service_delete_schedule(scheduler: AsyncIOScheduler, primary_key: int):
    """Service deletes a persisted Schedule object.

    :param AsyncIOScheduler scheduler:
    :param int primary_key:
    :return:
    """
    with Session(database_engine) as database_session, database_session.begin():
        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedule: Schedule = repo.get(primary_key)

        data: dict = schedule.model_dump()

        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        ap_repo.delete(data)

        repo.delete(primary_key)
