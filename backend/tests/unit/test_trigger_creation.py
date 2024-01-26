"""Tests for trigger creation."""
from datetime import time, timezone
from random import randint

import pytest
from app.scheduling import Repeat
from app.services.trigger import add_trigger, add_triggers, create_trigger_data
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
    }
    trigger_data = await create_trigger_data(schedule_data)

    assert trigger_data["hour"] == hour
    assert trigger_data["minute"] == minute
    assert trigger_data["day"] == "*"
    assert trigger_data["month"] == "*"

    if repeat == Repeat.once:
        pass
    elif repeat == Repeat.every_day:
        assert trigger_data["day_of_week"] == "*"
    elif repeat == Repeat.weekdays:
        assert trigger_data["day_of_week"] == "0,1,2,3,4"
    elif repeat == Repeat.weekends:
        assert trigger_data["day_of_week"] == "5,6"
    elif repeat == Repeat.monday:
        assert trigger_data["day_of_week"] == "0"
    elif repeat == Repeat.tuesday:
        assert trigger_data["day_of_week"] == "1"
    elif repeat == Repeat.wednesday:
        assert trigger_data["day_of_week"] == "2"
    elif repeat == Repeat.thursday:
        assert trigger_data["day_of_week"] == "3"
    elif repeat == Repeat.friday:
        assert trigger_data["day_of_week"] == "4"
    elif repeat == Repeat.saturday:
        assert trigger_data["day_of_week"] == "5"
    elif repeat == Repeat.sunday:
        assert trigger_data["day_of_week"] == "6"


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
    }
    with pytest.raises(Exception):
        await create_trigger_data(schedule_data)


async def test_add_trigger():
    """Tests adding one trigger to the scheduler.

    :return:
    """
    schedule_data: dict = {
        "start_time": time(hour=20, minute=10, tzinfo=timezone.utc),
        "duration": 10,
        "repeat": Repeat.every_day,
        "active": True,
    }

    async with AsyncScheduler() as scheduler:
        await add_trigger(scheduler, schedule_data)
        schedules: list[Schedule] = await scheduler.get_schedules()

        assert schedules
        assert len(schedules) == 1


async def test_add_multiple_triggers():
    """Tests adding multiple triggers to the scheduler.

    :return:
    """
    schedule_data: list[dict] = [
        {
            "start_time": time(hour=2, minute=57, tzinfo=timezone.utc),
            "duration": 10,
            "repeat": Repeat.every_day,
            "active": True,
        },
        {
            "start_time": time(hour=14, minute=10, tzinfo=timezone.utc),
            "duration": 10,
            "repeat": Repeat.friday,
            "active": True,
        },
        {
            "start_time": time(hour=22, minute=53, tzinfo=timezone.utc),
            "duration": 10,
            "repeat": Repeat.weekends,
            "active": True,
        },
    ]
    async with AsyncScheduler() as scheduler:
        await add_triggers(scheduler, schedule_data)
        schedules: list[Schedule] = await scheduler.get_schedules()

        assert schedules
        assert len(schedules) == 3
