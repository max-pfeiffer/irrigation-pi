"""Export commands."""

import click

from manage.utils import (
    BACKEND_PATH,
    VIRTUAL_ENVIRONMENT_PATH,
    activate_virtual_environment,
    run_subprocess,
)


@click.command()
def backend():
    """Run backend application.

    :return:
    """
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
