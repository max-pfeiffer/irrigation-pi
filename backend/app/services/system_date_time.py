"""Services for system date and time."""

import subprocess
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.exceptions import SystemDateTimeError

SUBPROCESS_TIMEOUT: int = 10


def service_get_system_date_time() -> datetime:
    """Service for reading system date and time.

    :return: timezone aware datetime object in the system's local timezone
    """
    system_date_time: datetime = datetime.now().astimezone()
    return system_date_time


def _run_command(command: list[str]) -> str:
    """Run a command and return its standard output.

    :param command:
    :raises SystemDateTimeError: if the command fails or times out
    :return: standard output of the command
    """
    try:
        completed_process: subprocess.CompletedProcess = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            timeout=SUBPROCESS_TIMEOUT,
        )
    except subprocess.CalledProcessError as error:
        raise SystemDateTimeError(
            f"{' '.join(command)} failed: {error.stderr.strip()}"
        ) from error
    except subprocess.TimeoutExpired as error:
        raise SystemDateTimeError(f"{' '.join(command)} timed out") from error
    return completed_process.stdout


def _ntp_enabled() -> bool:
    """Read whether NTP synchronization is currently enabled.

    :raises SystemDateTimeError: if reading the NTP state fails
    :return:
    """
    output: str = _run_command(["timedatectl", "show", "--property=NTP", "--value"])
    return output.strip() == "yes"


def service_set_system_date_time(
    date_time: datetime, scheduler: AsyncIOScheduler | None = None
) -> None:
    """Service for setting system date and time on a Debian Linux system.

    Disables NTP synchronization first because timedatectl refuses to set
    the time while it is active. NTP stays disabled on success because it
    would immediately overwrite the manually set time; if setting the time
    fails, the previous NTP state is restored. Sub-second precision is
    dropped. During the repeated hour at the end of daylight saving time
    the local wall-clock time is ambiguous and timedatectl picks one
    interpretation.

    Requires passwordless sudo for timedatectl for the application user.

    :param date_time: timezone aware datetime object
    :param scheduler: optional scheduler which gets woken up after the time
        change so it recalculates its job wait times
    :raises ValueError: if date_time is naive or outside the years 2000-2100
    :raises SystemDateTimeError: if a timedatectl call fails or times out
    :return:
    """
    if date_time.tzinfo is None:
        raise ValueError("date_time must be timezone aware")

    local_date_time: datetime = date_time.astimezone()
    if not 2000 <= local_date_time.year <= 2100:
        raise ValueError("date_time year must be between 2000 and 2100")
    formatted_date_time: str = local_date_time.strftime("%Y-%m-%d %H:%M:%S")

    ntp_was_enabled: bool = _ntp_enabled()
    _run_command(["sudo", "-n", "timedatectl", "set-ntp", "false"])
    try:
        _run_command(["sudo", "-n", "timedatectl", "set-time", formatted_date_time])
    except SystemDateTimeError:
        if ntp_was_enabled:
            _run_command(["sudo", "-n", "timedatectl", "set-ntp", "true"])
        raise

    if scheduler is not None:
        scheduler.wakeup()
