"""Database models."""

from datetime import time
from typing import Optional

from pydantic import PositiveInt
from sqlmodel import Field, SQLModel

from app.scheduling import Repeat


class BaseModel(SQLModel):
    """Base model."""

    id: Optional[int] = Field(default=None, primary_key=True)


class Schedule(BaseModel, table=True):
    """Schedule."""

    start_time: time
    stop_time: time
    duration: PositiveInt
    repeat: Repeat
    active: bool
    relay_position: PositiveInt
    start_job_id: Optional[str]
    stop_job_id: Optional[str]
