"""Tests for low level GPIO functionality."""

import asyncio
import time

import pytest
from app.adapters import WaveshareRpiRelayBoardAdapter
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from tests.utils import is_raspberry_pi


@pytest.mark.skipif(not is_raspberry_pi(), reason="Needs to be run on Raspberry Pi")
def test_basic_gpio_functionality():
    """Test basic GPIO functionality."""
    adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter()
    adapter.on(1)
    time.sleep(2)
    adapter.off(1)
    assert adapter


@pytest.mark.skipif(not is_raspberry_pi(), reason="Needs to be run on Raspberry Pi")
def test_scheduled_gpio_functionality():
    """Test scheduled GPIO functionality.

    :return:
    """

    def switch_relay():
        """Switch first relay."""
        adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter()
        adapter.on(1)
        time.sleep(1)
        adapter.off(1)

    scheduler = BackgroundScheduler()
    scheduler.start()

    job = scheduler.add_job(switch_relay, "interval", seconds=2)

    time.sleep(10)
    assert job


@pytest.mark.skipif(not is_raspberry_pi(), reason="Needs to be run on Raspberry Pi")
async def test_async_scheduled_gpio_functionality():
    """Test async scheduled GPIO functionality.

    :return:
    """

    async def switch_relay():
        """Switch first relay."""
        adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter()
        adapter.on(1)
        await asyncio.sleep(1)
        adapter.off(1)

    scheduler = AsyncIOScheduler()
    scheduler.start()

    job = scheduler.add_job(switch_relay, "interval", seconds=2)

    await asyncio.sleep(10)
    assert job
