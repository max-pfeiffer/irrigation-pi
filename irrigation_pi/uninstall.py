"""Uninstall commands."""

from configparser import ConfigParser

# ruff: noqa: D205, D301, D400
import click
from click import Context

from irrigation_pi.constants import (
    APPLICATION_CONFIGURATION_PATH,
    DATABASE_PATH,
    NETWORKMANAGER_CONFIG_FILE,
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
    \f
    :return:
    """
    ctx.forward(uninstall_application_configuration)
    ctx.forward(uninstall_database)
    ctx.forward(uninstall_systemd_configuration)
    ctx.forward(uninstall_nginx_configuration)
    ctx.forward(uninstall_systemd_resolved)


@click.command(name="config")
def uninstall_application_configuration():
    """Uninstall irrigation-pi application configuration.
    \f
    :return:
    """
    click.echo("Uninstalling irrigation-pi application configuration...")
    APPLICATION_CONFIGURATION_PATH.unlink(missing_ok=True)


@click.command(name="database")
def uninstall_database():
    """Uninstall database.
    \f
    :return:
    """
    click.echo("Uninstalling database...")
    DATABASE_PATH.unlink(missing_ok=True)


@click.command(name="systemd-config")
def uninstall_systemd_configuration():
    """Uninstall systemd config.
    \f
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
    \f
    :return:
    """
    click.echo("Uninstalling nginx configuration...")
    # Deactivate site
    NGINX_CONFIG_ACTIVATION_PATH.unlink(missing_ok=True)

    # Delete nginx config
    NGINX_CONFIG_PATH.unlink(missing_ok=True)

    # Reload nginx config
    run_subprocess(["sudo", "systemctl", "reload", "nginx"])


@click.command(name="systemd-resolved")
def uninstall_systemd_resolved():
    """Uninstall systemd-resolved as Network Name Resolution manager.

    For more details see: https://www.freedesktop.org/software/systemd/man/latest/systemd-resolved.html

    \f
    :return:
    """
    # Remove DNS processing mode in NetworkManager config
    click.echo("Remove DNS processing mode from NetworkManager config...")
    networkmanager_config = ConfigParser()
    networkmanager_config.read(NETWORKMANAGER_CONFIG_FILE)
    networkmanager_config.remove_option("main", "dns")

    with open(NETWORKMANAGER_CONFIG_FILE, "w") as file:
        networkmanager_config.write(file, space_around_delimiters=False)

    # Remove Debian package
    click.echo("Removing systemd-resolved Debian package...")
    run_subprocess(["sudo", "apt", "purge", "systemd-resolved", "-y"])


@click.command(name="wifi-hotspot")
def uninstall_wifi_hotspot():
    """Uninstall Wi-Fi hotspot using NetworkManager.

    For more details see: https://networkmanager.dev/docs/api/latest/
    \f
    :return:
    """
    # Delete Wi-Fi hotspot with NetworkManager
    click.echo("Uninstalling Wi-Fi hotspot...")
    run_subprocess(
        ["sudo", "nmcli", "connection", "delete", WIFI_HOTSPOT_CONNECTION_NAME]
    )

    click.echo("Restarting Uvicorn server...")
    run_subprocess(["sudo", "systemctl", "stop", "irrigation-pi"])
    run_subprocess(["sudo", "systemctl", "start", "irrigation-pi"])
