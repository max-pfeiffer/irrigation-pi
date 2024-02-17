"""Tests for systemd config."""

from irrigation_pi.constants import (
    APPLICATION_USER,
    BACKEND_PATH,
    VIRTUAL_ENVIRONMENT_PATH,
)
from irrigation_pi.utils import create_systemd_config


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
