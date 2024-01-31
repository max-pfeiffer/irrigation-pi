"""Test utilities."""
from gpiozero import Device
from gpiozero.exc import BadPinFactory


def is_raspberry_pi() -> bool:
    """Return true if the function is run on a Raspberry Pi.

    :return:
    """
    try:
        Device.ensure_pin_factory()
    except BadPinFactory:
        return False
    else:
        return True
