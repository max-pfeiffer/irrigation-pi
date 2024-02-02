"""Services for handling persistence of Schedule objects."""

from datetime import date, datetime, time, timedelta
from typing import Optional

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlmodel import Session

from app.database.config import database_engine
from app.database.models import Schedule
from app.repositories import ApSchedulerRepository, ScheduleRepository
from app.scheduling import Repeat


def calculate_stop_time(start_time: time, duration: int) -> time:
    """Calculate the stop time based on duration.

    :param start_time:
    :param duration:
    :return:
    """
    stop_date_time: datetime = datetime.combine(
        date.today(), start_time, tzinfo=start_time.tzinfo
    ) + timedelta(minutes=duration)
    stop_time: time = stop_date_time.timetz()
    return stop_time


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


def service_create_schedule(
    scheduler: AsyncIOScheduler,
    start_time: time,
    repeat: Repeat,
    duration: int,
    active: bool,
    relay_position: int,
) -> int:
    """Services creates and persists a Schedule object.

    :param AsyncIOScheduler scheduler:
    :return:
    """
    with Session(database_engine) as database_session, database_session.begin():
        stop_time: time = calculate_stop_time(start_time, duration)

        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        start_job_id, stop_job_id = ap_repo.create(
            start_time, stop_time, repeat, relay_position
        )

        data: dict = {
            "start_time": start_time,
            "stop_time": stop_time,
            "repeat": repeat,
            "duration": duration,
            "relay_position": relay_position,
            "active": active,
            "start_job_id": start_job_id,
            "stop_job_id": stop_job_id,
        }

        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedule: Schedule = repo.create(**data)
        primary_key: int = schedule.id

    return primary_key


def service_update_schedule(
    scheduler: AsyncIOScheduler,
    primary_key: int,
    start_time: Optional[time] = None,
    repeat: Optional[Repeat] = None,
    duration: Optional[int] = None,
    active: Optional[bool] = None,
    relay_position: Optional[int] = None,
):
    """Service updates and persists a Schedule object.

    :param AsyncIOScheduler scheduler:
    :param int primary_key:
    :param time start_time:
    :param Repeat repeat:
    :param int duration:
    :param bool active:
    :param int relay_position:
    :return:
    """
    with Session(database_engine) as database_session, database_session.begin():
        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedule: Schedule = repo.get(primary_key)

        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)

        # todo: find a better solution for this
        if active is None:
            active = schedule.active

        if relay_position is None:
            relay_position = schedule.relay_position

        data: dict = {
            "active": active,
            "relay_position": relay_position,
        }

        if active:
            if start_time and repeat and duration:
                stop_time: time = calculate_stop_time(start_time, duration)
                new_start_job_id, new_stop_job_id = ap_repo.update(
                    start_time,
                    stop_time,
                    repeat,
                    relay_position,
                    schedule.start_job_id,
                    schedule.stop_job_id,
                )
                data["start_time"] = start_time
                data["stop_time"] = stop_time
                data["duration"] = duration
                data["repeat"] = repeat
                data["start_job_id"] = new_start_job_id
                data["stop_job_id"] = new_stop_job_id
            elif start_time is not None:
                "todo: handle error"
        else:
            if schedule.start_job_id:
                ap_repo.delete(schedule.start_job_id)
            if schedule.stop_job_id:
                ap_repo.delete(schedule.stop_job_id)
            data["start_job_id"] = None
            data["stop_job_id"] = None

        repo.update(primary_key, **data)


def service_delete_schedule(scheduler: AsyncIOScheduler, primary_key: int):
    """Service deletes a persisted Schedule object.

    :param AsyncIOScheduler scheduler:
    :param int primary_key:
    :return:
    """
    with Session(database_engine) as database_session, database_session.begin():
        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedule: Schedule = repo.get(primary_key)

        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        ap_repo.delete(schedule.start_job_id)
        ap_repo.delete(schedule.stop_job_id)

        repo.delete(primary_key)
