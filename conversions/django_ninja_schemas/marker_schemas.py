from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
import uuid


class MarkerBaseSchema(AbstractElementBaseSchema):

    # Details
    map_id: uuid.UUID | None = None
    x: int | None = None
    y: int | None = None
    z: int | None = None


class MarkerCreateInSchema(MarkerBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class MarkerUpdateInSchema(MarkerBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class MarkerFilterSchema(BaseFilterSchema):
    map_id: uuid.UUID | None = Field(None, q='map_id')


class MarkerOutSchema(AbstractElementBaseSchema):

    # Details
    map: ElementNestedOutSchema | None = None
    x: int | None = None
    y: int | None = None
    z: int | None = None

