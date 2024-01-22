"""Tests for API root."""
from fastapi.testclient import TestClient
from httpx import Response
from starlette import status


def test_root(test_client: TestClient):
    """Test API root."""
    response: Response = test_client.get("/")

    assert response.status_code == status.HTTP_200_OK
