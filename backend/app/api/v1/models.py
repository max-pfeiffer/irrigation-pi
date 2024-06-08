"""API models."""

from datetime import time
from typing import Union

from pydantic import BaseModel, Field, PositiveInt

from app.scheduling import Repeat


class ScheduleResponse(BaseModel):
    """Response schema for schedule."""

    id: PositiveInt = Field(description="Primary key")
    start_time: time = Field(description="Start time of the schedule")
    duration: PositiveInt = Field(description="Duration in minutes")
    repeat: Repeat = Field(description="Specifies how the schedule is repeated")
    active: bool = Field(description="Whether the schedule is active")
    relay_position: PositiveInt = Field(description="Position of the relay")


class ScheduleCreate(BaseModel):
    """Creation schema for schedule."""

    start_time: time = Field(description="Start time of the schedule")
    duration: PositiveInt = Field(description="Duration in minutes")
    repeat: Repeat = Field(description="Specifies how the schedule is repeated")
    active: bool = Field(default=True, description="Whether the schedule is active")
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
    relay_position: Union[PositiveInt, None] = Field(
        default=None, description="Position of the relay"
    )


class Relay(BaseModel):
    """Response schema for Relay object."""

    position: PositiveInt = Field(description="Relay position on the board")
    on: bool = Field(description="Indicates if relay is switched on")


class RelayUpdate(BaseModel):
    """Update schema for Relay object."""

    on: bool = Field(description="Indicates if relay is switched on")


class RaspberryPiBoardInfo(BaseModel):
    """Raspberry Pi board information."""

    revision: str = Field(description="Raspberry Pi revision")
    model: str = Field(description="Raspberry Pi model")
    pcb_revision: str = Field(description="Printed Circuit Board (PCB) revision")
    released: str = Field(description="Release date")
    soc: str = Field(description="System On a Chip (SoC)")
    manufacturer: str = Field(description="Manufacturer")
    memory: int = Field(description="Memory (SDRAM)")
    storage: str = Field(description="Storage type")
    usb: int = Field(description="Number of USB ports")
    usb3: int = Field(description="Number of USB3 ports")
    ethernet: int = Field(description="Number of ethernet ports")
    eth_speed: int = Field(description="Ethernet speed")
    wifi: bool = Field(description="Wifi available")
    bluetooth: bool = Field(description="Bluetooth available")
    csi: int = Field(description="Number of Camera Serial Interfaces (CSI)")
    dsi: int = Field(description="Number of Display Serial Interfaces (DSI)")
