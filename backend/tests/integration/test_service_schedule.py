"""Integration tests for schedule service."""

from datetime import time
from uuid import uuid4

import pytest
from app.database.models import Schedule
from app.scheduling import Repeat
from app.services.schedule import (
    active_schedule_exists,
    calculate_stop_time,
    set_system_timezone,
)
from sqlmodel import Session

from tests.utils import RepeatTestData, TestSchedules


def test_active_schedule_exists_time_query(
    integration_test_database_session: Session,
) -> None:
    """Test the active_schedule_exists() function.

    :param integration_test_database_session:
    :return:
    """
    repeat = Repeat.monday

    schedule_1: Schedule = Schedule(
        start_time=set_system_timezone(time(hour=8, minute=15)),
        stop_time=set_system_timezone(time(hour=9, minute=0)),
        repeat=repeat,
        duration=45,
        relay_position=1,
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
        relay_position=1,
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
        integration_test_database_session,
        start_time,
        stop_time,
        repeat,
        relay_position=1,
    )
    assert schedule_exists

    start_time = set_system_timezone(time(hour=8, minute=30))
    stop_time = calculate_stop_time(start_time, 15)
    schedule_exists = active_schedule_exists(
        integration_test_database_session,
        start_time,
        stop_time,
        repeat,
        relay_position=1,
    )
    assert schedule_exists

    start_time = set_system_timezone(time(hour=9, minute=15))
    stop_time = calculate_stop_time(start_time, 15)
    schedule_exists = active_schedule_exists(
        integration_test_database_session,
        start_time,
        stop_time,
        repeat,
        relay_position=1,
    )
    assert not schedule_exists

    start_time = set_system_timezone(time(hour=8, minute=45))
    stop_time = calculate_stop_time(start_time, 75)
    schedule_exists = active_schedule_exists(
        integration_test_database_session,
        start_time,
        stop_time,
        repeat,
        relay_position=1,
    )
    assert schedule_exists

    start_time = set_system_timezone(time(hour=8, minute=00))
    stop_time = calculate_stop_time(start_time, 400)
    schedule_exists = active_schedule_exists(
        integration_test_database_session,
        start_time,
        stop_time,
        repeat,
        relay_position=1,
    )
    assert schedule_exists


@pytest.mark.parametrize(
    "repeat_results",
    [
        RepeatTestData(
            repeat=Repeat.every_day,
            every_day_result=True,
            weekdays_result=True,
            weekends_result=True,
            monday_result=True,
            tuesday_result=True,
            wednesday_result=True,
            thursday_result=True,
            friday_result=True,
            saturday_result=True,
            sunday_result=True,
        ),
        RepeatTestData(
            repeat=Repeat.weekdays,
            every_day_result=True,
            weekdays_result=True,
            weekends_result=False,
            monday_result=True,
            tuesday_result=True,
            wednesday_result=True,
            thursday_result=True,
            friday_result=True,
            saturday_result=False,
            sunday_result=False,
        ),
        RepeatTestData(
            repeat=Repeat.weekends,
            every_day_result=True,
            weekdays_result=False,
            weekends_result=True,
            monday_result=False,
            tuesday_result=False,
            wednesday_result=False,
            thursday_result=False,
            friday_result=False,
            saturday_result=True,
            sunday_result=True,
        ),
        RepeatTestData(
            repeat=Repeat.monday,
            every_day_result=True,
            weekdays_result=True,
            weekends_result=False,
            monday_result=True,
            tuesday_result=False,
            wednesday_result=False,
            thursday_result=False,
            friday_result=False,
            saturday_result=False,
            sunday_result=False,
        ),
        RepeatTestData(
            repeat=Repeat.tuesday,
            every_day_result=True,
            weekdays_result=True,
            weekends_result=False,
            monday_result=False,
            tuesday_result=True,
            wednesday_result=False,
            thursday_result=False,
            friday_result=False,
            saturday_result=False,
            sunday_result=False,
        ),
        RepeatTestData(
            repeat=Repeat.wednesday,
            every_day_result=True,
            weekdays_result=True,
            weekends_result=False,
            monday_result=False,
            tuesday_result=False,
            wednesday_result=True,
            thursday_result=False,
            friday_result=False,
            saturday_result=False,
            sunday_result=False,
        ),
        RepeatTestData(
            repeat=Repeat.thursday,
            every_day_result=True,
            weekdays_result=True,
            weekends_result=False,
            monday_result=False,
            tuesday_result=False,
            wednesday_result=False,
            thursday_result=True,
            friday_result=False,
            saturday_result=False,
            sunday_result=False,
        ),
        RepeatTestData(
            repeat=Repeat.friday,
            every_day_result=True,
            weekdays_result=True,
            weekends_result=False,
            monday_result=False,
            tuesday_result=False,
            wednesday_result=False,
            thursday_result=False,
            friday_result=True,
            saturday_result=False,
            sunday_result=False,
        ),
        RepeatTestData(
            repeat=Repeat.saturday,
            every_day_result=True,
            weekdays_result=False,
            weekends_result=True,
            monday_result=False,
            tuesday_result=False,
            wednesday_result=False,
            thursday_result=False,
            friday_result=False,
            saturday_result=True,
            sunday_result=False,
        ),
        RepeatTestData(
            repeat=Repeat.sunday,
            every_day_result=True,
            weekdays_result=False,
            weekends_result=True,
            monday_result=False,
            tuesday_result=False,
            wednesday_result=False,
            thursday_result=False,
            friday_result=False,
            saturday_result=False,
            sunday_result=True,
        ),
    ],
)
def test_active_schedule_exists_repeat_query(
    integration_test_database_session: Session,
    schedules: TestSchedules,
    repeat_results: RepeatTestData,
) -> None:
    """Test the active_schedule_exists() function.

    :param integration_test_database_session:
    :return:
    """
    assert repeat_results.every_day_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_every_day.start_time,
        schedules.schedule_every_day.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
    assert repeat_results.weekdays_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_weekdays.start_time,
        schedules.schedule_weekdays.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
    assert repeat_results.weekends_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_weekends.start_time,
        schedules.schedule_weekends.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
    assert repeat_results.monday_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_monday.start_time,
        schedules.schedule_monday.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
    assert repeat_results.tuesday_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_tuesday.start_time,
        schedules.schedule_tuesday.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
    assert repeat_results.wednesday_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_wednesday.start_time,
        schedules.schedule_wednesday.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
    assert repeat_results.thursday_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_thursday.start_time,
        schedules.schedule_thursday.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
    assert repeat_results.friday_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_friday.start_time,
        schedules.schedule_friday.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
    assert repeat_results.saturday_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_saturday.start_time,
        schedules.schedule_saturday.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
    assert repeat_results.sunday_result == active_schedule_exists(
        integration_test_database_session,
        schedules.schedule_sunday.start_time,
        schedules.schedule_sunday.stop_time,
        repeat_results.repeat,
        schedules.relay_position,
    )
