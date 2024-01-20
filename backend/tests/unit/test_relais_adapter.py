from time import sleep

from app.adapters.waveshare import WaveshareRpiRelayBoardAdapter


def test_relay_adapter():
    adapter: WaveshareRpiRelayBoardAdapter = WaveshareRpiRelayBoardAdapter()
    adapter.on(1)

    sleep(5)

    adapter.off(1)

