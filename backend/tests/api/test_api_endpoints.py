"""Tests for API root."""
import pytest
from app.api.v1.endpoints import schedule
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi.testclient import TestClient
from httpx import Response
from starlette import status

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
            "start_time": "17:46:58.338Z",
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
        "data": {"active": False},
    },
    {
        "path": "/v1/schedule/1",
        "method": "delete",
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
]


@pytest.mark.parametrize("test_data", TEST_DATA)
def test_root_options(test_client: TestClient, test_data: dict, monkeypatch):
    """Test API endpoints."""

    def fake_service_update_schedule(scheduler: AsyncIOScheduler, **kwargs):
        """Fake service function.

        :param scheduler:
        :param kwargs:
        :return:
        """
        pass

    def fake_service_delete_schedule(scheduler: AsyncIOScheduler, primary_key: int):
        """Fake service function.

        :param scheduler:
        :param primary_key:
        :return:
        """
        pass

    monkeypatch.setattr(
        schedule, "service_update_schedule", fake_service_update_schedule
    )
    monkeypatch.setattr(
        schedule, "service_delete_schedule", fake_service_delete_schedule
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
