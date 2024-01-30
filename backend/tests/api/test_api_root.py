"""Tests for API root."""

from fastapi.testclient import TestClient
from httpx import Response
from starlette import status


def test_root(test_client: TestClient):
    """Test API root."""
    response: Response = test_client.get("/")

    assert response.status_code == status.HTTP_200_OK


def test_root_options(test_client: TestClient):
    """Test API root."""
    headers: dict = {
        "Origin": "http://localhost:8100",
    }
    response: Response = test_client.get("/", headers=headers)

    assert response.status_code == status.HTTP_200_OK
    assert response.headers["access-control-allow-origin"] == "http://localhost:8100"
