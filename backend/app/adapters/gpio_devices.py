"""GPIO Devices."""
from typing import Union

from gpiozero import DigitalOutputDevice


class Relay(DigitalOutputDevice):
    """Relay which is triggered by GPIO pins."""

    def __init__(self, pin: Union[int, str]):
        """Initialize object.

        :param Union[int, str] pin:
        """
        super().__init__(pin, active_high=False)
