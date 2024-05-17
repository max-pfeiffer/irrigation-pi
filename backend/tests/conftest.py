"""Test fixtures."""

from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from app.config import application_settings
from fastapi.testclient import TestClient
from pytest import MonkeyPatch
from sqlmodel import Session


@pytest.fixture(scope="package")
def api_test_database() -> str:
    """Create a test database."""
    with MonkeyPatch.context() as mp:
        database_name: str = "api_test"
        mp.setenv("database_name", database_name)
        mp.setattr(application_settings, "database_name", database_name)

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


@pytest.fixture(scope="package")
def test_client(api_test_database: str) -> TestClient:
    """Provides test client for API tests."""
    from app.main import app

    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="package")
def integration_test_database_session() -> Session:
    """Create a test database for integration tests."""
    with MonkeyPatch.context() as mp:
        database_name: str = "integration_test"
        mp.setenv("database_name", database_name)
        mp.setattr(application_settings, "database_name", database_name)

        # Apply migrations
        migrations_path: Path = Path(__file__).parent.parent.resolve() / "migrations"
        alembic_cfg = Config()
        alembic_cfg.set_main_option("script_location", str(migrations_path))
        command.upgrade(alembic_cfg, "head")

        from app.database.config import get_session

        database_session_generator = get_session()

        yield next(database_session_generator)

        database_path: Path = (
            Path(__file__).parent.parent.resolve() / "sqlite_db" / f"{database_name}.db"
        )
        if database_path.exists():
            database_path.unlink()
