from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class ObjectBaseSchema(AbstractElementBaseSchema):

    # Form
    aesthetics: str | None = None
    weight: int | None = None
    amount: int | None = None
    parent_object: uuid.UUID | None = None
    technology: list[uuid.UUID] | None = None

    # Function
    utility: str | None = None
    effects: list[uuid.UUID] | None = None
    enables: list[uuid.UUID] | None = None
    consumes: list[uuid.UUID] | None = None

    # World
    origins: str | None = None
    location: uuid.UUID | None = None

    # Games
    craftsmanship: str | None = None
    requirements: str | None = None
    durability: str | None = None
    value: int | None = None
    damage: int | None = None
    armor: int | None = None
    rarity: str | None = None
    language: uuid.UUID | None = None
    requires: list[uuid.UUID] | None = None


class ObjectCreateInSchema(ObjectBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class ObjectUpdateInSchema(ObjectBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class ObjectFilterSchema(BaseFilterSchema):
    parent_object_id: Optional[uuid.UUID] = Field(None, q='parent_object_id')
    technology_ids: Optional[uuid.UUID] = Field(None, q='technology__id')
    effects_ids: Optional[uuid.UUID] = Field(None, q='effects__id')
    enables_ids: Optional[uuid.UUID] = Field(None, q='enables__id')
    consumes_ids: Optional[uuid.UUID] = Field(None, q='consumes__id')
    location_id: Optional[uuid.UUID] = Field(None, q='location_id')
    language_id: Optional[uuid.UUID] = Field(None, q='language_id')
    requires_ids: Optional[uuid.UUID] = Field(None, q='requires__id')


class ObjectOutSchema(AbstractElementBaseSchema):

    # Form
    aesthetics: str | None = None
    weight: int | None = None
    amount: int | None = None
    parent_object: Optional[ElementNestedOutSchema] = None
    technology: List[ElementNestedOutSchema] = []

    # Function
    utility: str | None = None
    effects: List[ElementNestedOutSchema] = []
    enables: List[ElementNestedOutSchema] = []
    consumes: List[ElementNestedOutSchema] = []

    # World
    origins: str | None = None
    location: Optional[ElementNestedOutSchema] = None

    # Games
    craftsmanship: str | None = None
    requirements: str | None = None
    durability: str | None = None
    value: int | None = None
    damage: int | None = None
    armor: int | None = None
    rarity: str | None = None
    language: Optional[ElementNestedOutSchema] = None
    requires: List[ElementNestedOutSchema] = []

