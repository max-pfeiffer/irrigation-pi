"""Test fixtures."""
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    """Provides test client for API tests."""
    from app.main import app

    return TestClient(app)
