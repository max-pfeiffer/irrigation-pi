"""API models."""
from datetime import time
from typing import Union

from pydantic import BaseModel, Field, PositiveInt

from app.adapters import RelayBoardType
from app.scheduling import Repeat


class ScheduleResponse(BaseModel):
    """Response schema for schedule."""

    id: PositiveInt = Field(description="Primary key")
    start_time: time = Field(description="Start time of the schedule")
    duration: PositiveInt = Field(description="Duration in minutes")
    repeat: Repeat = Field(description="Specifies how the schedule is repeated")
    active: bool = Field(description="Whether the schedule is active")
    relay_board_type: RelayBoardType = Field(description="Type of the relay board")
    relay_position: PositiveInt = Field(description="Position of the relay")


class ScheduleCreate(BaseModel):
    """Creation schema for schedule."""

    start_time: time = Field(description="Start time of the schedule")
    duration: PositiveInt = Field(description="Duration in minutes")
    repeat: Repeat = Field(description="Specifies how the schedule is repeated")
    active: bool = Field(default=True, description="Whether the schedule is active")
    relay_board_type: RelayBoardType = Field(description="Type of the relay board")
    relay_position: PositiveInt = Field(description="Position of the relay")


class ScheduleUpdate(BaseModel):
    """Update schema for schedule."""

    start_time: Union[time, None] = Field(
        default=None, description="Start time of the schedule"
    )
    duration: Union[PositiveInt, None] = Field(
        default=None, description="Duration in minutes"
    )
    repeat: Union[Repeat, None] = Field(
        default=None, description="Specifies how the schedule is repeated"
    )
    active: Union[bool, None] = Field(
        default=None, description="Whether the schedule is active"
    )
    relay_board_type: Union[RelayBoardType, None] = Field(
        default=None, description="Type of the relay board"
    )
    relay_position: Union[PositiveInt, None] = Field(
        default=None, description="Position of the relay"
    )
