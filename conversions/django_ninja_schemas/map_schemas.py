from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import Optional
import uuid


class MapBaseSchema(AbstractElementBaseSchema):

    # Details
    background_color: str | None = None
    hierarchy: int | None = None
    width: int | None = None
    height: int | None = None
    map: uuid.UUID | None = None


class MapCreateInSchema(MapBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class MapUpdateInSchema(MapBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class MapFilterSchema(BaseFilterSchema):
    map_id: Optional[uuid.UUID] = Field(None, q='map_id')


class MapOutSchema(AbstractElementBaseSchema):

    # Details
    background_color: str | None = None
    hierarchy: int | None = None
    width: int | None = None
    height: int | None = None
    map: Optional[ElementNestedOutSchema] = None

