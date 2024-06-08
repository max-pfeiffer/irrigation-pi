"""A management CLI inspired by Django's manage.py command."""

# ruff: noqa: D205, D301, D400

import click

from irrigation_pi.groups import export, install, restart, run, uninstall


@click.group()
def cli():
    """Irrigation Pi command line interface (CLI).

    CLI provides common operations for configuring and running the application.

    Run 'irrigation-pi COMMAND --help' for more information about commands and usage.
    \f

    :return:
    """
    pass


cli.add_command(install)
cli.add_command(uninstall)
cli.add_command(run)
cli.add_command(restart)
cli.add_command(export)
