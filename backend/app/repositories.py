"""Repositories for data persistence."""

from datetime import time
from typing import Optional

from apscheduler.job import Job
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlmodel import Session, select

from app.database.models import Schedule
from app.scheduling import Repeat, task_switch_relay


class ScheduleRepository:
    """Repository for persisting Schedule objects."""

    def __init__(self, session: Session) -> None:
        """Initialize object.

        :param Session session:
        """
        self.session: Session = session

    def get(self, primary_key: int) -> Schedule:
        """Get one schedule by primary_key.

        :param int primary_key:
        :return:
        """
        schedule: Schedule = self.session.get_one(Schedule, primary_key)
        return schedule

    def query(self, **kwargs) -> list[Schedule]:
        """Query for Schedule objects.

        :param kwargs:
        :return:
        """
        statement = select(Schedule)
        for key, value in kwargs.items():
            statement = statement.where(getattr(Schedule, key) == value)

        result = self.session.scalars(statement).all()
        return result

    def create(self, **kwargs) -> Schedule:
        """Create a new Schedule object.

        :param kwargs:
        :return Schedule:
        """
        schedule: Schedule = Schedule(**kwargs)
        self.session.add(schedule)
        # Don't commit just flush the session in order to leverage sqlalchemy's
        # unit of work feature/pattern.
        # https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#flushing
        self.session.flush()
        return schedule

    def update(self, primary_key: int, **kwargs) -> Schedule:
        """Update a Schedule object.

        :param int primary_key:
        :param kwargs:
        :return:
        """
        schedule: Schedule = self.get(primary_key)

        for key, value in kwargs.items():
            setattr(schedule, key, value)

        self.session.flush()
        return schedule

    def delete(self, primary_key: int):
        """Delete a schedule by primary_key.

        :param int primary_key:
        :return:
        """
        schedule: Schedule = self.get(primary_key)
        self.session.delete(schedule)
        self.session.flush()


class ApSchedulerRepository:
    """Repository for interfacing with ApScheduler library."""

    def __init__(self, scheduler: AsyncIOScheduler) -> None:
        """Initialize object.

        :param AsyncScheduler scheduler:
        """
        self.scheduler: AsyncIOScheduler = scheduler

    def _create_trigger_data(
        self, start_time: time, stop_time: time, repeat: Repeat
    ) -> tuple[dict, dict]:
        """Create trigger date from Schedule object.

        :param time start_time:
        :param time stop_time:
        :param Repeat repeat:
        :return dict:
        """
        start_data: dict = {
            "hour": start_time.hour,
            "minute": start_time.minute,
            "timezone": start_time.tzinfo,
            "day": "*",
            "month": "*",
        }

        stop_data: dict = {
            "hour": stop_time.hour,
            "minute": stop_time.minute,
            "timezone": stop_time.tzinfo,
            "day": "*",
            "month": "*",
        }

        if repeat == Repeat.every_day:
            start_data["day_of_week"] = "*"
            stop_data["day_of_week"] = "*"
        elif repeat == Repeat.weekdays:
            start_data["day_of_week"] = "0,1,2,3,4"
            stop_data["day_of_week"] = "0,1,2,3,4"
        elif repeat == Repeat.weekends:
            start_data["day_of_week"] = "5,6"
            stop_data["day_of_week"] = "5,6"
        elif repeat == Repeat.monday:
            start_data["day_of_week"] = "0"
            stop_data["day_of_week"] = "0"
        elif repeat == Repeat.tuesday:
            start_data["day_of_week"] = "1"
            stop_data["day_of_week"] = "1"
        elif repeat == Repeat.wednesday:
            start_data["day_of_week"] = "2"
            stop_data["day_of_week"] = "2"
        elif repeat == Repeat.thursday:
            start_data["day_of_week"] = "3"
            stop_data["day_of_week"] = "3"
        elif repeat == Repeat.friday:
            start_data["day_of_week"] = "4"
            stop_data["day_of_week"] = "4"
        elif repeat == Repeat.saturday:
            start_data["day_of_week"] = "5"
            stop_data["day_of_week"] = "5"
        elif repeat == Repeat.sunday:
            start_data["day_of_week"] = "6"
            stop_data["day_of_week"] = "6"
        else:
            raise Exception("Unknown schedule.repeat value")

        return start_data, stop_data

    def exists(self, primary_key: str) -> bool:
        """Check if job with the specified primary_key exists.

        :param primary_key:
        :return:
        """
        result: Optional[Job] = self.scheduler.get_job(primary_key)
        if result is None:
            return False
        else:
            return True

    def create(
        self, start_time: time, stop_time: time, repeat: Repeat, relay_position: int
    ) -> tuple[str, str]:
        """Add a trigger to the scheduler.

        :param time start_time:
        :param time stop_time:
        :param Repeat repeat:
        :param int relay_position:
        :return:
        """
        start_data, stop_data = self._create_trigger_data(start_time, stop_time, repeat)
        start_job: Job = self.scheduler.add_job(
            task_switch_relay,
            CronTrigger(**start_data),
            args=[
                relay_position,
                True,
            ],
        )
        stop_job: Job = self.scheduler.add_job(
            task_switch_relay,
            CronTrigger(**stop_data),
            args=[
                relay_position,
                False,
            ],
        )
        return start_job.id, stop_job.id

    def delete(self, primary_key: str):
        """Add a trigger to the scheduler.

        :param int primary_key:
        :return:
        """
        self.scheduler.remove_job(primary_key)
