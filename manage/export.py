"""Export commands."""

import click

from manage.utils import (
    BACKEND_PATH,
    VIRTUAL_ENVIRONMENT_PATH,
    activate_virtual_environment,
    run_subprocess,
)


@click.command(name="backend-api-specs")
def backend_api_specs():
    """Export backend API specification.

    :return:
    """
    env: dict = activate_virtual_environment(VIRTUAL_ENVIRONMENT_PATH)
    run_subprocess(
        ["python", "-m", "utilities.export_api_specification"],
        cwd=BACKEND_PATH,
        env=env,
    )
