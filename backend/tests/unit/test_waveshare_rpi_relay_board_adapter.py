import pytest

from app.adapters.waveshare import WaveshareRpiRelayBoardAdapter
import pytest

from app.adapters.waveshare import WaveshareRpiRelayBoardAdapter


class FakeRelay:
    def __init__(self):
        self.state: bool = None

    def on(self):
        self.state = True

    def off(self):
        self.state = False


def test_relay_board_adapter() -> None:
    fake_relay_1: FakeRelay = FakeRelay()
    fake_relay_2: FakeRelay = FakeRelay()
    fake_relay_3: FakeRelay = FakeRelay()

    adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter(relays=[fake_relay_1, fake_relay_2, fake_relay_3])
    adapter.on(1)
    assert fake_relay_1.state

    adapter.off(1)
    assert not fake_relay_1.state

    adapter.on(2)
    assert fake_relay_2.state

    adapter.off(2)
    assert not fake_relay_2.state

    adapter.on(3)
    assert fake_relay_3.state

    adapter.off(3)
    assert not fake_relay_3.state


def test_relay_board_adapter_fails() -> None:
    fake_relay_1: FakeRelay = FakeRelay()
    fake_relay_2: FakeRelay = FakeRelay()
    fake_relay_3: FakeRelay = FakeRelay()

    adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter(relays=[fake_relay_1, fake_relay_2, fake_relay_3])

    with pytest.raises(ValueError):
        adapter.on(0)

    with pytest.raises(ValueError):
        adapter.on(4)
