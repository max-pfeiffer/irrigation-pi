"""Tests for system date and time API endpoints."""

from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import Response
from starlette import status

from app.api.v1.endpoints.system_date_time import router
from app.exceptions import SystemDateTimeError


@pytest.fixture
def endpoint_test_client() -> TestClient:
    """Provide a test client for the system date and time endpoints.

    Mounts only the system date and time router so no database or
    scheduler lifespan is needed.

    :return:
    """
    app: FastAPI = FastAPI()
    app.include_router(router, prefix="/system-date-time")
    app.state.scheduler = MagicMock()
    return TestClient(app)


def test_get_system_date_time(endpoint_test_client: TestClient) -> None:
    """Test getting the system date and time in ISO 8601 format."""
    date_time: datetime = datetime(
        2026, 7, 12, 14, 30, 0, tzinfo=timezone(timedelta(hours=2))
    )

    with patch(
        "app.api.v1.endpoints.system_date_time.service_get_system_date_time",
        return_value=date_time,
    ):
        response: Response = endpoint_test_client.get("/system-date-time/")

    assert response.status_code == status.HTTP_200_OK
    response_date_time: datetime = datetime.fromisoformat(response.json()["date_time"])
    assert response_date_time.tzinfo is not None
    assert response_date_time == date_time


def test_set_system_date_time(endpoint_test_client: TestClient) -> None:
    """Test setting the system date and time from ISO 8601 input."""
    with patch(
        "app.api.v1.endpoints.system_date_time.service_set_system_date_time"
    ) as service_mock:
        response: Response = endpoint_test_client.put(
            "/system-date-time/",
            json={"date_time": "2026-07-12T14:30:00+02:00"},
        )

    assert response.status_code == status.HTTP_200_OK
    service_mock.assert_called_once_with(
        datetime(2026, 7, 12, 14, 30, 0, tzinfo=timezone(timedelta(hours=2))),
        endpoint_test_client.app.state.scheduler,
    )


def test_set_system_date_time_naive_datetime(
    endpoint_test_client: TestClient,
) -> None:
    """Test that a naive datetime is rejected with a validation error."""
    with patch(
        "app.api.v1.endpoints.system_date_time.service_set_system_date_time"
    ) as service_mock:
        response: Response = endpoint_test_client.put(
            "/system-date-time/",
            json={"date_time": "2026-07-12T14:30:00"},
        )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
    service_mock.assert_not_called()


def test_set_system_date_time_invalid_input(
    endpoint_test_client: TestClient,
) -> None:
    """Test that a non-datetime input is rejected with a validation error."""
    with patch(
        "app.api.v1.endpoints.system_date_time.service_set_system_date_time"
    ) as service_mock:
        response: Response = endpoint_test_client.put(
            "/system-date-time/",
            json={"date_time": "not a datetime"},
        )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
    service_mock.assert_not_called()


def test_set_system_date_time_service_failure(
    endpoint_test_client: TestClient,
) -> None:
    """Test that a service failure results in a 500 response."""
    with patch(
        "app.api.v1.endpoints.system_date_time.service_set_system_date_time",
        side_effect=SystemDateTimeError("timedatectl failed"),
    ):
        response: Response = endpoint_test_client.put(
            "/system-date-time/",
            json={"date_time": "2026-07-12T14:30:00+02:00"},
        )

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json()["detail"] == "timedatectl failed"
