"""API endpoints for Relay objects."""
from fastapi import APIRouter

from app.api.v1.models import Relay
from app.config import relayBoardAdapter
from app.services.relay import service_get_relay

router = APIRouter()


@router.get("/{position}")
def get_relay(position: int) -> Relay:
    """Get relay by position.

    :param position:
    :return:
    """
    data: dict = service_get_relay(relayBoardAdapter, position)
    return Relay(**data)


@router.put("/{position}")
def update_relay(relay: Relay):
    """Update relay by position.

    :param relay:
    :return:
    """
    if relay.on:
        relayBoardAdapter.on(relay.position)
    else:
        relayBoardAdapter.off(relay.position)
