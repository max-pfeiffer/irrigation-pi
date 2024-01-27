"""Command groups."""
import click

from manage.export import backend_api_specs
from manage.install import install_backend_dependencies, install_poetry
from manage.update import update_backend_dependencies, update_poetry


@click.group()
def install():
    """Install sub command group.

    :return:
    """
    pass


install.add_command(install_poetry)
install.add_command(install_backend_dependencies)


@click.group()
def update():
    """Update sub command group.

    :return:
    """
    pass


update.add_command(update_poetry)
update.add_command(update_backend_dependencies)


@click.group()
def export():
    """Update sub command group.

    :return:
    """
    pass


export.add_command(backend_api_specs)