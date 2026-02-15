"""Configure commands."""

import json

import click

from irrigation_pi.constants import FRONTEND_PATH_HOSTNAME_CONFIGURATION_PATH
from irrigation_pi.utils import create_frontend_hostname_configuration


@click.command(name="hostname")
def frontend_hostname():
    """Configure current systems hostname for frontend application.

    :return:
    """
    click.echo("Configuring hostname for frontend application...")
    with open(FRONTEND_PATH_HOSTNAME_CONFIGURATION_PATH, "w") as file:
        json.dump(create_frontend_hostname_configuration(), file)
