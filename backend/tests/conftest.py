"""Test fixtures."""

from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from app.config import application_settings
from fastapi.testclient import TestClient
from pytest import MonkeyPatch


@pytest.fixture(scope="session")
def monkeypatch_session() -> MonkeyPatch:
    """MonkeyPatch session fixture.

    :return:
    """
    with MonkeyPatch.context() as mp:
        yield mp


@pytest.fixture(scope="session")
def api_test_database(monkeypatch_session: MonkeyPatch):
    """Create a test database."""
    database_name: str = "api_test"
    monkeypatch_session.setenv("database_name", database_name)
    monkeypatch_session.setattr(application_settings, "database_name", database_name)

    # Apply migrations
    migrations_path: Path = Path(__file__).parent.parent.resolve() / "migrations"
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", str(migrations_path))
    command.upgrade(alembic_cfg, "head")

    yield database_name

    database_path: Path = (
        Path(__file__).parent.parent.resolve() / "sqlite_db" / f"{database_name}.db"
    )
    if database_path.exists():
        database_path.unlink()


@pytest.fixture(scope="session")
def test_client(api_test_database: str) -> TestClient:
    """Provides test client for API tests."""
    from app.main import app

    with TestClient(app) as client:
        yield client
