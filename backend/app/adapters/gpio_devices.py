"""GPIO Devices."""

from typing import Optional, Union

from gpiozero import DigitalOutputDevice, Factory


class Relay(DigitalOutputDevice):
    """Relay which is triggered by GPIO pins."""

    def __init__(self, pin: Union[int, str], pin_factory: Optional[Factory] = None):
        """Initialize relay object.

        :param Union[int, str] pin:
        """
        super().__init__(pin, active_high=False, pin_factory=pin_factory)
