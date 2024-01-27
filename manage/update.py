"""Update commands."""
from pathlib import Path

import click

from manage.utils import (
    PROJECT_ROOT_PATH,
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
    """Update backend installation.

    :return:
    """
    backend_path: Path = PROJECT_ROOT_PATH / "backend"
    virtual_environment_path: Path = PROJECT_ROOT_PATH / "backend" / ".venv"
    env: dict = activate_virtual_environment(virtual_environment_path)
    execute_command(["poetry", "update"], cwd=backend_path, env=env)
