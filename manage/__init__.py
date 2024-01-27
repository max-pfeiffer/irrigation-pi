"""Project management."""

import click

from manage.groups import export, install, update


@click.group()
def cli():
    """Command line interface entrypoint.

    :return:
    """
    pass


cli.add_command(install)
cli.add_command(update)
cli.add_command(export)
