from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
import uuid


class PinBaseSchema(AbstractElementBaseSchema):

    # Details
    map_id: uuid.UUID
    element_type: str
    element_id: uuid.UUID
    x: int
    y: int
    z: int | None = None


class PinCreateInSchema(PinBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class PinUpdateInSchema(PinBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class PinFilterSchema(BaseFilterSchema):
    map_id: uuid.UUID | None = Field(None, q='map_id')


class PinOutSchema(AbstractElementBaseSchema):

    # Details
    map: ElementNestedOutSchema
    element_type: str
    element_id: uuid.UUID
    x: int
    y: int
    z: int | None = None

