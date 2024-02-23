"""Constants for irrigation_pi package."""
from pathlib import Path

DEBIAN_PACKAGES: list[str] = [
    "python3-gpiozero",
    "python3-pigpio",
    "python3-rpi.gpio",
    "nginx",
]

PROJECT_ROOT_PATH: Path = Path(__file__).parent.parent.resolve()
VIRTUAL_ENVIRONMENT_PATH: Path = PROJECT_ROOT_PATH / ".venv"
BACKEND_PATH: Path = PROJECT_ROOT_PATH / "backend"
FRONTEND_PATH: Path = PROJECT_ROOT_PATH / "frontend"

APPLICATION_CONFIGURATION_PATH: Path = PROJECT_ROOT_PATH / "config.toml"

NGINX_CONFIG_PATH: Path = Path("/etc/nginx/sites-available/irrigation-pi")
NGINX_CONFIG_ACTIVATION_PATH: Path = Path("/etc/nginx/sites-enabled/irrigation-pi")
NGINX_DEFAULT_CONFIG_ACTIVATION_PATH: Path = Path("/etc/nginx/sites-enabled/default")

SYSTEMD_CONFIG_PATH: Path = Path("/etc/systemd/system/irrigation-pi.service")

APPLICATION_USER: str = PROJECT_ROOT_PATH.owner()

HOST: str = "raspberrypi.local"
PORT: str = "80"
