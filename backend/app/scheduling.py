"""Scheduling for relay switches."""
from datetime import datetime
from enum import Enum

from apscheduler import AsyncScheduler
from starlette.types import ASGIApp, Receive, Scope, Send

from app.adapters import RelayBoardType
from app.services.relay import switch_relay


class Repeat(str, Enum):
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


def execute_task(relay_board_type: RelayBoardType, relay_position: int, on: bool):
    """Trigger function to switch relays.

    :param relay_board_type:
    :param relay_position:
    :param on:
    :return:
    """
    print(f"{relay_board_type}: position:{relay_position} on:{on}, {datetime.now()}]")
    switch_relay(relay_board_type, relay_position, on)


class SchedulerMiddleware:
    """Middleware to inject the scheduler instance."""

    def __init__(
        self,
        app: ASGIApp,
        scheduler: AsyncScheduler,
    ) -> None:
        """Initialize object.

        :param ASGIApp app:
        :param AsyncScheduler scheduler:
        """
        self.app = app
        self.scheduler = scheduler

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """Handle ASGI call.

        :param Scope scope:
        :param Receive receive:
        :param Send send:
        :return:
        """
        if scope["type"] == "lifespan":
            async with self.scheduler:
                await self.scheduler.start_in_background()
                await self.app(scope, receive, send)
        else:
            await self.app(scope, receive, send)


scheduler = AsyncScheduler()
