"""Command groups."""
import click

from irrigation_pi.export import backend_api_specs
from irrigation_pi.install import (
    install_database,
    install_debian_packages,
    install_nginx_configuration,
    install_systemd_configuration,
)
from irrigation_pi.run import backend, frontend
from irrigation_pi.uninstall import (
    uninstall_nginx_configuration,
    uninstall_systemd_configuration,
)
from irrigation_pi.update import update_poetry


@click.group()
def install():
    """Install sub command group.

    :return:
    """
    pass


install.add_command(install_debian_packages)
install.add_command(install_systemd_configuration)
install.add_command(install_nginx_configuration)
install.add_command(install_database)


@click.group()
def uninstall():
    """Uninstall sub command group.

    :return:
    """
    pass


uninstall.add_command(uninstall_nginx_configuration)
uninstall.add_command(uninstall_systemd_configuration)


@click.group()
def update():
    """Update sub command group.

    :return:
    """
    pass


update.add_command(update_poetry)


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
