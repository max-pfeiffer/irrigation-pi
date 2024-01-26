"""Tests for services."""
from app.adapters.waveshare import WaveshareRpiRelayBoardAdapter
from app.services.relay import switch_relay

from tests.fake_objects import FakeRelay


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

    switch_relay("waveshare_rpi_relay_board", 1, True, adapter=fake_adapter)
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

    switch_relay("waveshare_rpi_relay_board", 1, False, adapter=fake_adapter)
    assert fake_relay_1.value == 0
