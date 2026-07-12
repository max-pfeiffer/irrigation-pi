"""Tests for API root."""

from subprocess import CompletedProcess

import pytest
from fastapi.testclient import TestClient
from httpx import Response
from starlette import status

import app.services.system_date_time

TEST_DATA: list[dict] = [
    {
        "path": "/",
        "method": "get",
        "data": None,
    },
    {
        "path": "/v1/schedule",
        "method": "get",
        "data": None,
    },
    {
        "path": "/v1/schedule",
        "method": "post",
        "data": {
            "start_time": "23:46:58.338Z",
            "duration": 10,
            "repeat": "every_day",
            "active": True,
            "relay_board_type": "waveshare_rpi_relay_board",
            "relay_position": 1,
        },
    },
    {
        "path": "/v1/schedule/1",
        "method": "get",
        "data": None,
    },
    {
        "path": "/v1/schedule/1",
        "method": "put",
        "data": {"relay_position": 3},
    },
    {
        "path": "/v1/schedule/1",
        "method": "delete",
        "data": None,
    },
    {
        "path": "/v1/relay",
        "method": "get",
        "data": None,
    },
    {
        "path": "/v1/relay/1",
        "method": "get",
        "data": None,
    },
    {
        "path": "/v1/relay/1",
        "method": "put",
        "data": {"position": 1, "on": True},
    },
    {
        "path": "/v1/info",
        "method": "get",
        "data": None,
    },
    {
        "path": "/v1/system-date-time",
        "method": "get",
        "data": None,
    },
    {
        "path": "/v1/system-date-time",
        "method": "put",
        "data": {"date_time": "2026-07-12T14:30:00+02:00"},
    },
]


def fake_subprocess_run(command: list[str], **kwargs) -> CompletedProcess:
    """Fake subprocess.run so no timedatectl command is executed locally.

    :param command:
    :return:
    """
    stdout: str = "yes\n" if "show" in command else ""
    return CompletedProcess(args=command, returncode=0, stdout=stdout, stderr="")


@pytest.mark.parametrize("test_data", TEST_DATA)
def test_all_api_endpoints(test_client: TestClient, test_data: dict, monkeypatch):
    """Test API endpoints."""
    monkeypatch.setattr(
        app.services.system_date_time.subprocess, "run", fake_subprocess_run
    )
    method: str = test_data["method"]
    path: str = test_data["path"]
    data: str = test_data["data"]
    headers: dict = {
        "Origin": "http://localhost:8100",
    }
    if method == "get":
        response: Response = test_client.get(path, headers=headers)
    elif method == "post":
        response: Response = test_client.post(path, headers=headers, json=data)
    elif method == "put":
        response: Response = test_client.put(path, headers=headers, json=data)
    elif method == "delete":
        response: Response = test_client.delete(path, headers=headers)
    else:
        raise Exception("Unknown HTTP method")

    assert response.status_code == status.HTTP_200_OK
    assert response.headers["access-control-allow-origin"] == "http://localhost:8100"
