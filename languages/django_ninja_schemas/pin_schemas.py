from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from django.contrib.contenttypes.models import ContentType
import uuid
from pydantic import field_validator


class PinBaseSchema(AbstractElementBaseSchema):

    # Details
    map_id: uuid.UUID
    element_type: str | None = None
    element_id: uuid.UUID | None = None
    x: int
    y: int
    z: int | None = None


class PinCreateInSchema(PinBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    element_type: str
    element_id: uuid.UUID


class PinUpdateInSchema(PinBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None
    map_id: uuid.UUID | None = None
    x: int | None = None
    y: int | None = None


class PinFilterSchema(BaseFilterSchema):
    map_id: uuid.UUID | None = Field(None, q='map_id')


class PinOutSchema(AbstractElementBaseSchema):

    # Details
    map: ElementNestedOutSchema
    element_type: str | None = None
    element_id: uuid.UUID | None = None
    x: int
    y: int
    z: int | None = None

    @field_validator('element_type', mode='before')
    @classmethod
    def validate_element_type_output(cls, value):
        if isinstance(value, ContentType):
            return value.model.capitalize() 
        return value
