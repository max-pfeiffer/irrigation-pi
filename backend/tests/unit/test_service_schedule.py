"""Tests for schedule service package."""

from datetime import datetime, time

from app.services.schedule import (
    calculate_stop_time,
    set_system_timezone,
)


def test_set_system_timezone() -> None:
    """Test setting the system timezone to a time object.

    :return:
    """
    naive_time: time = time(hour=10, minute=15)
    test_time = set_system_timezone(naive_time)

    tz_string = datetime.now().astimezone().tzname()
    assert test_time.tzname() == tz_string


def test_calculate_stop_time() -> None:
    """Test calculating the stop time for a timezone aware time object.

    :return:
    """
    start_time = set_system_timezone(time(hour=10, minute=0))
    stop_time = calculate_stop_time(start_time, 30)

    assert stop_time.hour == 10
    assert stop_time.minute == 30
    assert start_time.tzinfo == stop_time.tzinfo
