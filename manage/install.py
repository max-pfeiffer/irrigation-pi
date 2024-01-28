"""Install commands."""

import click

from manage.utils import (
    BACKEND_PATH,
    BACKEND_VIRTUAL_ENVIRONMENT_PATH,
    activate_virtual_environment,
    execute_command,
)


@click.command(name="poetry")
def install_poetry():
    """Install Poetry.

    :return:
    """
    execute_command(
        ["curl", "-sSL", "https://install.python-poetry.org", "|", "python3", "-"]
    )


@click.command(name="backend-dependencies")
def install_backend_dependencies():
    """Install backend dependencies.

    :return:
    """
    env: dict = activate_virtual_environment(BACKEND_VIRTUAL_ENVIRONMENT_PATH)
    execute_command(["poetry", "install"], cwd=BACKEND_PATH, env=env)


@click.command(name="backend-database")
def install_backend_database():
    """Install backend database.

    :return:
    """
    env: dict = activate_virtual_environment(BACKEND_VIRTUAL_ENVIRONMENT_PATH)
    execute_command(["alembic", "upgrade", "head"], cwd=BACKEND_PATH, env=env)
