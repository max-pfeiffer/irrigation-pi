"""Scheduling for relay switches."""

from datetime import datetime
from enum import StrEnum

from app.config import relayBoardAdapter
from app.services.relay import service_update_relay


class Repeat(StrEnum):
    """Enumeration for repeat values."""

    every_day = "every_day"
    weekdays = "weekdays"
    weekends = "weekends"
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    sunday = "sunday"


def task_switch_relay(relay_position: int, on: bool):
    """Trigger function to switch relays.

    :param relay_position:
    :param on:
    :return:
    """
    print(f"position:{relay_position} on:{on}, {datetime.now()}]")
    service_update_relay(relayBoardAdapter, relay_position, on)
