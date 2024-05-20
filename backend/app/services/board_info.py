"""Services for Raspberry Pi board information."""

from typing import Union

from gpiozero import Factory, PiBoardInfo

from app.adapters.base import RelayBoardAdapter


def service_get_board_info(adapter: RelayBoardAdapter) -> dict[str, Union[str, int]]:
    """Service for producing Raspberry Pi board information.

    :param adapter:
    :return:
    """
    pin_factory: Factory = adapter.get_pin_factory()
    board_info: PiBoardInfo = pin_factory.board_info
    data: dict[str, Union[str, int]] = {
        "revision": board_info.revision,
        "model": board_info.model,
        "pcb_revision": board_info.pcb_revision,
        "released": board_info.released,
        "soc": board_info.soc,
        "manufacturer": board_info.manufacturer,
        "memory": board_info.memory,
        "storage": board_info.storage,
        "usb": board_info.usb,
        "usb3": board_info.usb3,
        "ethernet": board_info.ethernet,
        "eth_speed": board_info.eth_speed,
        "wifi": board_info.wifi,
        "bluetooth": board_info.bluetooth,
        "csi": board_info.csi,
        "dsi": board_info.dsi,
    }
    return data
