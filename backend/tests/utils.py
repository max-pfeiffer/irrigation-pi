"""Test utilities."""

from dataclasses import dataclass

from app.database.models import Schedule
from app.scheduling import Repeat
from gpiozero import Device
from gpiozero.exc import BadPinFactory


def is_raspberry_pi() -> bool:
    """Return true if the function is run on a Raspberry Pi.

    :return:
    """
    try:
        Device.ensure_pin_factory()
    except BadPinFactory:
        return False
    else:
        return True


@dataclass
class TimeQueryTestSchedules:
    """Data class to hold test schedules."""

    repeat: Repeat
    relay_position: int
    schedule_1: Schedule
    schedule_2: Schedule
    schedule_3: Schedule


@dataclass
class RepeatQueryTestSchedules:
    """Data class to hold test schedules."""

    relay_position: int
    schedule_every_day: Schedule
    schedule_weekdays: Schedule
    schedule_weekends: Schedule
    schedule_monday: Schedule
    schedule_tuesday: Schedule
    schedule_wednesday: Schedule
    schedule_thursday: Schedule
    schedule_friday: Schedule
    schedule_saturday: Schedule
    schedule_sunday: Schedule


@dataclass
class RepeatTestData:
    """Data class to hold schedule test data."""

    repeat: Repeat
    every_day_result: bool
    weekdays_result: bool
    weekends_result: bool
    monday_result: bool
    tuesday_result: bool
    wednesday_result: bool
    thursday_result: bool
    friday_result: bool
    saturday_result: bool
    sunday_result: bool
