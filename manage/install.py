"""Install commands."""
from pathlib import Path

import click

from manage.utils import (
    PROJECT_ROOT_PATH,
    activate_virtual_environment,
    execute_command,
)


@click.command(name="poetry")
def install_poetry():
    """Execute poetry installation.

    :return:
    """
    execute_command(["poetry", "--version"])


@click.command(name="backend-dependencies")
def install_backend_dependencies():
    """Execute backend installation.

    :return:
    """
    backend_path: Path = PROJECT_ROOT_PATH / "backend"
    virtual_environment_path: Path = PROJECT_ROOT_PATH / "backend" / ".venv"
    env: dict = activate_virtual_environment(virtual_environment_path)
    execute_command(["poetry", "install"], cwd=backend_path, env=env)
