from gpiozero import DigitalOutputDevice
from typing import Union

class Relay(DigitalOutputDevice):
    def __init__(self, pin: Union[int, str]):
        super().__init__(pin, active_high=False)

