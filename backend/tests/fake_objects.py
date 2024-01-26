"""Classes for fake objects to stub out dependencies."""


class FakeRelay:
    """Class for faking a relay."""

    def __init__(self):
        """Initialize object."""
        self._value: int = None

    def on(self) -> None:
        """Switches relay on.

        :return:
        """
        self._value = 1

    def off(self) -> None:
        """Switches relay off.

        :return:
        """
        self._value = 0

    @property
    def value(self):
        """Value representing current state."""
        return self._value
