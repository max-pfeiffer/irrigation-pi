"""Services for handling persistence of Schedule objects."""

from datetime import date, datetime, time, timedelta, timezone

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlmodel import Session

from app.database.config import database_engine
from app.database.models import Schedule
from app.repositories import ApSchedulerRepository, ScheduleRepository
from app.scheduling import Repeat


def set_system_timezone(time_input: time):
    """Create new time object from input with system timezone.

    :param time_input:
    :return:
    """
    system_timezone: timezone = datetime.now(timezone.utc).astimezone().tzinfo
    time_output = time(
        hour=time_input.hour, minute=time_input.minute, tzinfo=system_timezone
    )
    return time_output


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
    :param time start_time:
    :param Repeat repeat:
    :param int duration:
    :param bool active:
    :param int relay_position:
    :return:
    """
    with Session(database_engine) as database_session, database_session.begin():
        start_time = set_system_timezone(start_time)
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


def service_update_schedule(scheduler: AsyncIOScheduler, primary_key: int, **kwargs):
    """Service updates and persists a Schedule object.

    :param AsyncIOScheduler scheduler:
    :param int primary_key:
    :param kwargs:
    :return:
    """
    with Session(database_engine) as database_session, database_session.begin():
        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedule: Schedule = repo.get(primary_key)

        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        for job_id in [schedule.start_job_id, schedule.stop_job_id]:
            if ap_repo.exists(job_id):
                ap_repo.delete(job_id)

        data: dict = schedule.model_dump()
        for key, value in kwargs.items():
            if value is not None:
                data[key] = value

        data["start_time"] = set_system_timezone(data["start_time"])

        if data["active"]:
            stop_time: time = calculate_stop_time(data["start_time"], data["duration"])
            start_job_id, stop_job_id = ap_repo.create(
                start_time=data["start_time"],
                stop_time=stop_time,
                repeat=data["repeat"],
                relay_position=data["relay_position"],
            )
            data["stop_time"] = stop_time
            data["start_job_id"] = start_job_id
            data["stop_job_id"] = stop_job_id
        else:
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

        if schedule.active:
            ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
            ap_repo.delete(schedule.start_job_id)
            ap_repo.delete(schedule.stop_job_id)

        repo.delete(primary_key)
