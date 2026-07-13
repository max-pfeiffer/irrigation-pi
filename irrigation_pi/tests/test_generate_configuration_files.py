"""Tests for generation application configuration."""

from pathlib import Path

from irrigation_pi.constants import (
    APPLICATION_USER,
    BACKEND_PATH,
    PORT,
    VIRTUAL_ENVIRONMENT_PATH,
)
from irrigation_pi.utils import (
    create_application_configuration,
    create_nginx_config,
    create_sudoers_config,
    create_systemd_config,
)


def test_create_application_configuration():
    """Test creating application configuration.

    :return:
    """
    config: str = create_application_configuration()
    assert config


def test_create_nginx_config():
    """Test generating nginx config.

    :return:
    """
    server_root_path: Path = (
        Path(__file__).parent.parent.resolve() / "frontend" / "www" / "browser"
    )
    nginx_config: str = create_nginx_config(PORT, server_root_path)

    assert str(PORT) in nginx_config
    assert str(server_root_path) in nginx_config


def test_create_systemd_config():
    """Test generating systemd config.

    :return:
    """
    systemd_config: str = create_systemd_config(
        APPLICATION_USER, VIRTUAL_ENVIRONMENT_PATH, BACKEND_PATH
    )

    assert APPLICATION_USER in systemd_config
    assert str(VIRTUAL_ENVIRONMENT_PATH) in systemd_config
    assert str(BACKEND_PATH) in systemd_config
    # System binary directories must be on PATH so the backend can run
    # system commands like timedatectl and sudo
    assert f"PATH={VIRTUAL_ENVIRONMENT_PATH / 'bin'}:/usr/local/bin" in systemd_config
    assert "/usr/bin" in systemd_config


def test_create_sudoers_config():
    """Test generating sudoers config.

    :return:
    """
    sudoers_config: str = create_sudoers_config(APPLICATION_USER)

    assert sudoers_config.startswith(APPLICATION_USER)
    assert "NOPASSWD" in sudoers_config
    assert "/usr/bin/timedatectl set-ntp *" in sudoers_config
    assert "/usr/bin/timedatectl set-time *" in sudoers_config
    # sudoers files must end with a newline, otherwise sudo rejects them
    assert sudoers_config.endswith("\n")
