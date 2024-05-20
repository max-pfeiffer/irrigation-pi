"""API endpoint for Raspberry Pi board information."""

from typing import Union

from fastapi import APIRouter

from app.api.v1.models import RaspberryPiBoardInfo
from app.config import relayBoardAdapter
from app.services.board_info import service_get_board_info

router = APIRouter()


@router.get("/")
def get_board_info() -> RaspberryPiBoardInfo:
    """Get Raspberry Pi board information.

    :return:
    """
    data: dict[str, Union[str, int]] = service_get_board_info(relayBoardAdapter)
    return RaspberryPiBoardInfo(**data)
