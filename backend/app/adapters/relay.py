from app.adapters.output_devices import Relay


class RelayAdapter:
    def __init__(self, relays: list[Relay]):
        self.relays: list[Relay] = relays

    def on(self):
        for relay in self.relays:
            relay.on()

    def off(self):
        for relay in self.relays:
            relay.off()
