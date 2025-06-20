from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
import uuid


class MarkerBaseSchema(AbstractElementBaseSchema):

    # Details
    x: int | None = None
    y: int | None = None
    z: int | None = None
    map_id: uuid.UUID | None = None
    zone_id: uuid.UUID | None = None


class MarkerCreateInSchema(MarkerBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class MarkerUpdateInSchema(MarkerBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class MarkerFilterSchema(BaseFilterSchema):
    map_id: uuid.UUID | None = Field(None, q='map_id')
    zone_id: uuid.UUID | None = Field(None, q='zone_id')


class MarkerOutSchema(AbstractElementBaseSchema):

    # Details
    x: int | None = None
    y: int | None = None
    z: int | None = None
    map: ElementNestedOutSchema | None = None
    zone: ElementNestedOutSchema | None = None

