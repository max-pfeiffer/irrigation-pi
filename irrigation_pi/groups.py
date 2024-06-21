"""Command groups."""

# ruff: noqa: D205, D301, D400

import os
import subprocess
import sys

import click

from irrigation_pi.export import backend_api_specs
from irrigation_pi.install import (
    install_all,
    install_application_configuration,
    install_database,
    install_debian_packages,
    install_nginx_configuration,
    install_systemd_configuration,
    install_systemd_resolved,
    install_wifi_hotspot,
)
from irrigation_pi.restart import restart_nginx, restart_uvicorn
from irrigation_pi.run import backend, frontend
from irrigation_pi.uninstall import (
    uninstall_all,
    uninstall_application_configuration,
    uninstall_database,
    uninstall_nginx_configuration,
    uninstall_systemd_configuration,
    uninstall_systemd_resolved,
    uninstall_wifi_hotspot,
)


def become_root():
    """Re-run the cli command with superuser privileges.

    :return:
    """
    if os.geteuid() != 0:
        click.echo(
            "Executing this command requires sudo privileges. If you "
            "encounter a password challenge, please enter your user's password. \n"
        )
        subprocess.call(["sudo", *sys.argv])
        sys.exit()


@click.group()
def install():
    """Install commands.
    \f

    :return:
    """
    become_root()


install.add_command(install_all)
install.add_command(install_debian_packages)
install.add_command(install_application_configuration)
install.add_command(install_database)
install.add_command(install_systemd_configuration)
install.add_command(install_nginx_configuration)
install.add_command(install_systemd_resolved)
install.add_command(install_wifi_hotspot)


@click.group()
def uninstall():
    """Uninstall commands.
    \f

    :return:
    """
    become_root()


uninstall.add_command(uninstall_all)
uninstall.add_command(uninstall_application_configuration)
uninstall.add_command(uninstall_database)
uninstall.add_command(uninstall_nginx_configuration)
uninstall.add_command(uninstall_systemd_configuration)
uninstall.add_command(uninstall_systemd_resolved)
uninstall.add_command(uninstall_wifi_hotspot)


@click.group()
def run():
    """Run commands.
    \f

    :return:
    """
    pass


run.add_command(backend)
run.add_command(frontend)


@click.group()
def restart():
    """Restart commands.
    \f

    :return:
    """
    pass


restart.add_command(restart_uvicorn)
restart.add_command(restart_nginx)


@click.group()
def export():
    """Update commands.
    \f

    :return:
    """
    pass


export.add_command(backend_api_specs)
