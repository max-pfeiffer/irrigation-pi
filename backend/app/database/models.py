"""Database models."""
from datetime import time
from typing import Optional

from sqlmodel import Field, SQLModel

from app.scheduling import Repeat


class BaseModel(SQLModel):
    """Base model."""

    id: Optional[int] = Field(default=None, primary_key=True)


class Schedule(BaseModel, table=True):
    """Schedule."""

    start_time: time
    duration: int
    repeat: Repeat
    active: bool
