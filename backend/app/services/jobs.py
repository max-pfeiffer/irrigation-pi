"""Services for APScheduler jobs."""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlmodel import Session

from app.database.config import database_engine
from app.database.models import Schedule
from app.repositories import ApSchedulerRepository, ScheduleRepository


def service_recreate_jobs(scheduler: AsyncIOScheduler):
    """Recreates all jobs for ApScheduler.

    :param scheduler:
    :return:
    """
    with Session(database_engine) as database_session, database_session.begin():
        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        repo: ScheduleRepository = ScheduleRepository(database_session)
        schedules: list[Schedule] = repo.query(active=True)

        for schedule in schedules:
            start_job_id, stop_job_id = ap_repo.create(
                schedule.start_time,
                schedule.stop_time,
                schedule.repeat,
                schedule.relay_position,
            )
            repo.update(schedule.id, start_job_id=start_job_id, stop_job_id=stop_job_id)
