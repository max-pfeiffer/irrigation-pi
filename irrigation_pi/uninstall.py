"""Uninstall commands."""

import click

from irrigation_pi.constants import (
    NGINX_CONFIG_ACTIVATION_PATH,
    NGINX_CONFIG_PATH,
    SYSTEMD_CONFIG_PATH,
)
from irrigation_pi.utils import (
    run_subprocess,
)


@click.command(name="systemd-config")
def uninstall_systemd_configuration():
    """Uninstall systemd config.

    :return:
    """
    # Stop irrigation-pi service
    run_subprocess(["sudo", "systemctl", "stop", "irrigation-pi"])

    # Disable irrigation-pi service, so does not boot on startup anymore
    run_subprocess(["sudo", "systemctl", "disable", "irrigation-pi"])

    # Remove config file
    SYSTEMD_CONFIG_PATH.unlink(missing_ok=True)


@click.command(name="nginx-config")
def uninstall_nginx_configuration():
    """Uninstall nginx configuration.

    :return:
    """
    # Deactivate site
    NGINX_CONFIG_ACTIVATION_PATH.unlink(missing_ok=True)

    # Delete nginx config
    NGINX_CONFIG_PATH.unlink(missing_ok=True)

    # Reload nginx config
    run_subprocess(["sudo", "systemctl", "reload", "nginx"])
