"""Application configuration."""
from pathlib import Path
from typing import Optional

import toml
from gpiozero.pins.mock import MockFactory
from gpiozero.pins.native import NativeFactory
from pydantic import computed_field
from pydantic_settings import BaseSettings

from app.adapters import WaveshareRpiRelayBoardAdapter


class ApplicationSettings(BaseSettings):
    """Application settings."""

    database_name: str = "sqlite"

    @computed_field
    def database_uri(self) -> str:
        """URI for database connection.

        :return:
        """
        db_path: Path = (
            Path(__file__).parent.parent.resolve()
            / "sqlite_db"
            / f"{self.database_name}.db"
        )
        return f"sqlite:///{db_path!s}"


application_settings = ApplicationSettings()


def load_application_configuration() -> Optional[dict]:
    """Load application configuration from toml file.

    :return:
    """
    config_path: Path = Path(__file__).parent.parent.resolve() / "config.toml"
    if config_path.exists():
        config: dict = toml.load(config_path)
        return config
    else:
        return None


def get_relay_board_adapter() -> WaveshareRpiRelayBoardAdapter:
    """Create a relay board adapter.

    :return:
    """
    config: dict = load_application_configuration()
    if config:
        pin_factory_type: str = config["backend"]["pin_factory_type"]

        if pin_factory_type == "rpi_gpio":
            from gpiozero.pins.rpigpio import RPiGPIOFactory
            pin_factory = RPiGPIOFactory()
        elif pin_factory_type == "pigpio":
            from gpiozero.pins.pigpio import PiGPIOFactory
            pin_factory = PiGPIOFactory()
        elif pin_factory_type == "native":
            pin_factory = NativeFactory()
    else:
        pin_factory = MockFactory()

    adapter = WaveshareRpiRelayBoardAdapter(pin_factory=pin_factory)
    return adapter


relayBoardAdapter = get_relay_board_adapter()
