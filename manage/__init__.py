"""A management CLI inspired by Django's manage.py command."""

import click

from manage.groups import export, install, run, update


@click.group()
def cli():
    """Command line interface entrypoint.

    :return:
    """
    pass


cli.add_command(install)
cli.add_command(update)
cli.add_command(run)
cli.add_command(export)
