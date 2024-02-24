"""Command groups."""
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
)
from irrigation_pi.run import backend, frontend
from irrigation_pi.uninstall import (
    uninstall_all,
    uninstall_application_configuration,
    uninstall_database,
    uninstall_nginx_configuration,
    uninstall_systemd_configuration,
)


def become_root():
    """Re-run the cli command with superuser privileges.

    :return:
    """
    if os.geteuid() != 0:
        subprocess.call(['sudo', *sys.argv])
        sys.exit()


@click.group()
def install():
    """Install sub command group.

    :return:
    """
    become_root()


install.add_command(install_all)
install.add_command(install_debian_packages)
install.add_command(install_application_configuration)
install.add_command(install_database)
install.add_command(install_systemd_configuration)
install.add_command(install_nginx_configuration)


@click.group()
def uninstall():
    """Uninstall sub command group.

    :return:
    """
    become_root()


uninstall.add_command(uninstall_all)
uninstall.add_command(uninstall_application_configuration)
uninstall.add_command(uninstall_database)
uninstall.add_command(uninstall_nginx_configuration)
uninstall.add_command(uninstall_systemd_configuration)


@click.group()
def run():
    """Run sub command group.

    :return:
    """
    pass


run.add_command(backend)
run.add_command(frontend)


@click.group()
def export():
    """Update sub command group.

    :return:
    """
    pass


export.add_command(backend_api_specs)
