from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import Optional
import uuid


class PinBaseSchema(AbstractElementBaseSchema):

    # Details
    map: uuid.UUID | None = None
    element: uuid.UUID | None = None
    x: int | None = None
    y: int | None = None
    z: int | None = None


class PinCreateInSchema(PinBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class PinUpdateInSchema(PinBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class PinFilterSchema(BaseFilterSchema):
    map_id: Optional[uuid.UUID] = Field(None, q='map_id')
    element_id: Optional[uuid.UUID] = Field(None, q='element_id')


class PinOutSchema(AbstractElementBaseSchema):

    # Details
    map: Optional[ElementNestedOutSchema] = None
    element: Optional[ElementNestedOutSchema] = None
    x: int | None = None
    y: int | None = None
    z: int | None = None

