class FakeRelay:
    def __init__(self):
        self._value: int = None

    def on(self) -> None:
        self._value = 1

    def off(self) -> None:
        self._value = 0

    @property
    def value(self):
        return self._value
