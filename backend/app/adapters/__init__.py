"""Adapters module."""

from enum import StrEnum

from app.adapters.waveshare import WaveshareRpiRelayBoardAdapter


class RelayBoardType(StrEnum):
    """Enumeration for repeat values."""

    waveshare_rpi_relay_board = "waveshare_rpi_relay_board"


RELAY_BOARD_TYPE_ADAPTER_MAPPING: dict = {
    RelayBoardType.waveshare_rpi_relay_board: WaveshareRpiRelayBoardAdapter
}
