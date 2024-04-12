"""Database configuration."""

from sqlalchemy import Engine
from sqlmodel import create_engine

from app.config import application_settings

database_engine: Engine = create_engine(application_settings.database_uri)
