"""Database models."""
from datetime import time
from typing import Optional

from pydantic import PositiveInt
from sqlmodel import Field, SQLModel

from app.adapters import RelayBoardType
from app.scheduling import Repeat


class BaseModel(SQLModel):
    """Base model."""

    id: Optional[int] = Field(default=None, primary_key=True)


class Schedule(BaseModel, table=True):
    """Schedule."""

    start_time: time
    duration: PositiveInt
    repeat: Repeat
    active: bool
    relay_board_type: RelayBoardType
    relay_position: PositiveInt
    start_schedule_id: Optional[str]
    stop_schedule_id: Optional[str]
