"""Services for relay switching."""
from app.adapters.base import RelayBoardAdapter
from app.adapters.gpio_devices import Relay


def service_get_relay(
    adapter: RelayBoardAdapter, relay_position: int
) -> dict:
    """Get relay data.

    :param adapter:
    :param relay_position:
    :return:
    """
    relay: Relay = adapter.get_relay(relay_position)
    data: dict = {
        "position": relay_position,
        "on": bool(relay.value),
    }
    return data
