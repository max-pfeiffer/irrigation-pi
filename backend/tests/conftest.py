"""Test fixtures."""

from datetime import time
from pathlib import Path
from uuid import uuid4

import pytest
from alembic import command
from alembic.config import Config
from app.config import application_settings
from app.database.models import Schedule
from app.scheduling import Repeat
from app.services.schedule import set_system_timezone
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi.testclient import TestClient
from pytest import MonkeyPatch
from sqlmodel import Session

from tests.utils import RepeatQueryTestSchedules, TimeQueryTestSchedules


@pytest.fixture(scope="package")
def api_test_database() -> str:
    """Create a test database."""
    with MonkeyPatch.context() as mp:
        database_name: str = "api_test"
        mp.setenv("database_name", database_name)
        mp.setattr(application_settings, "database_name", database_name)

        # Apply migrations
        migrations_path: Path = Path(__file__).parent.parent.resolve() / "migrations"
        alembic_cfg = Config()
        alembic_cfg.set_main_option("script_location", str(migrations_path))
        command.upgrade(alembic_cfg, "head")

        yield database_name

        database_path: Path = (
            Path(__file__).parent.parent.resolve() / "sqlite_db" / f"{database_name}.db"
        )
        if database_path.exists():
            database_path.unlink()


@pytest.fixture(scope="package")
def test_client(api_test_database: str) -> TestClient:
    """Provides test client for API tests."""
    from app.main import app

    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="package")
def integration_test_database_session() -> Session:
    """Create a test database for integration tests."""
    with MonkeyPatch.context() as mp:
        database_name: str = "integration_test"
        mp.setenv("database_name", database_name)
        mp.setattr(application_settings, "database_name", database_name)

        # Apply migrations
        migrations_path: Path = Path(__file__).parent.parent.resolve() / "migrations"
        alembic_cfg = Config()
        alembic_cfg.set_main_option("script_location", str(migrations_path))
        command.upgrade(alembic_cfg, "head")

        from app.database.config import get_session

        database_session_generator = get_session()

        yield next(database_session_generator)

        database_path: Path = (
            Path(__file__).parent.parent.resolve() / "sqlite_db" / f"{database_name}.db"
        )
        if database_path.exists():
            database_path.unlink()


@pytest.fixture(scope="function")
def time_query_schedules(
    integration_test_database_session: Session,
) -> TimeQueryTestSchedules:
    """Schedules for active schedule test.

    :param integration_test_database_session:
    :return:
    """
    repeat: Repeat = Repeat.monday
    relay_position: int = 1
    schedule_1: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=8, minute=15)),
        stop_time=set_system_timezone(time(hour=9, minute=0)),
        repeat=repeat,
        duration=45,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_1)
    schedule_2: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=10, minute=15)),
        stop_time=set_system_timezone(time(hour=11, minute=0)),
        repeat=repeat,
        duration=45,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_2)
    schedule_3: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=12, minute=15)),
        stop_time=set_system_timezone(time(hour=13, minute=0)),
        repeat=repeat,
        duration=45,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_3)
    integration_test_database_session.commit()

    yield TimeQueryTestSchedules(
        repeat=repeat,
        relay_position=relay_position,
        schedule_1=schedule_1,
        schedule_2=schedule_2,
        schedule_3=schedule_3,
    )

    integration_test_database_session.delete(schedule_1)
    integration_test_database_session.delete(schedule_2)
    integration_test_database_session.delete(schedule_3)
    integration_test_database_session.commit()


@pytest.fixture(scope="function")
def repeat_query_schedules(
    integration_test_database_session: Session,
) -> RepeatQueryTestSchedules:
    """Schedules for active schedule test.

    :param integration_test_database_session:
    :return:
    """
    relay_position: int = 1
    schedule_every_day: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=1, minute=00)),
        stop_time=set_system_timezone(time(hour=1, minute=30)),
        repeat=Repeat.every_day,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_every_day)
    schedule_weekdays: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=2, minute=00)),
        stop_time=set_system_timezone(time(hour=2, minute=30)),
        repeat=Repeat.weekdays,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_weekdays)
    schedule_weekends: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=3, minute=00)),
        stop_time=set_system_timezone(time(hour=3, minute=30)),
        repeat=Repeat.weekends,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_weekends)
    schedule_monday: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=4, minute=00)),
        stop_time=set_system_timezone(time(hour=4, minute=30)),
        repeat=Repeat.monday,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_monday)
    schedule_tuesday: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=5, minute=00)),
        stop_time=set_system_timezone(time(hour=5, minute=30)),
        repeat=Repeat.tuesday,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_tuesday)
    schedule_wednesday: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=6, minute=00)),
        stop_time=set_system_timezone(time(hour=6, minute=30)),
        repeat=Repeat.wednesday,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_wednesday)
    schedule_thursday: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=7, minute=00)),
        stop_time=set_system_timezone(time(hour=7, minute=30)),
        repeat=Repeat.thursday,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_thursday)
    schedule_friday: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=8, minute=00)),
        stop_time=set_system_timezone(time(hour=8, minute=30)),
        repeat=Repeat.friday,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_friday)
    schedule_saturday: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=9, minute=00)),
        stop_time=set_system_timezone(time(hour=9, minute=30)),
        repeat=Repeat.saturday,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_saturday)
    schedule_sunday: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=10, minute=00)),
        stop_time=set_system_timezone(time(hour=10, minute=30)),
        repeat=Repeat.sunday,
        duration=30,
        relay_position=relay_position,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_sunday)
    integration_test_database_session.commit()

    yield RepeatQueryTestSchedules(
        relay_position=relay_position,
        schedule_every_day=schedule_every_day,
        schedule_weekdays=schedule_weekdays,
        schedule_weekends=schedule_weekends,
        schedule_monday=schedule_monday,
        schedule_tuesday=schedule_tuesday,
        schedule_wednesday=schedule_wednesday,
        schedule_thursday=schedule_thursday,
        schedule_friday=schedule_friday,
        schedule_saturday=schedule_saturday,
        schedule_sunday=schedule_sunday,
    )

    integration_test_database_session.delete(schedule_every_day)
    integration_test_database_session.delete(schedule_weekdays)
    integration_test_database_session.delete(schedule_weekends)
    integration_test_database_session.delete(schedule_monday)
    integration_test_database_session.delete(schedule_tuesday)
    integration_test_database_session.delete(schedule_wednesday)
    integration_test_database_session.delete(schedule_thursday)
    integration_test_database_session.delete(schedule_friday)
    integration_test_database_session.delete(schedule_saturday)
    integration_test_database_session.delete(schedule_sunday)
    integration_test_database_session.commit()


@pytest.fixture(scope="function")
def async_scheduler() -> AsyncIOScheduler:
    """Provide AsyncIOScheduler as fixture.

    :return:
    """
    scheduler: AsyncIOScheduler = AsyncIOScheduler()
    scheduler.start()
    yield scheduler
    scheduler.shutdown()
