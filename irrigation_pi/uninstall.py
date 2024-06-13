"""Uninstall commands."""

import click
from click import Context

from irrigation_pi.constants import (
    APPLICATION_CONFIGURATION_PATH,
    DATABASE_PATH,
    NGINX_CONFIG_ACTIVATION_PATH,
    NGINX_CONFIG_PATH,
    SYSTEMD_CONFIG_PATH,
    WIFI_HOTSPOT_CONNECTION_NAME,
)
from irrigation_pi.utils import (
    run_subprocess,
)


@click.command(name="all")
@click.pass_context
def uninstall_all(ctx: Context):
    """Uninstall everything necessary to run the application on Raspberry Pi.

    :return:
    """
    ctx.forward(uninstall_application_configuration)
    ctx.forward(uninstall_database)
    ctx.forward(uninstall_systemd_configuration)
    ctx.forward(uninstall_nginx_configuration)


@click.command(name="config")
def uninstall_application_configuration():
    """Uninstall irrigation-pi application configuration.

    :return:
    """
    click.echo("Uninstalling irrigation-pi application configuration...")
    APPLICATION_CONFIGURATION_PATH.unlink(missing_ok=True)


@click.command(name="database")
def uninstall_database():
    """Uninstall database.

    :return:
    """
    click.echo("Uninstalling database...")
    DATABASE_PATH.unlink(missing_ok=True)


@click.command(name="systemd-config")
def uninstall_systemd_configuration():
    """Uninstall systemd config.

    :return:
    """
    click.echo("Uninstalling systemd configuration...")
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
    click.echo("Uninstalling nginx configuration...")
    # Deactivate site
    NGINX_CONFIG_ACTIVATION_PATH.unlink(missing_ok=True)

    # Delete nginx config
    NGINX_CONFIG_PATH.unlink(missing_ok=True)

    # Reload nginx config
    run_subprocess(["sudo", "systemctl", "reload", "nginx"])


@click.command(name="wifi-hotspot")
def uninstall_wifi_hotspot():
    """Uninstall Wi-Fi hotspot using NetworkManager.

    For more details see: https://networkmanager.dev/docs/api/latest/

    :return:
    """
    click.echo("Uninstalling Wi-Fi hotspot...")

    # Delete Wi-Fi hotspot with NetworkManager
    run_subprocess(
        ["sudo", "nmcli", "connection", "delete", WIFI_HOTSPOT_CONNECTION_NAME]
    )
