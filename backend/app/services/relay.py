"""Services for relay switching."""
from app.adapters.base import ADAPTER_TYPE_MAPPING


def switch_relay_on(adapter_type: str, relay_position: int, adapter=None) -> None:
    """Switches relay on.

    :param adapter_type:
    :param relay_position:
    :param adapter:
    :return:
    """
    if adapter is None:
        adapter = ADAPTER_TYPE_MAPPING[adapter_type]()
    adapter.on(relay_position)


def switch_relay_off(adapter_type: str, relay_position: int, adapter=None) -> None:
    """Switches relay off.

    :param adapter_type:
    :param relay_position:
    :param adapter:
    :return:
    """
    if adapter is None:
        adapter = ADAPTER_TYPE_MAPPING[adapter_type]()
    adapter.off(relay_position)
