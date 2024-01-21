"""Tests for services."""
from fake_objects import FakeRelay

from app.adapters.waveshare import WaveshareRpiRelayBoardAdapter
from app.services import switch_relay_off, switch_relay_on


def test_switch_relay_on():
    """Tests switching relays on.

    :return:
    """
    fake_relay_1: FakeRelay = FakeRelay()
    fake_relay_2: FakeRelay = FakeRelay()
    fake_relay_3: FakeRelay = FakeRelay()

    fake_adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter(
        relays=[fake_relay_1, fake_relay_2, fake_relay_3]
    )

    switch_relay_on("waveshare_rpi_relay_board", 1, adapter=fake_adapter)
    assert fake_relay_1.value == 1


def test_switch_relay_off():
    """Tests switching relays off.

    :return:
    """
    fake_relay_1: FakeRelay = FakeRelay()
    fake_relay_2: FakeRelay = FakeRelay()
    fake_relay_3: FakeRelay = FakeRelay()

    fake_adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter(
        relays=[fake_relay_1, fake_relay_2, fake_relay_3]
    )

    switch_relay_off("waveshare_rpi_relay_board", 1, adapter=fake_adapter)
    assert fake_relay_1.value == 0
