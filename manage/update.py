"""Update commands."""

import click

from manage.utils import (
    BACKEND_PATH,
    BACKEND_VIRTUAL_ENVIRONMENT_PATH,
    activate_virtual_environment,
    execute_command,
)


@click.command(name="poetry")
def update_poetry():
    """Update Poetry installation.

    :return:
    """
    execute_command(["poetry", "self", "update"])


@click.command(name="backend-dependencies")
def update_backend_dependencies():
    """Update backend dependencies.

    :return:
    """
    env: dict = activate_virtual_environment(BACKEND_VIRTUAL_ENVIRONMENT_PATH)
    execute_command(["poetry", "update"], cwd=BACKEND_PATH, env=env)
