"""Relay board base class."""

from abc import ABC, abstractmethod

from gpiozero import Factory

from app.adapters.gpio_devices import Relay


class RelayBoardAdapter(ABC):
    """Base class for all adapters."""

    @abstractmethod
    def get_pin_factory(self) -> Factory:
        """Return the pin factory."""

    @abstractmethod
    def get_relay(self, relay_position: int) -> Relay:
        """Return the relay object at the desired position."""

    @abstractmethod
    def get_relays(self) -> list[Relay]:
        """Return all relay objects."""

    @abstractmethod
    def on(self, relay_position: int):
        """Turn on relay at relay_position.

        :param int relay_position:
        :return:
        """

    @abstractmethod
    def off(self, relay_position: int):
        """Turn off relay at relay_position.

        :param int relay_position:
        :return:
        """
