"""Export commands."""
from pathlib import Path

import click

from manage.utils import (
    PROJECT_ROOT_PATH,
    activate_virtual_environment,
    run_subprocess,
)


@click.command()
def backend_api_specs():
    """Export backend API specification.

    :return:
    """
    backend_path: Path = PROJECT_ROOT_PATH / "backend"
    virtual_environment_path: Path = PROJECT_ROOT_PATH / "backend" / ".venv"
    env: dict = activate_virtual_environment(virtual_environment_path)
    run_subprocess(
        ["python", "-m", "utilities.export_api_specification"],
        cwd=backend_path,
        env=env,
    )
