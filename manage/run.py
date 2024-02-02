"""Export commands."""
from pathlib import Path

import click

from manage.utils import (
    PROJECT_ROOT_PATH,
    activate_virtual_environment,
    run_subprocess,
)


@click.command()
def backend():
    """Run backend application.

    :return:
    """
    backend_path: Path = PROJECT_ROOT_PATH / "backend"
    virtual_environment_path: Path = PROJECT_ROOT_PATH / ".venv"
    env: dict = activate_virtual_environment(virtual_environment_path)
    run_subprocess(
        [
            "uvicorn",
            "--workers",
            "1",
            "--host",
            "0.0.0.0",
            "--port",
            "8000",
            "app.main:app",
        ],
        cwd=backend_path,
        env=env,
    )
