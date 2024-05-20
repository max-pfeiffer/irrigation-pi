"""Tests for service board info."""

from app.adapters.waveshare import WaveshareRpiRelayBoardAdapter
from app.services.board_info import service_get_board_info
from gpiozero.pins.mock import MockFactory

from tests.fake_objects import FakeRelay


def test_service_get_board_info() -> None:
    """Test the service board info."""
    fake_relay_1: FakeRelay = FakeRelay()
    fake_adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter(
        pin_factory=MockFactory(), relays=[fake_relay_1]
    )

    data = service_get_board_info(fake_adapter)
    assert data
