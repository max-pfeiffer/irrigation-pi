"""Adapters for Waveshare boards."""

from typing import ClassVar, Optional

from gpiozero import Factory

from app.adapters.base import RelayBoardAdapter
from app.adapters.gpio_devices import Relay


class WaveshareRpiRelayBoardAdapter(RelayBoardAdapter):
    """Adapter for RPi Relay Board from Waveshare.

    The Board carries three relays which are connected to GPIO pins.
    https://www.waveshare.com/rpi-relay-board.htm
    https://www.waveshare.com/wiki/RPi_Relay_Board
    """

    relay_position_mapping: ClassVar[dict] = {
        1: 0,
        2: 1,
        3: 2,
    }

    def __init__(
        self,
        pin_factory: Optional[Factory] = None,
        relays: Optional[list[Relay]] = None,
    ):
        """Initialize object.

        :param list[Relay] relays:
        """
        self.pin_factory = pin_factory

        if relays is None:
            relays = [
                Relay(26, pin_factory=self.pin_factory),
                Relay(20, pin_factory=self.pin_factory),
                Relay(21, pin_factory=self.pin_factory),
            ]
        self.relays: list[Relay] = relays

    def get_pin_factory(self) -> Factory:
        """Return the pin factory."""
        return self.pin_factory

    def get_relay(self, relay_position: int) -> Relay:
        """Return the relay object at the desired position."""
        if relay_position not in self.relay_position_mapping.keys():
            raise ValueError("Invalid relay position")

        relay: Relay = self.relays[self.relay_position_mapping[relay_position]]
        return relay

    def get_relays(self) -> list[Relay]:
        """Return all relay objects."""
        return self.relays

    def on(self, relay_position: int):
        """Turn on relay at relay_position.

        :param int relay_position:
        :return:
        """
        if relay_position not in self.relay_position_mapping.keys():
            raise ValueError("Invalid relay position")

        relay: Relay = self.relays[self.relay_position_mapping[relay_position]]
        relay.on()

    def off(self, relay_position: int):
        """Turn off relay at relay_position.

        :param int relay_position:
        :return:
        """
        if relay_position not in self.relay_position_mapping.keys():
            raise ValueError("Invalid relay position")

        relay: Relay = self.relays[self.relay_position_mapping[relay_position]]
        relay.off()
