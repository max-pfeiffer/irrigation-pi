"""Services for relay switching."""

from app.adapters.base import RelayBoardAdapter
from app.adapters.gpio_devices import Relay


def service_get_relay(adapter: RelayBoardAdapter, relay_position: int) -> dict:
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


def service_get_relays(adapter: RelayBoardAdapter) -> list[dict]:
    """Get all relay data.

    :param adapter:
    :return:
    """
    relays: list[Relay] = adapter.get_relays()
    data: list[dict] = []
    for index, relay in enumerate(relays):
        data.append({"position": index + 1, "on": bool(relay.value)})
    return data


def service_update_relay(adapter: RelayBoardAdapter, relay_position: int, on: bool):
    """Update relay.

    :param adapter:
    :param relay_position:
    :param on:
    :return:
    """
    if on:
        adapter.on(relay_position)
    else:
        adapter.off(relay_position)
