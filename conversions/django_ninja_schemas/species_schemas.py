from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class SpeciesBaseSchema(AbstractElementBaseSchema):

    # Biology
    appearance: str | None = None
    life_span: int | None = None
    average_weight: int | None = None
    nourishment_ids: list[uuid.UUID] | None = None

    # Psychology
    instincts: str | None = None
    aggression: int | None = Field(None, le=100)
    agency: str | None = None
    languages_ids: list[uuid.UUID] | None = None

    # World
    impact: str | None = None
    habitat_ids: list[uuid.UUID] | None = None
    interaction_ids: list[uuid.UUID] | None = None
    consumables_ids: list[uuid.UUID] | None = None


class SpeciesCreateInSchema(SpeciesBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class SpeciesUpdateInSchema(SpeciesBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class SpeciesFilterSchema(BaseFilterSchema):
    nourishment_ids: uuid.UUID | None = Field(None, q='nourishment__id')
    languages_ids: uuid.UUID | None = Field(None, q='languages__id')
    habitat_ids: uuid.UUID | None = Field(None, q='habitat__id')
    interaction_ids: uuid.UUID | None = Field(None, q='interaction__id')
    consumables_ids: uuid.UUID | None = Field(None, q='consumables__id')


class SpeciesOutSchema(AbstractElementBaseSchema):

    # Biology
    appearance: str | None = None
    life_span: int | None = None
    average_weight: int | None = None
    nourishment: List[ElementNestedOutSchema] = []

    # Psychology
    instincts: str | None = None
    aggression: int | None = Field(None, le=100)
    agency: str | None = None
    languages: List[ElementNestedOutSchema] = []

    # World
    impact: str | None = None
    habitat: List[ElementNestedOutSchema] = []
    interaction: List[ElementNestedOutSchema] = []
    consumables: List[ElementNestedOutSchema] = []

