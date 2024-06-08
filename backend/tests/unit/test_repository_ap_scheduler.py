"""Tests for trigger creation."""

from datetime import time, timezone
from random import randint

import pytest
from app.adapters import RelayBoardType
from app.repositories import ApSchedulerRepository
from app.scheduling import Repeat
from apscheduler.job import Job
from apscheduler.schedulers.asyncio import AsyncIOScheduler


@pytest.mark.parametrize("repeat", Repeat)
async def test_create_trigger_data(repeat: Repeat):
    """Test creation of trigger data.

    :param Repeat repeat:
    :return:
    """
    start_hour: int = randint(0, 23)
    start_minute: int = randint(0, 59)

    stop_hour: int = randint(0, 23)
    stop_minute: int = randint(0, 59)

    job_data: dict = {
        "start_time": time(hour=start_hour, minute=start_minute, tzinfo=timezone.utc),
        "stop_time": time(hour=stop_hour, minute=stop_minute, tzinfo=timezone.utc),
        "repeat": repeat,
    }

    ap_repo: ApSchedulerRepository = ApSchedulerRepository(AsyncIOScheduler())
    start_data, stop_data = ap_repo._create_trigger_data(**job_data)

    assert start_data["hour"] == start_hour
    assert start_data["minute"] == start_minute
    assert start_data["day"] == "*"
    assert start_data["month"] == "*"

    assert stop_data["hour"] == stop_hour
    assert stop_data["minute"] == stop_minute
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
    job_data: dict = {
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
        ap_repo: ApSchedulerRepository = ApSchedulerRepository(AsyncIOScheduler())
        ap_repo._create_trigger_data(job_data)


async def test_create_schedule():
    """Tests adding one schedule (trigger + task) to the scheduler.

    :return:
    """
    job_data: dict = {
        "start_time": time(hour=20, minute=10, tzinfo=timezone.utc),
        "stop_time": time(hour=23, minute=20, tzinfo=timezone.utc),
        "repeat": Repeat.every_day,
        "relay_position": 1,
    }

    scheduler = AsyncIOScheduler()
    ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
    start_job_id, stop_job_id = ap_repo.create(**job_data)
    updated_job_data_ids: list[str] = [start_job_id, stop_job_id]

    jobs: list[Job] = scheduler.get_jobs()
    job_ids: list[int] = [job.id for job in jobs]

    assert len(jobs) == 2
    assert not set(updated_job_data_ids).difference(set(job_ids))


async def test_create_multiple_schedules():
    """Tests adding multiple schedules (trigger + task) to the scheduler.

    :return:
    """
    job_data: list[dict] = [
        {
            "start_time": time(hour=2, minute=57, tzinfo=timezone.utc),
            "stop_time": time(hour=3, minute=20, tzinfo=timezone.utc),
            "repeat": Repeat.every_day,
            "relay_position": 1,
        },
        {
            "start_time": time(hour=14, minute=10, tzinfo=timezone.utc),
            "stop_time": time(hour=15, minute=20, tzinfo=timezone.utc),
            "repeat": Repeat.friday,
            "relay_position": 1,
        },
        {
            "start_time": time(hour=22, minute=53, tzinfo=timezone.utc),
            "stop_time": time(hour=23, minute=20, tzinfo=timezone.utc),
            "repeat": Repeat.weekends,
            "relay_position": 1,
        },
    ]
    scheduler = AsyncIOScheduler()
    ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)

    for data in job_data:
        ap_repo.create(**data)
    jobs: list[Job] = scheduler.get_jobs()

    assert len(jobs) == 6


async def test_delete_schedule():
    """Tests deleting a schedule.

    :return:
    """
    job_data: dict = {
        "start_time": time(hour=20, minute=10, tzinfo=timezone.utc),
        "stop_time": time(hour=21, minute=14, tzinfo=timezone.utc),
        "repeat": Repeat.every_day,
        "relay_position": 1,
    }

    scheduler = AsyncIOScheduler()
    ap_repo: ApSchedulerRepository = ApSchedulerRepository(scheduler)
    start_job_id, stop_job_id = ap_repo.create(**job_data)

    jobs: list[Job] = scheduler.get_jobs()
    assert len(jobs) == 2

    ap_repo.delete(start_job_id)
    ap_repo.delete(stop_job_id)
    jobs: list[Job] = scheduler.get_jobs()
    assert not jobs
