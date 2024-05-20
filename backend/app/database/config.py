"""Database configuration."""

from sqlalchemy import Engine
from sqlmodel import Session, create_engine

from app.config import application_settings

database_engine: Engine = create_engine(
    application_settings.database_uri, connect_args={"check_same_thread": False}
)


def get_session() -> Session:
    """Create and yield a database session.

    :return:
    """
    with Session(database_engine) as session:
        yield session
