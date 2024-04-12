"""Tests for generation application configuration."""

from irrigation_pi.utils import create_application_configuration


def test_create_application_configuration():
    """Test creating application configuration.

    :return:
    """
    config: str = create_application_configuration()
    assert config
