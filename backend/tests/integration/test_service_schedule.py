"""Integration tests for schedule service."""

from datetime import time
from uuid import uuid4

from app.database.models import Schedule
from app.scheduling import Repeat
from app.services.schedule import (
    active_schedule_exists,
    calculate_stop_time,
    set_system_timezone,
)
from sqlmodel import Session


def test_active_schedule_exists(integration_test_database_session: Session) -> None:
    """Test the active_schedule_exists() function.

    :param integration_test_database_session:
    :return:
    """
    schedule_1: Schedule = Schedule(
        start_time=time(hour=8, minute=15),
        stop_time=time(hour=9, minute=0),
        repeat=Repeat.every_day,
        duration=45,
        relay_position=1,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_1)
    schedule_2: Schedule = Schedule(
        start_time=time(hour=10, minute=15),
        stop_time=time(hour=11, minute=0),
        repeat=Repeat.every_day,
        duration=45,
        relay_position=1,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_2)
    schedule_3: Schedule = Schedule(
        start_time=time(hour=12, minute=15),
        stop_time=time(hour=13, minute=0),
        repeat=Repeat.every_day,
        duration=45,
        relay_position=1,
        active=True,
        start_job_id=str(uuid4()),
        stop_job_id=str(uuid4()),
    )
    integration_test_database_session.add(schedule_3)
    integration_test_database_session.commit()

    start_time = set_system_timezone(time(hour=8, minute=00))
    stop_time = calculate_stop_time(start_time, 20)
    schedule_exists = active_schedule_exists(
        integration_test_database_session, start_time, stop_time, relay_position=1
    )
    assert schedule_exists

    start_time = set_system_timezone(time(hour=8, minute=30))
    stop_time = calculate_stop_time(start_time, 15)
    schedule_exists = active_schedule_exists(
        integration_test_database_session, start_time, stop_time, relay_position=1
    )
    assert schedule_exists

    start_time = set_system_timezone(time(hour=9, minute=15))
    stop_time = calculate_stop_time(start_time, 15)
    schedule_exists = active_schedule_exists(
        integration_test_database_session, start_time, stop_time, relay_position=1
    )
    assert not schedule_exists

    start_time = set_system_timezone(time(hour=8, minute=45))
    stop_time = calculate_stop_time(start_time, 75)
    schedule_exists = active_schedule_exists(
        integration_test_database_session, start_time, stop_time, relay_position=1
    )
    assert schedule_exists

    start_time = set_system_timezone(time(hour=8, minute=00))
    stop_time = calculate_stop_time(start_time, 400)
    schedule_exists = active_schedule_exists(
        integration_test_database_session, start_time, stop_time, relay_position=1
    )
    assert schedule_exists
