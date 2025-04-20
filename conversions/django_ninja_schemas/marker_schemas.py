from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import Optional
import uuid


class MarkerBaseSchema(AbstractElementBaseSchema):

    # Details
    map: uuid.UUID | None = None
    x: int | None = None
    y: int | None = None
    z: int | None = None


class MarkerCreateInSchema(MarkerBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class MarkerUpdateInSchema(MarkerBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class MarkerFilterSchema(BaseFilterSchema):
    map_id: Optional[uuid.UUID] = Field(None, q='map_id')


class MarkerOutSchema(AbstractElementBaseSchema):

    # Details
    map: Optional[ElementNestedOutSchema] = None
    x: int | None = None
    y: int | None = None
    z: int | None = None

