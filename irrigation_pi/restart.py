"""Restart commands."""

# ruff: noqa: D205, D301, D400

import click

from irrigation_pi.utils import run_subprocess


@click.command(name="uvicorn")
def restart_uvicorn() -> None:
    """Restart Uvicorn server.
    \f
    :return:
    """
    click.echo("Restarting Uvicorn server...")
    run_subprocess(["sudo", "systemctl", "stop", "irrigation-pi"])
    run_subprocess(["sudo", "systemctl", "start", "irrigation-pi"])


@click.command(name="nginx")
def restart_nginx() -> None:
    """Restart nginx server.
    \f
    :return:
    """
    click.echo("Restarting nginx server...")
    run_subprocess(["sudo", "systemctl", "restart", "nginx"])
