from ninja import Field, Schema, FilterSchema # type: ignore
from typing import List # Only List needed now
import uuid


class AbstractElementBaseSchema(Schema):
    id: uuid.UUID
    name: str
    description: str | None = Field(None, alias='Description')
    supertype: str | None = Field(None, alias='Supertype')
    subtype: str | None = Field(None, alias='Subtype')
    image_url: str | None = Field(None, alias='Image_URL')
    world: uuid.UUID | None = None


class ElementNestedOutSchema(Schema):
    id: uuid.UUID
    name: str
    supertype: str | None = None
    subtype: str | None = None
    image_url: str | None = Field(None, alias='Image_URL')


class BaseFilterSchema(FilterSchema):
    """Base filter schema including common element fields."""
    name__icontains: str | None = Field(None, q='name__icontains')
    supertype: str | None = Field(None, q='supertype')
    subtype: str | None = Field(None, q='subtype')
