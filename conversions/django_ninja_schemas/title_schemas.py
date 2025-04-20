from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import Optional
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
    author: uuid.UUID | None = None

    # World
    character: uuid.UUID | None = None
    location: uuid.UUID | None = None
    object: uuid.UUID | None = None
    institution: uuid.UUID | None = None
    creature: uuid.UUID | None = None
    territory: uuid.UUID | None = None
    collective: uuid.UUID | None = None
    construct: uuid.UUID | None = None


class TitleCreateInSchema(TitleBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class TitleUpdateInSchema(TitleBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class TitleFilterSchema(BaseFilterSchema):
    author_id: Optional[uuid.UUID] = Field(None, q='author_id')
    character_id: Optional[uuid.UUID] = Field(None, q='character_id')
    location_id: Optional[uuid.UUID] = Field(None, q='location_id')
    object_id: Optional[uuid.UUID] = Field(None, q='object_id')
    institution_id: Optional[uuid.UUID] = Field(None, q='institution_id')
    creature_id: Optional[uuid.UUID] = Field(None, q='creature_id')
    territory_id: Optional[uuid.UUID] = Field(None, q='territory_id')
    collective_id: Optional[uuid.UUID] = Field(None, q='collective_id')
    construct_id: Optional[uuid.UUID] = Field(None, q='construct_id')


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
    author: Optional[ElementNestedOutSchema] = None

    # World
    character: Optional[ElementNestedOutSchema] = None
    location: Optional[ElementNestedOutSchema] = None
    object: Optional[ElementNestedOutSchema] = None
    institution: Optional[ElementNestedOutSchema] = None
    creature: Optional[ElementNestedOutSchema] = None
    territory: Optional[ElementNestedOutSchema] = None
    collective: Optional[ElementNestedOutSchema] = None
    construct: Optional[ElementNestedOutSchema] = None

