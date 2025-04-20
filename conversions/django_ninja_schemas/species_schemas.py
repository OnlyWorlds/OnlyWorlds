from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class SpeciesBaseSchema(AbstractElementBaseSchema):

    # Biology
    appearance: str | None = None
    life_span: int | None = None
    average_weight: int | None = None
    nourishment: list[uuid.UUID] | None = None

    # Psychology
    instincts: str | None = None
    aggression: int | None = Field(None, le=100)
    agency: str | None = None
    languages: list[uuid.UUID] | None = None

    # World
    impact: str | None = None
    habitat: list[uuid.UUID] | None = None
    interaction: list[uuid.UUID] | None = None
    consumables: list[uuid.UUID] | None = None


class SpeciesCreateInSchema(SpeciesBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class SpeciesUpdateInSchema(SpeciesBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class SpeciesFilterSchema(BaseFilterSchema):
    nourishment_ids: Optional[uuid.UUID] = Field(None, q='nourishment__id')
    languages_ids: Optional[uuid.UUID] = Field(None, q='languages__id')
    habitat_ids: Optional[uuid.UUID] = Field(None, q='habitat__id')
    interaction_ids: Optional[uuid.UUID] = Field(None, q='interaction__id')
    consumables_ids: Optional[uuid.UUID] = Field(None, q='consumables__id')


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

