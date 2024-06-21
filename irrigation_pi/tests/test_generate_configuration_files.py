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
