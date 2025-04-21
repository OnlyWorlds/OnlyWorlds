from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
import uuid


class PinBaseSchema(AbstractElementBaseSchema):

    # Details
    map_id: uuid.UUID
    element_id: uuid.UUID | None = None
    x: int | None = None
    y: int | None = None
    z: int | None = None


class PinCreateInSchema(PinBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class PinUpdateInSchema(PinBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class PinFilterSchema(BaseFilterSchema):
    map_id: uuid.UUID | None = Field(None, q='map_id')
    element_id: uuid.UUID | None = Field(None, q='element_id')


class PinOutSchema(AbstractElementBaseSchema):

    # Details
    map: ElementNestedOutSchema | None = None
    element: ElementNestedOutSchema | None = None
    x: int | None = None
    y: int | None = None
    z: int | None = None

