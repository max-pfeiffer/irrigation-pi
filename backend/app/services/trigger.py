"""Trigger logic."""
from datetime import time

from apscheduler import AsyncScheduler
from apscheduler.triggers.cron import CronTrigger

from app.scheduling import Repeat, switch_relays


async def create_trigger_data(schedule_data: dict) -> dict:
    """Create trigger date from Schedule object.

    :param dict schedule_data:
    :return dict:
    """
    if not schedule_data["active"]:
        raise Exception("Schedule is not active")

    start_time: time = schedule_data["start_time"]
    repeat: Repeat = schedule_data["repeat"]

    data: dict = {
        "hour": start_time.hour,
        "minute": start_time.minute,
        "timezone": start_time.tzinfo,
        "day": "*",
        "month": "*",
    }

    if repeat == Repeat.once:
        pass
    elif repeat == Repeat.every_day:
        data["day_of_week"] = "*"
    elif repeat == Repeat.weekdays:
        data["day_of_week"] = "0,1,2,3,4"
    elif repeat == Repeat.weekends:
        data["day_of_week"] = "5,6"
    elif repeat == Repeat.monday:
        data["day_of_week"] = "0"
    elif repeat == Repeat.tuesday:
        data["day_of_week"] = "1"
    elif repeat == Repeat.wednesday:
        data["day_of_week"] = "2"
    elif repeat == Repeat.thursday:
        data["day_of_week"] = "3"
    elif repeat == Repeat.friday:
        data["day_of_week"] = "4"
    elif repeat == Repeat.saturday:
        data["day_of_week"] = "5"
    elif repeat == Repeat.sunday:
        data["day_of_week"] = "6"
    else:
        raise Exception("Unknown schedule.repeat value")

    return data


async def add_trigger(scheduler: AsyncScheduler, schedule_data: dict):
    """Add a trigger to the scheduler.

    :param AsyncScheduler scheduler:
    :param dict schedule_data:
    :return:
    """
    trigger_data = await create_trigger_data(schedule_data)
    await scheduler.add_schedule(
        switch_relays, CronTrigger(**trigger_data), id="switch_relays"
    )
    test = await scheduler.get_schedules()
    print(test)


async def add_triggers(scheduler: AsyncScheduler, schedule_data_list: list[dict]):
    """Add multiple triggers to the scheduler.

    :param AsyncScheduler scheduler:
    :param list[dict] schedule_data_list:
    :return:
    """
    for schedule_data in schedule_data_list:
        await add_trigger(scheduler, schedule_data)
