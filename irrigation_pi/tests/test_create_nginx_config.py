"""Tests for nginx config."""
from pathlib import Path

from irrigation_pi.constants import HOST, PORT
from irrigation_pi.utils import create_nginx_config


def test_create_nginx_config():
    """Test generating nginx config.

    :return:
    """
    server_root_path: Path = (
        Path(__file__).parent.parent.resolve() / "frontend" / "www" / "browser"
    )
    nginx_config: str = create_nginx_config(HOST, PORT, server_root_path)

    assert str(server_root_path) in nginx_config
