"""Command groups."""
import click

from manage.export import backend_api_specs
from manage.install import (
    install_database,
    install_poetry,
)
from manage.run import backend, frontend
from manage.update import update_poetry


@click.group()
def install():
    """Install sub command group.

    :return:
    """
    pass


install.add_command(install_poetry)
install.add_command(install_database)


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
