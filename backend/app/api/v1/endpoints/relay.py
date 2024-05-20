"""API endpoints for Relay objects."""

from fastapi import APIRouter

from app.api.v1.models import Relay, RelayUpdate
from app.config import relayBoardAdapter
from app.services.relay import (
    service_get_relay,
    service_get_relays,
    service_update_relay,
)

router = APIRouter()


@router.get("/")
def get_relays() -> list[Relay]:
    """Get all relays.

    :return:
    """
    data: list[dict] = service_get_relays(relayBoardAdapter)
    relays: list[Relay] = [Relay(**item) for item in data]
    return relays


@router.get("/{position}")
def get_relay(position: int) -> Relay:
    """Get relay by position.

    :param position:
    :return:
    """
    data: dict = service_get_relay(relayBoardAdapter, position)
    return Relay(**data)


@router.put("/{position}")
def update_relay(position: int, relay: RelayUpdate):
    """Update relay by position.

    :param position:
    :param relay:
    :return:
    """
    service_update_relay(relayBoardAdapter, position, relay.on)
