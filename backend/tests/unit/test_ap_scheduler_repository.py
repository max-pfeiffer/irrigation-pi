"""Tests for trigger creation."""
from datetime import time, timezone
from random import randint

import pytest
from app.adapters import RelayBoardType
from app.repositories import ApSchedulerRepository
from app.scheduling import Repeat
from apscheduler import AsyncScheduler, Schedule


@pytest.mark.parametrize("repeat", Repeat)
async def test_create_trigger_data(repeat: Repeat):
    """Test creation of trigger data.

    :param Repeat repeat:
    :return:
    """
    hour: int = randint(0, 23)
    minute: int = randint(0, 59)
    schedule_data: dict = {
        "start_time": time(hour=hour, minute=minute, tzinfo=timezone.utc),
        "duration": randint(1, 1440),
        "repeat": repeat,
        "active": True,
        "relay_board_type": RelayBoardType.waveshare_rpi_relay_board,
        "relay_position": 1,
    }
    async with AsyncScheduler() as scheduler:
        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        start_data, stop_data = await ap_repo._create_trigger_data(schedule_data)

    assert start_data["hour"] == hour
    assert start_data["minute"] == minute
    assert start_data["day"] == "*"
    assert start_data["month"] == "*"

    # assert stop_data["hour"] == hour
    # assert stop_data["minute"] == minute
    assert stop_data["day"] == "*"
    assert stop_data["month"] == "*"

    if repeat == Repeat.every_day:
        assert start_data["day_of_week"] == "*"
    elif repeat == Repeat.weekdays:
        assert start_data["day_of_week"] == "0,1,2,3,4"
    elif repeat == Repeat.weekends:
        assert start_data["day_of_week"] == "5,6"
    elif repeat == Repeat.monday:
        assert start_data["day_of_week"] == "0"
    elif repeat == Repeat.tuesday:
        assert start_data["day_of_week"] == "1"
    elif repeat == Repeat.wednesday:
        assert start_data["day_of_week"] == "2"
    elif repeat == Repeat.thursday:
        assert start_data["day_of_week"] == "3"
    elif repeat == Repeat.friday:
        assert start_data["day_of_week"] == "4"
    elif repeat == Repeat.saturday:
        assert start_data["day_of_week"] == "5"
    elif repeat == Repeat.sunday:
        assert start_data["day_of_week"] == "6"


async def test_create_trigger_data_fail():
    """Trigger creation should fail when schedule is not active.

    :return:
    """
    schedule_data: dict = {
        "start_time": time(
            hour=randint(0, 23), minute=randint(0, 59), tzinfo=timezone.utc
        ),
        "duration": randint(1, 1440),
        "repeat": Repeat.every_day,
        "active": False,
        "relay_board_type": RelayBoardType.waveshare_rpi_relay_board,
        "relay_position": 1,
    }
    with pytest.raises(Exception):
        async with AsyncScheduler() as scheduler:
            ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
            await ap_repo._create_trigger_data(schedule_data)


async def test_create_schedule():
    """Tests adding one schedule (trigger + task) to the scheduler.

    :return:
    """
    schedule_data: dict = {
        "start_time": time(hour=20, minute=10, tzinfo=timezone.utc),
        "duration": 10,
        "repeat": Repeat.every_day,
        "active": True,
        "relay_board_type": RelayBoardType.waveshare_rpi_relay_board,
        "relay_position": 1,
    }

    async with AsyncScheduler() as scheduler:
        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        await ap_repo.create(schedule_data)
        schedules: list[Schedule] = await scheduler.get_schedules()

        assert schedules
        assert len(schedules) == 2


async def test_create_multiple_schedules():
    """Tests adding multiple schedules (trigger + task) to the scheduler.

    :return:
    """
    schedule_data: list[dict] = [
        {
            "start_time": time(hour=2, minute=57, tzinfo=timezone.utc),
            "duration": 10,
            "repeat": Repeat.every_day,
            "active": True,
            "relay_board_type": RelayBoardType.waveshare_rpi_relay_board,
            "relay_position": 1,
        },
        {
            "start_time": time(hour=14, minute=10, tzinfo=timezone.utc),
            "duration": 10,
            "repeat": Repeat.friday,
            "active": True,
            "relay_board_type": RelayBoardType.waveshare_rpi_relay_board,
            "relay_position": 1,
        },
        {
            "start_time": time(hour=22, minute=53, tzinfo=timezone.utc),
            "duration": 10,
            "repeat": Repeat.weekends,
            "active": True,
            "relay_board_type": RelayBoardType.waveshare_rpi_relay_board,
            "relay_position": 1,
        },
    ]
    async with AsyncScheduler() as scheduler:
        ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
        await ap_repo.create_multiple(schedule_data)
        schedules: list[Schedule] = await scheduler.get_schedules()

        assert schedules
        assert len(schedules) == 6
