from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
import uuid


class MapBaseSchema(AbstractElementBaseSchema):

    # Details
    background_color: str | None = None
    hierarchy: int | None = None
    width: int | None = None
    height: int | None = None
    depth: int | None = None
    parent_map_id: uuid.UUID | None = None
    location_id: uuid.UUID | None = None


class MapCreateInSchema(MapBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class MapUpdateInSchema(MapBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class MapFilterSchema(BaseFilterSchema):
    parent_map_id: uuid.UUID | None = Field(None, q='parent_map_id')
    location_id: uuid.UUID | None = Field(None, q='location_id')


class MapOutSchema(AbstractElementBaseSchema):

    # Details
    background_color: str | None = None
    hierarchy: int | None = None
    width: int | None = None
    height: int | None = None
    depth: int | None = None
    parent_map: ElementNestedOutSchema | None = None
    location: ElementNestedOutSchema | None = None

