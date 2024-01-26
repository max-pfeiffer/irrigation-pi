"""Repositories for data persistence."""
from datetime import date, datetime, time, timedelta

from apscheduler import AsyncScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlmodel import Session, select

from app.database.models import Schedule
from app.scheduling import Repeat, execute_task


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

    def update(self, **kwargs):
        """Update a Schedule object.

        :param kwargs:
        :return:
        """
        primary_key: int = kwargs.pop("primary_key")
        schedule: Schedule = self.get(primary_key)

        for key, value in kwargs.items():
            setattr(schedule, key, value)

        self.session.flush()

    def delete(self, primary_key: int):
        """Delete a schedule by primary_key.

        :param int primary_key:
        :return:
        """
        schedule: Schedule = self.get(primary_key)
        self.session.delete(schedule)
        self.session.flush()


class ApSchedulerRepository:
    """Repository for persisting Schedule objects."""

    def __init__(self, scheduler: AsyncScheduler) -> None:
        """Initialize object.

        :param AsyncScheduler scheduler:
        """
        self.scheduler: AsyncScheduler = scheduler

    async def _create_trigger_data(self, schedule_data: dict) -> tuple[dict, dict]:
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
            date.today(), start_time
        ) + timedelta(minutes=duration)
        stop_time: datetime.time = stop_date_time.time()
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

    async def add_triggers_for_schedule(self, schedule_data: dict) -> dict:
        """Add a trigger to the scheduler.

        :param dict schedule_data:
        :return:
        """
        start_data, stop_data = await self._create_trigger_data(schedule_data)
        primary_key_start: str = await self.scheduler.add_schedule(
            execute_task,
            CronTrigger(**start_data),
            args=[
                schedule_data["relay_board_type"],
                schedule_data["relay_position"],
                True,
            ],
        )
        primary_key_stop: str = await self.scheduler.add_schedule(
            execute_task,
            CronTrigger(**stop_data),
            args=[
                schedule_data["relay_board_type"],
                schedule_data["relay_position"],
                False,
            ],
        )

        return_data: dict = schedule_data.copy()
        return_data["start_schedule_id"] = primary_key_start
        return_data["stop_schedule_id"] = primary_key_stop
        return return_data

    async def add_triggers_for_schedules(self, schedule_data_list: list[dict]):
        """Add multiple triggers to the scheduler.

        :param list[dict] schedule_data_list:
        :return:
        """
        return_data_list: list[dict] = []

        for schedule_data in schedule_data_list:
            return_data: dict = await self.add_triggers_for_schedule(schedule_data)
            return_data_list.append(return_data)

        return return_data_list
