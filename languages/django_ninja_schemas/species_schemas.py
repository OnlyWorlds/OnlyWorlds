from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class SpeciesBaseSchema(AbstractElementBaseSchema):

    # Biology
    appearance: str | None = None
    life_span: int | None = None
    typical_weight: int | None = None
    diet_ids: list[uuid.UUID] | None = None
    reproduction_ids: list[uuid.UUID] | None = None

    # Psychology
    instincts: str | None = None
    sociality: str | None = None
    temperament: str | None = None
    communication: str | None = None
    aggression: int | None = Field(None, le=100)
    traits_ids: list[uuid.UUID] | None = None

    # World
    role: str | None = None
    parent_species_id: uuid.UUID | None = None
    locations_ids: list[uuid.UUID] | None = None
    zones_ids: list[uuid.UUID] | None = None
    affinities_ids: list[uuid.UUID] | None = None


class SpeciesCreateInSchema(SpeciesBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class SpeciesUpdateInSchema(SpeciesBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class SpeciesFilterSchema(BaseFilterSchema):
    diet_ids: uuid.UUID | None = Field(None, q='diet__id')
    reproduction_ids: uuid.UUID | None = Field(None, q='reproduction__id')
    traits_ids: uuid.UUID | None = Field(None, q='traits__id')
    parent_species_id: uuid.UUID | None = Field(None, q='parent_species_id')
    locations_ids: uuid.UUID | None = Field(None, q='locations__id')
    zones_ids: uuid.UUID | None = Field(None, q='zones__id')
    affinities_ids: uuid.UUID | None = Field(None, q='affinities__id')


class SpeciesOutSchema(AbstractElementBaseSchema):

    # Biology
    appearance: str | None = None
    life_span: int | None = None
    typical_weight: int | None = None
    diet: List[ElementNestedOutSchema] = []
    reproduction: List[ElementNestedOutSchema] = []

    # Psychology
    instincts: str | None = None
    sociality: str | None = None
    temperament: str | None = None
    communication: str | None = None
    aggression: int | None = Field(None, le=100)
    traits: List[ElementNestedOutSchema] = []

    # World
    role: str | None = None
    parent_species: ElementNestedOutSchema | None = None
    locations: List[ElementNestedOutSchema] = []
    zones: List[ElementNestedOutSchema] = []
    affinities: List[ElementNestedOutSchema] = []

