"""Utility functions."""
import os
import sys
from pathlib import Path
from subprocess import PIPE, Popen
from typing import Optional

import click

PROJECT_ROOT_PATH: Path = Path(__file__).parent.parent.resolve()
BACKEND_PATH: Path = PROJECT_ROOT_PATH / "backend"
BACKEND_VIRTUAL_ENVIRONMENT_PATH: Path = PROJECT_ROOT_PATH / "backend" / ".venv"


def run_subprocess(
    command: list[str], cwd: Optional[Path] = None, env: Optional[dict] = None
):
    """Execute command with Popen and prints it's output.

    :param command:
    :param cwd:
    :param env:
    :return:
    """
    with Popen(
        command, cwd=cwd, env=env, stdout=PIPE, bufsize=1, universal_newlines=True
    ) as cp:
        for line in cp.stdout:
            click.echo(line)


def activate_virtual_environment(virtual_environment_path: Path) -> dict:
    """Provide environment variable for activating a virtual environment.

    :param virtual_environment_path:
    :param virtual_environment_binary_path:
    :return:
    """
    virtual_environment_binary_path: Path = virtual_environment_path / "bin"

    # Acquiring system environment variables
    environment_variables: dict = os.environ.copy()

    # "Deactivate" the old and "activate" the new virtual environment: strip the current
    # virtual environment path and add the new virtual environment path.
    # See: https://docs.python.org/3/library/venv.html#how-venvs-work
    paths: list[str] = environment_variables["PATH"].split(os.pathsep)

    if sys.prefix != sys.base_prefix:
        old_virtual_environment_binary_path: str = f"{sys.prefix}/bin"
        paths: list[str] = [
            item for item in paths if item != old_virtual_environment_binary_path
        ]

    paths.insert(0, str(virtual_environment_binary_path))
    environment_variables["PATH"] = os.pathsep.join(paths)

    # Pointing VIRTUAL_ENV to the new virtual environment
    environment_variables["VIRTUAL_ENV"] = str(virtual_environment_path)

    # Configuring Poetry to put the virtual environment in project directory
    environment_variables["POETRY_VIRTUALENVS_IN_PROJECT"] = "true"

    return environment_variables
