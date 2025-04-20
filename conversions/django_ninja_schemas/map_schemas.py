from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
import uuid


class MapBaseSchema(AbstractElementBaseSchema):

    # Details
    background_color: str | None = None
    hierarchy: int | None = None
    width: int | None = None
    height: int | None = None
    map_id: uuid.UUID | None = None


class MapCreateInSchema(MapBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class MapUpdateInSchema(MapBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class MapFilterSchema(BaseFilterSchema):
    map_id: uuid.UUID | None = Field(None, q='map_id')


class MapOutSchema(AbstractElementBaseSchema):

    # Details
    background_color: str | None = None
    hierarchy: int | None = None
    width: int | None = None
    height: int | None = None
    map: ElementNestedOutSchema | None = None

