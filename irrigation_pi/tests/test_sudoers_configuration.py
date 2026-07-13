"""Tests for installing and uninstalling the sudoers configuration."""

import stat
import subprocess
from importlib import import_module
from pathlib import Path

import pytest
from click.testing import CliRunner, Result

from irrigation_pi.constants import APPLICATION_USER
from irrigation_pi.install import install_sudoers_configuration
from irrigation_pi.uninstall import uninstall_sudoers_configuration
from irrigation_pi.utils import create_sudoers_config

# The irrigation_pi package binds click groups named "install" and
# "uninstall" as package attributes, shadowing the modules of the same
# name, so the modules must be resolved explicitly for monkeypatching.
install_module = import_module("irrigation_pi.install")
uninstall_module = import_module("irrigation_pi.uninstall")


@pytest.fixture
def sudoers_config_path(tmp_path: Path, monkeypatch) -> Path:
    """Redirect the sudoers configuration path into a temporary directory.

    :param tmp_path:
    :param monkeypatch:
    :return: patched sudoers configuration path
    """
    path: Path = tmp_path / "irrigation-pi"
    monkeypatch.setattr(install_module, "SUDOERS_CONFIG_PATH", path)
    monkeypatch.setattr(uninstall_module, "SUDOERS_CONFIG_PATH", path)
    return path


@pytest.fixture
def visudo_calls(monkeypatch) -> list[list[str]]:
    """Replace subprocess.run in the install module with a successful fake.

    :param monkeypatch:
    :return: list which records the commands passed to subprocess.run
    """
    calls: list[list[str]] = []

    def fake_run(command: list[str], *args, **kwargs) -> subprocess.CompletedProcess:
        calls.append(command)
        return subprocess.CompletedProcess(command, returncode=0)

    monkeypatch.setattr(install_module.subprocess, "run", fake_run)
    return calls


def test_install_sudoers_configuration(
    sudoers_config_path: Path, visudo_calls: list[list[str]]
):
    """Test installing the sudoers configuration.

    :param sudoers_config_path:
    :param visudo_calls:
    :return:
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(install_sudoers_configuration)

    assert result.exit_code == 0
    assert sudoers_config_path.read_text() == create_sudoers_config(APPLICATION_USER)
    assert stat.S_IMODE(sudoers_config_path.stat().st_mode) == 0o440

    # The configuration must be validated with visudo at the temporary path
    # before it is renamed into place
    temporary_path: Path = sudoers_config_path.with_name(
        f"{sudoers_config_path.name}.tmp"
    )
    assert visudo_calls == [["sudo", "visudo", "-cf", str(temporary_path)]]
    assert not temporary_path.exists()


def test_install_sudoers_configuration_invalid(sudoers_config_path: Path, monkeypatch):
    """Test that an invalid sudoers configuration is not installed.

    :param sudoers_config_path:
    :param monkeypatch:
    :return:
    """

    def fake_run(command: list[str], *args, **kwargs) -> subprocess.CompletedProcess:
        return subprocess.CompletedProcess(command, returncode=1)

    monkeypatch.setattr(install_module.subprocess, "run", fake_run)

    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(install_sudoers_configuration)

    assert result.exit_code != 0
    assert "Invalid sudoers configuration" in result.output
    assert not sudoers_config_path.exists()
    assert not sudoers_config_path.with_name(f"{sudoers_config_path.name}.tmp").exists()


def test_uninstall_sudoers_configuration(sudoers_config_path: Path):
    """Test uninstalling the sudoers configuration.

    :param sudoers_config_path:
    :return:
    """
    sudoers_config_path.write_text("content")

    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(uninstall_sudoers_configuration)

    assert result.exit_code == 0
    assert not sudoers_config_path.exists()


def test_uninstall_sudoers_configuration_missing_file(sudoers_config_path: Path):
    """Test uninstalling when no sudoers configuration is installed.

    :param sudoers_config_path:
    :return:
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(uninstall_sudoers_configuration)

    assert result.exit_code == 0
