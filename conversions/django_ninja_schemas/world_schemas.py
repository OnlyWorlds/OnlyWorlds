import uuid
from typing import List
from ninja import Schema  # type: ignore


class WorldBaseSchema(Schema):
    name: str
    description: str | None = None
    image_url: str | None = None
    time_format_equivalents: List[str]
    time_format_names: List[str]
    time_basic_unit: str
    time_range_min: int
    time_range_max: int
    time_current: int


class WorldOutSchema(WorldBaseSchema):
    id: uuid.UUID
    api_key: str
    version: str


class WorldUpdateSchema(Schema):
    name: str | None = None
    description: str | None = None
    version: str | None = None
    image_url: str | None = None
    time_format_equivalents: List[str] | None = None
    time_format_names: List[str] | None = None
    time_basic_unit: str | None = None
    time_range_min: int | None = None
    time_range_max: int | None = None
    time_current: int | None = None
