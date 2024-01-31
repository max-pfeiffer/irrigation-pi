"""Repositories for data persistence."""
from datetime import date, datetime, time, timedelta

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

    def update(self, **kwargs) -> Schedule:
        """Update a Schedule object.

        :param int primary_key:
        :param kwargs:
        :return:
        """
        primary_key: int = kwargs.pop("primary_key")
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

    def _create_trigger_data(self, schedule_data: dict) -> tuple[dict, dict]:
        """Create trigger date from Schedule object.

        :param dict schedule_data:
        :return dict:
        """
        if not schedule_data["active"]:
            raise Exception("Schedule is not active")

        start_time: time = schedule_data["start_time"]
        repeat: Repeat = schedule_data["repeat"]
        duration: int = schedule_data["duration"]

        start_data: dict = {
            "hour": start_time.hour,
            "minute": start_time.minute,
            "timezone": start_time.tzinfo,
            "day": "*",
            "month": "*",
        }

        stop_date_time: datetime = datetime.combine(
            date.today(), start_time, tzinfo=start_time.tzinfo
        ) + timedelta(minutes=duration)
        stop_time: time = stop_date_time.timetz()
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

    def create(self, schedule_data: dict) -> dict:
        """Add a trigger to the scheduler.

        :param dict schedule_data:
        :return:
        """
        start_data, stop_data = self._create_trigger_data(schedule_data)
        start_job: Job = self.scheduler.add_job(
            task_switch_relay,
            CronTrigger(**start_data),
            args=[
                schedule_data["relay_position"],
                True,
            ],
        )
        stop_job: Job = self.scheduler.add_job(
            task_switch_relay,
            CronTrigger(**stop_data),
            args=[
                schedule_data["relay_position"],
                False,
            ],
        )

        return_data: dict = schedule_data.copy()
        return_data["start_schedule_id"] = start_job.id
        return_data["stop_schedule_id"] = stop_job.id
        return return_data

    def create_multiple(self, schedule_data_list: list[dict]):
        """Add multiple triggers to the scheduler.

        :param list[dict] schedule_data_list:
        :return:
        """
        return_data_list: list[dict] = []

        for schedule_data in schedule_data_list:
            return_data: dict = self.create(schedule_data)
            return_data_list.append(return_data)

        return return_data_list

    def delete(self, schedule_data: dict):
        """Add a trigger to the scheduler.

        :param dict schedule_data:
        :return:
        """
        self.scheduler.remove_job(schedule_data["start_schedule_id"])
        self.scheduler.remove_job(schedule_data["stop_schedule_id"])

    def update(self, schedule_data: dict) -> dict:
        """Add a trigger to the scheduler.

        :param dict schedule_data:
        :return:
        """
        self.delete(schedule_data)
        return_data: dict = self.create(schedule_data)
        return return_data
