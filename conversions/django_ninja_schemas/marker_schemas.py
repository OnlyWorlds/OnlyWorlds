from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
import uuid


class MarkerBaseSchema(AbstractElementBaseSchema):

    # Details
    map_id: uuid.UUID
    zone_id: uuid.UUID | None = None
    x: int
    y: int
    z: int | None = None


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
    map: ElementNestedOutSchema
    zone: ElementNestedOutSchema | None = None
    x: int
    y: int
    z: int | None = None

