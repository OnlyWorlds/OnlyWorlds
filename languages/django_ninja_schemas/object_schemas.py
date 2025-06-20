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
    materials_ids: list[uuid.UUID] | None = None
    technology_ids: list[uuid.UUID] | None = None

    # Function
    utility: str | None = None
    effects_ids: list[uuid.UUID] | None = None
    abilities_ids: list[uuid.UUID] | None = None
    consumes_ids: list[uuid.UUID] | None = None

    # World
    origins: str | None = None
    location_id: uuid.UUID | None = None
    language_id: uuid.UUID | None = None
    affinities_ids: list[uuid.UUID] | None = None


class ObjectCreateInSchema(ObjectBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class ObjectUpdateInSchema(ObjectBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class ObjectFilterSchema(BaseFilterSchema):
    parent_object_id: uuid.UUID | None = Field(None, q='parent_object_id')
    materials_ids: uuid.UUID | None = Field(None, q='materials__id')
    technology_ids: uuid.UUID | None = Field(None, q='technology__id')
    effects_ids: uuid.UUID | None = Field(None, q='effects__id')
    abilities_ids: uuid.UUID | None = Field(None, q='abilities__id')
    consumes_ids: uuid.UUID | None = Field(None, q='consumes__id')
    location_id: uuid.UUID | None = Field(None, q='location_id')
    language_id: uuid.UUID | None = Field(None, q='language_id')
    affinities_ids: uuid.UUID | None = Field(None, q='affinities__id')


class ObjectOutSchema(AbstractElementBaseSchema):

    # Form
    aesthetics: str | None = None
    weight: int | None = None
    amount: int | None = None
    parent_object: ElementNestedOutSchema | None = None
    materials: List[ElementNestedOutSchema] = []
    technology: List[ElementNestedOutSchema] = []

    # Function
    utility: str | None = None
    effects: List[ElementNestedOutSchema] = []
    abilities: List[ElementNestedOutSchema] = []
    consumes: List[ElementNestedOutSchema] = []

    # World
    origins: str | None = None
    location: ElementNestedOutSchema | None = None
    language: ElementNestedOutSchema | None = None
    affinities: List[ElementNestedOutSchema] = []

