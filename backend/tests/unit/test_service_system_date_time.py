"""Tests for service system date and time."""

import subprocess
from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest

from app.exceptions import SystemDateTimeError
from app.services.system_date_time import (
    service_get_system_date_time,
    service_set_system_date_time,
)

SHOW_NTP_COMMAND: list[str] = ["timedatectl", "show", "--property=NTP", "--value"]
SET_NTP_FALSE_COMMAND: list[str] = ["sudo", "-n", "timedatectl", "set-ntp", "false"]
SET_NTP_TRUE_COMMAND: list[str] = ["sudo", "-n", "timedatectl", "set-ntp", "true"]


def make_run_side_effect(ntp_enabled: bool, set_time_error: Exception | None = None):
    """Create a subprocess.run side effect simulating timedatectl.

    :param ntp_enabled: reported NTP state
    :param set_time_error: exception raised by the set-time call
    :return:
    """

    def run_side_effect(command: list[str], **kwargs) -> subprocess.CompletedProcess:
        stdout: str = ""
        if command == SHOW_NTP_COMMAND:
            stdout = "yes\n" if ntp_enabled else "no\n"
        if "set-time" in command and set_time_error is not None:
            raise set_time_error
        return subprocess.CompletedProcess(
            args=command, returncode=0, stdout=stdout, stderr=""
        )

    return run_side_effect


def test_service_get_system_date_time() -> None:
    """Test reading the system date and time."""
    date_time: datetime = service_get_system_date_time()

    assert date_time.tzinfo is not None
    assert date_time.utcoffset() is not None


def test_service_set_system_date_time() -> None:
    """Test setting the system date and time."""
    date_time: datetime = datetime(2026, 7, 12, 12, 30, 0, tzinfo=UTC)
    expected_time: str = date_time.astimezone().strftime("%Y-%m-%d %H:%M:%S")

    with patch(
        "app.services.system_date_time.subprocess.run",
        side_effect=make_run_side_effect(ntp_enabled=True),
    ) as run_mock:
        service_set_system_date_time(date_time)

    commands: list[list[str]] = [c.args[0] for c in run_mock.call_args_list]
    assert commands == [
        SHOW_NTP_COMMAND,
        SET_NTP_FALSE_COMMAND,
        ["sudo", "-n", "timedatectl", "set-time", expected_time],
    ]


def test_service_set_system_date_time_naive_datetime() -> None:
    """Test that a naive datetime is rejected."""
    with patch("app.services.system_date_time.subprocess.run") as run_mock:
        with pytest.raises(ValueError, match="timezone aware"):
            service_set_system_date_time(datetime(2026, 7, 12, 12, 30, 0))

    run_mock.assert_not_called()


def test_service_set_system_date_time_failure_restores_ntp() -> None:
    """Test that the previous NTP state is restored when set-time fails."""
    date_time: datetime = datetime(2026, 7, 12, 12, 30, 0, tzinfo=UTC)
    set_time_error = subprocess.CalledProcessError(
        returncode=1, cmd=["timedatectl"], stderr="Failed to set time"
    )

    with patch(
        "app.services.system_date_time.subprocess.run",
        side_effect=make_run_side_effect(
            ntp_enabled=True, set_time_error=set_time_error
        ),
    ) as run_mock:
        with pytest.raises(SystemDateTimeError) as exception_info:
            service_set_system_date_time(date_time)

    commands: list[list[str]] = [c.args[0] for c in run_mock.call_args_list]
    assert commands[-1] == SET_NTP_TRUE_COMMAND
    assert "Failed to set time" in exception_info.value.detail


def test_service_set_system_date_time_failure_keeps_ntp_disabled() -> None:
    """Test that NTP is not re-enabled when it was disabled before."""
    date_time: datetime = datetime(2026, 7, 12, 12, 30, 0, tzinfo=UTC)
    set_time_error = subprocess.CalledProcessError(
        returncode=1, cmd=["timedatectl"], stderr="Failed to set time"
    )

    with patch(
        "app.services.system_date_time.subprocess.run",
        side_effect=make_run_side_effect(
            ntp_enabled=False, set_time_error=set_time_error
        ),
    ) as run_mock:
        with pytest.raises(SystemDateTimeError):
            service_set_system_date_time(date_time)

    commands: list[list[str]] = [c.args[0] for c in run_mock.call_args_list]
    assert SET_NTP_TRUE_COMMAND not in commands


def test_service_set_system_date_time_timeout() -> None:
    """Test that a hanging timedatectl call raises SystemDateTimeError."""
    date_time: datetime = datetime(2026, 7, 12, 12, 30, 0, tzinfo=UTC)
    set_time_error = subprocess.TimeoutExpired(cmd=["timedatectl"], timeout=10)

    with patch(
        "app.services.system_date_time.subprocess.run",
        side_effect=make_run_side_effect(
            ntp_enabled=False, set_time_error=set_time_error
        ),
    ):
        with pytest.raises(SystemDateTimeError, match="timed out"):
            service_set_system_date_time(date_time)


def test_service_set_system_date_time_wakes_up_scheduler() -> None:
    """Test that the scheduler is woken up after a successful time change."""
    date_time: datetime = datetime(2026, 7, 12, 12, 30, 0, tzinfo=UTC)
    scheduler: MagicMock = MagicMock()

    with patch(
        "app.services.system_date_time.subprocess.run",
        side_effect=make_run_side_effect(ntp_enabled=True),
    ):
        service_set_system_date_time(date_time, scheduler=scheduler)

    scheduler.wakeup.assert_called_once()


def test_service_set_system_date_time_no_scheduler_wakeup_on_failure() -> None:
    """Test that the scheduler is not woken up when setting the time fails."""
    date_time: datetime = datetime(2026, 7, 12, 12, 30, 0, tzinfo=UTC)
    scheduler: MagicMock = MagicMock()
    set_time_error = subprocess.CalledProcessError(
        returncode=1, cmd=["timedatectl"], stderr="Failed to set time"
    )

    with patch(
        "app.services.system_date_time.subprocess.run",
        side_effect=make_run_side_effect(
            ntp_enabled=True, set_time_error=set_time_error
        ),
    ):
        with pytest.raises(SystemDateTimeError):
            service_set_system_date_time(date_time, scheduler=scheduler)

    scheduler.wakeup.assert_not_called()
