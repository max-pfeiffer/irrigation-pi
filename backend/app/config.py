"""Application configuration."""

from pathlib import Path
from socket import AddressFamily
from typing import Any, Optional

import semver
import toml
from gpiozero.pins.mock import MockFactory
from gpiozero.pins.native import NativeFactory
from psutil import net_if_addrs
from pydantic import computed_field
from pydantic_settings import BaseSettings

from app.adapters import WaveshareRpiRelayBoardAdapter


class ApplicationSettings(BaseSettings):
    """Application settings."""

    title: str = "Irrigation Pi"
    description: str = "REST API of Irrigation Pi backend application."
    version: str = "1.0.0"
    database_name: str = "backend"

    @computed_field
    def database_uri(self) -> str:
        """URI for SQLite database connection.

        :return:
        """
        db_path: Path = (
            Path(__file__).parent.parent.resolve()
            / "sqlite_db"
            / f"{self.database_name}.db"
        )
        return f"sqlite:///{db_path!s}"

    @computed_field
    def api_prefix(self) -> str:
        """Return API prefix.

        :return:
        """
        version = semver.Version.parse(self.version)
        return f"/v{version.major}"

    @computed_field
    def ip_addresses(self) -> list[str]:
        """Return all IP v4 addresses of this host.

        :return:
        """
        if_data: dict[str, Any] = net_if_addrs()
        ip_adresses: list[str] = []
        for interface in if_data.values():
            ip_adresses.extend(
                [
                    interface_type.address
                    for interface_type in interface
                    if (interface_type.family == AddressFamily.AF_INET)
                ]
            )
        return ip_adresses


application_settings = ApplicationSettings()


def load_application_configuration() -> Optional[dict]:
    """Load application configuration from toml file.

    :return:
    """
    config_path: Path = Path(__file__).parent.parent.parent.resolve() / "config.toml"
    if config_path.exists():
        config: dict = toml.load(config_path)
        return config
    else:
        return None


def get_relay_board_adapter() -> WaveshareRpiRelayBoardAdapter:
    """Create a relay board adapter.

    gpiozero library has a certain way how it discovers pins factories.
    Please see: https://gpiozero.readthedocs.io/en/latest/api_pins.htm
    :return:
    """
    config: dict = load_application_configuration()
    if config:
        pin_factory_type: str = config["backend"]["pin_factory_type"]

        match pin_factory_type:
            case "rpi_gpio":
                from gpiozero.pins.rpigpio import RPiGPIOFactory

                pin_factory = RPiGPIOFactory()
            case "pigpio":
                from gpiozero.pins.pigpio import PiGPIOFactory

                pin_factory = PiGPIOFactory()
            case "native":
                pin_factory = NativeFactory()
            case _:
                raise ValueError("Invalid pin_factory_type in config file")
    else:
        # This MockFactory is used for development purposes. If application is
        # not run on a Raspberry Pi and the pin hardware with low-level drivers
        # is available, the instantiation of any other pin factory will fail.
        pin_factory = MockFactory()
    adapter = WaveshareRpiRelayBoardAdapter(pin_factory=pin_factory)
    return adapter


# We need to instantiate the board adapter with pin factory as global singleton.
# Otherwise, switching relays during application runtime will fail.
relayBoardAdapter = get_relay_board_adapter()
