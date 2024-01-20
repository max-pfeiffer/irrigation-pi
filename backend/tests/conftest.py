import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    from app.main import app

    return TestClient(app)
