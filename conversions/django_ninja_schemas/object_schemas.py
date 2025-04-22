from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class ObjectBaseSchema(AbstractElementBaseSchema):

    # Form
    aesthetics: str | None = None
    weight: int | None = None
    amount: int | None = None
    parent_object_id: uuid.UUID | None = None
    technology_ids: list[uuid.UUID] | None = None

    # Function
    utility: str | None = None
    effects_ids: list[uuid.UUID] | None = None
    enables_ids: list[uuid.UUID] | None = None
    consumes_ids: list[uuid.UUID] | None = None

    # World
    origins: str | None = None
    location_id: uuid.UUID | None = None

    # Games
    craftsmanship: str | None = None
    requirements: str | None = None
    durability: str | None = None
    value: int | None = None
    damage: int | None = None
    armor: int | None = None
    rarity: str | None = None
    language_id: uuid.UUID | None = None
    requires_ids: list[uuid.UUID] | None = None


class ObjectCreateInSchema(ObjectBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class ObjectUpdateInSchema(ObjectBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class ObjectFilterSchema(BaseFilterSchema):
    parent_object_id: uuid.UUID | None = Field(None, q='parent_object_id')
    technology_ids: uuid.UUID | None = Field(None, q='technology__id')
    effects_ids: uuid.UUID | None = Field(None, q='effects__id')
    enables_ids: uuid.UUID | None = Field(None, q='enables__id')
    consumes_ids: uuid.UUID | None = Field(None, q='consumes__id')
    location_id: uuid.UUID | None = Field(None, q='location_id')
    language_id: uuid.UUID | None = Field(None, q='language_id')
    requires_ids: uuid.UUID | None = Field(None, q='requires__id')


class ObjectOutSchema(AbstractElementBaseSchema):

    # Form
    aesthetics: str | None = None
    weight: int | None = None
    amount: int | None = None
    parent_object: ElementNestedOutSchema | None = None
    technology: List[ElementNestedOutSchema] = []

    # Function
    utility: str | None = None
    effects: List[ElementNestedOutSchema] = []
    enables: List[ElementNestedOutSchema] = []
    consumes: List[ElementNestedOutSchema] = []

    # World
    origins: str | None = None
    location: ElementNestedOutSchema | None = None

    # Games
    craftsmanship: str | None = None
    requirements: str | None = None
    durability: str | None = None
    value: int | None = None
    damage: int | None = None
    armor: int | None = None
    rarity: str | None = None
    language: ElementNestedOutSchema | None = None
    requires: List[ElementNestedOutSchema] = []

