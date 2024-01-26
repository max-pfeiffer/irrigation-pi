"""Scheduling for relay switches."""
from datetime import datetime
from enum import Enum

from apscheduler import AsyncScheduler
from starlette.types import ASGIApp, Receive, Scope, Send


class Repeat(str, Enum):
    """Enumeration for repeat values."""

    once = "once"
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


def switch_relays():
    """Trigger function to switch relays.

    :return:
    """
    print("Hello, the time is", datetime.now())


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
