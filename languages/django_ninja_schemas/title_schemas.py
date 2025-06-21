from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
import uuid


class TitleBaseSchema(AbstractElementBaseSchema):

    # Nature
    privileges: str | None = None
    conditions: str | None = None
    create_date: int | None = None
    assign_date: int | None = None
    revoke_date: int | None = None
    hierarchy: int | None = None

    # Issue
    rights: str | None = None
    author_id: uuid.UUID | None = None

    # World
    character_id: uuid.UUID | None = None
    location_id: uuid.UUID | None = None
    object_id: uuid.UUID | None = None
    institution_id: uuid.UUID | None = None
    creature_id: uuid.UUID | None = None
    zone_id: uuid.UUID | None = None
    collective_id: uuid.UUID | None = None
    construct_id: uuid.UUID | None = None


class TitleCreateInSchema(TitleBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class TitleUpdateInSchema(TitleBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class TitleFilterSchema(BaseFilterSchema):
    author_id: uuid.UUID | None = Field(None, q='author_id')
    character_id: uuid.UUID | None = Field(None, q='character_id')
    location_id: uuid.UUID | None = Field(None, q='location_id')
    object_id: uuid.UUID | None = Field(None, q='object_id')
    institution_id: uuid.UUID | None = Field(None, q='institution_id')
    creature_id: uuid.UUID | None = Field(None, q='creature_id')
    zone_id: uuid.UUID | None = Field(None, q='zone_id')
    collective_id: uuid.UUID | None = Field(None, q='collective_id')
    construct_id: uuid.UUID | None = Field(None, q='construct_id')


class TitleOutSchema(AbstractElementBaseSchema):

    # Nature
    privileges: str | None = None
    conditions: str | None = None
    create_date: int | None = None
    assign_date: int | None = None
    revoke_date: int | None = None
    hierarchy: int | None = None

    # Issue
    rights: str | None = None
    author: ElementNestedOutSchema | None = None

    # World
    character: ElementNestedOutSchema | None = None
    location: ElementNestedOutSchema | None = None
    object: ElementNestedOutSchema | None = None
    institution: ElementNestedOutSchema | None = None
    creature: ElementNestedOutSchema | None = None
    zone: ElementNestedOutSchema | None = None
    collective: ElementNestedOutSchema | None = None
    construct: ElementNestedOutSchema | None = None

