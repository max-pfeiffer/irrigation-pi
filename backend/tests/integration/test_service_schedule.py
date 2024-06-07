"""Integration tests for schedule service."""

from datetime import time

import pytest
from app.scheduling import Repeat
from app.services.schedule import (
    active_schedule_exists,
    calculate_stop_time,
    service_create_schedule,
    service_delete_schedule,
    service_get_schedule,
    service_update_schedule,
    set_system_timezone,
)
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.exc import NoResultFound
from sqlmodel import Session

from tests.utils import RepeatQueryTestSchedules, RepeatTestData, TimeQueryTestSchedules


def test_active_schedule_exists_time_query(
    integration_test_database_session: Session,
    time_query_schedules: TimeQueryTestSchedules,
) -> None:
    """Test the active_schedule_exists() function.

    :param integration_test_database_session:
    :return:
    """
    start_time = set_system_timezone(time(hour=8, minute=00))
    stop_time = calculate_stop_time(start_time, 20)
    schedule_exists = active_schedule_exists(
        integration_test_database_session,
        start_time,
        stop_time,
        time_query_schedules.repeat,
        time_query_schedules.relay_position,
    )
    assert schedule_exists

    start_time = set_system_timezone(time(hour=8, minute=30))
    stop_time = calculate_stop_time(start_time, 15)
    schedule_exists = active_schedule_exists(
        integration_test_database_session,
        start_time,
        stop_time,
        time_query_schedules.repeat,
        time_query_schedules.relay_position,
    )
    assert schedule_exists

    start_time = set_system_timezone(time(hour=9, minute=15))
    stop_time = calculate_stop_time(start_time, 15)
    schedule_exists = active_schedule_exists(
        integration_test_database_session,
        start_time,
        stop_time,
        time_query_schedules.repeat,
        time_query_schedules.relay_position,
    )
    assert not schedule_exists

    start_time = set_system_timezone(time(hour=8, minute=45))
    stop_time = calculate_stop_time(start_time, 75)
    schedule_exists = active_schedule_exists(
        integration_test_database_session,
        start_time,
        stop_time,
        time_query_schedules.repeat,
        time_query_schedules.relay_position,
    )
    assert schedule_exists

    start_time = set_system_timezone(time(hour=8, minute=00))
    stop_time = calculate_stop_time(start_time, 400)
    schedule_exists = active_schedule_exists(
        integration_test_database_session,
        start_time,
        stop_time,
        time_query_schedules.repeat,
        time_query_schedules.relay_position,
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
    repeat_query_schedules: RepeatQueryTestSchedules,
    repeat_results: RepeatTestData,
) -> None:
    """Test the active_schedule_exists() function.

    :param integration_test_database_session:
    :return:
    """
    assert repeat_results.every_day_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_every_day.start_time,
        repeat_query_schedules.schedule_every_day.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )
    assert repeat_results.weekdays_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_weekdays.start_time,
        repeat_query_schedules.schedule_weekdays.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )
    assert repeat_results.weekends_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_weekends.start_time,
        repeat_query_schedules.schedule_weekends.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )
    assert repeat_results.monday_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_monday.start_time,
        repeat_query_schedules.schedule_monday.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )
    assert repeat_results.tuesday_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_tuesday.start_time,
        repeat_query_schedules.schedule_tuesday.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )
    assert repeat_results.wednesday_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_wednesday.start_time,
        repeat_query_schedules.schedule_wednesday.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )
    assert repeat_results.thursday_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_thursday.start_time,
        repeat_query_schedules.schedule_thursday.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )
    assert repeat_results.friday_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_friday.start_time,
        repeat_query_schedules.schedule_friday.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )
    assert repeat_results.saturday_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_saturday.start_time,
        repeat_query_schedules.schedule_saturday.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )
    assert repeat_results.sunday_result == active_schedule_exists(
        integration_test_database_session,
        repeat_query_schedules.schedule_sunday.start_time,
        repeat_query_schedules.schedule_sunday.stop_time,
        repeat_results.repeat,
        repeat_query_schedules.relay_position,
    )


def test_schedule_update_toggle_active_schedule(
    integration_test_database_session: Session, async_scheduler: AsyncIOScheduler
) -> None:
    """Test toggling the active flag for a schedule, active schedule use case.

    :param integration_test_database_session:
    :param async_scheduler:
    :return:
    """
    primary_key: int = service_create_schedule(
        integration_test_database_session,
        async_scheduler,
        time(hour=10, minute=15),
        Repeat.monday,
        10,
        True,
        1,
    )
    assert primary_key

    service_update_schedule(
        integration_test_database_session, async_scheduler, primary_key, active=False
    )
    schedule_data: dict = service_get_schedule(
        integration_test_database_session, primary_key
    )
    assert schedule_data

    service_delete_schedule(
        integration_test_database_session, async_scheduler, primary_key
    )
    with pytest.raises(NoResultFound):
        service_get_schedule(integration_test_database_session, primary_key)


def test_schedule_update_toggle_inactive_schedule(
    integration_test_database_session: Session, async_scheduler: AsyncIOScheduler
) -> None:
    """Test toggling the active flag for a schedule, inactive schedule use case.

    :param integration_test_database_session:
    :param async_scheduler:
    :return:
    """
    primary_key: int = service_create_schedule(
        integration_test_database_session,
        async_scheduler,
        time(hour=10, minute=15),
        Repeat.monday,
        10,
        False,
        1,
    )
    assert primary_key

    service_update_schedule(
        integration_test_database_session, async_scheduler, primary_key, active=True
    )
    schedule_data: dict = service_get_schedule(
        integration_test_database_session, primary_key
    )
    assert schedule_data

    service_delete_schedule(
        integration_test_database_session, async_scheduler, primary_key
    )
    with pytest.raises(NoResultFound):
        service_get_schedule(integration_test_database_session, primary_key)
