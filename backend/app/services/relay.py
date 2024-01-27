"""Services for relay switching."""
from app.adapters import RELAY_BOARD_TYPE_ADAPTER_MAPPING, RelayBoardType


def service_switch_relay(
    relay_board_type: RelayBoardType, relay_position: int, on: bool, adapter=None
) -> None:
    """Switches relay on.

    :param relay_board_type:
    :param relay_position:
    :param on:
    :param adapter:
    :return:
    """
    if adapter is None:
        adapter = RELAY_BOARD_TYPE_ADAPTER_MAPPING[relay_board_type]()

    if on:
        adapter.on(relay_position)
    else:
        adapter.off(relay_position)
