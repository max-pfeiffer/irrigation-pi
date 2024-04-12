"""Tests for the Waveshare board adapter."""

import pytest
from app.adapters.waveshare import WaveshareRpiRelayBoardAdapter
from gpiozero.pins.mock import MockFactory

from tests.fake_objects import FakeRelay


def test_relay_board_adapter() -> None:
    """Tests switching relays on the board.

    :return:
    """
    fake_relay_1: FakeRelay = FakeRelay()
    fake_relay_2: FakeRelay = FakeRelay()
    fake_relay_3: FakeRelay = FakeRelay()

    fake_adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter(
        pin_factory=MockFactory(), relays=[fake_relay_1, fake_relay_2, fake_relay_3]
    )
    fake_adapter.on(1)
    assert fake_relay_1.value == 1

    fake_adapter.off(1)
    assert fake_relay_1.value == 0

    fake_adapter.on(2)
    assert fake_relay_2.value == 1

    fake_adapter.off(2)
    assert fake_relay_2.value == 0

    fake_adapter.on(3)
    assert fake_relay_3.value == 1

    fake_adapter.off(3)
    assert fake_relay_3.value == 0


def test_relay_board_adapter_fails() -> None:
    """Tests invalid relay positions.

    :return:
    """
    fake_relay_1: FakeRelay = FakeRelay()
    fake_relay_2: FakeRelay = FakeRelay()
    fake_relay_3: FakeRelay = FakeRelay()

    fake_adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter(
        pin_factory=MockFactory(), relays=[fake_relay_1, fake_relay_2, fake_relay_3]
    )

    with pytest.raises(ValueError):
        fake_adapter.on(0)

    with pytest.raises(ValueError):
        fake_adapter.on(4)
