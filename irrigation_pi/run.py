"""Export commands."""

# ruff: noqa: D205, D301, D400

import click

from irrigation_pi.constants import (
    BACKEND_PATH,
    FRONTEND_PATH,
    VIRTUAL_ENVIRONMENT_PATH,
)
from irrigation_pi.utils import (
    activate_virtual_environment,
    run_subprocess,
)


@click.command()
def backend():
    """Run backend application.
    \f
    :return:
    """
    click.echo("Running backend application...")
    env: dict = activate_virtual_environment(VIRTUAL_ENVIRONMENT_PATH)
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
        cwd=BACKEND_PATH,
        env=env,
    )


@click.command()
def frontend():
    """Run frontend application.
    \f
    :return:
    """
    click.echo("Running frontend application...")
    run_subprocess(
        [
            "ionic",
            "serve",
        ],
        cwd=FRONTEND_PATH,
    )
