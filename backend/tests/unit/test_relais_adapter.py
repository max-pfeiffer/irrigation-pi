from time import sleep

from app.adapters.output_devices import Relay
from app.adapters.relay import RelayAdapter


def test_relay_adapter():
    relay: Relay = Relay(26)
    adapter: RelayAdapter = RelayAdapter([relay])
    adapter.on()

    sleep(5)

    adapter.off()

