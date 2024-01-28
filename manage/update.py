"""Update commands."""

import click

from manage.utils import (
    BACKEND_PATH,
    BACKEND_VIRTUAL_ENVIRONMENT_PATH,
    activate_virtual_environment,
    run_subprocess,
)


@click.command(name="poetry")
def update_poetry():
    """Update Poetry installation.

    :return:
    """
    run_subprocess(["poetry", "self", "update"])


@click.command(name="backend-dependencies")
def update_backend_dependencies():
    """Update backend dependencies.

    :return:
    """
    env: dict = activate_virtual_environment(BACKEND_VIRTUAL_ENVIRONMENT_PATH)
    run_subprocess(["poetry", "update", "--no-interaction"], cwd=BACKEND_PATH, env=env)
