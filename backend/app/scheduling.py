"""Scheduling for relay switches."""
from datetime import datetime

from apscheduler import AsyncScheduler
from apscheduler.triggers.cron import CronTrigger
from starlette.types import ASGIApp, Receive, Scope, Send


def switch_relays():
    print("Hello, the time is", datetime.now())


class SchedulerMiddleware:
    def __init__(
        self,
        app: ASGIApp,
        scheduler: AsyncScheduler,
    ) -> None:
        self.app = app
        self.scheduler = scheduler

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "lifespan":
            async with self.scheduler:
                await self.scheduler.add_schedule(
                    switch_relays, CronTrigger.from_crontab("* * * * *"), id="switch_relays"
                )
                await self.scheduler.start_in_background()
                await self.app(scope, receive, send)
        else:
            await self.app(scope, receive, send)


scheduler = AsyncScheduler()
