from typing import Union

from gpiozero import DigitalOutputDevice


class Relay(DigitalOutputDevice):
    def __init__(self, pin: Union[int, str]):
        super().__init__(pin, active_high=False)
