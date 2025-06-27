from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class AbilityBaseSchema(AbstractElementBaseSchema):

    # Mechanics
    activation: str | None = None
    duration: int | None = None
    potency: int | None = Field(None, le=100)
    range: int | None = None
    effects_ids: list[uuid.UUID] | None = None
    challenges: str | None = None
    talents_ids: list[uuid.UUID] | None = None
    requisites_ids: list[uuid.UUID] | None = None

    # World
    prevalence: str | None = None
    tradition_id: uuid.UUID | None = None
    source_id: uuid.UUID | None = None
    locus_id: uuid.UUID | None = None
    instruments_ids: list[uuid.UUID] | None = None
    systems_ids: list[uuid.UUID] | None = None


class AbilityCreateInSchema(AbilityBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class AbilityUpdateInSchema(AbilityBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class AbilityFilterSchema(BaseFilterSchema):
    effects_ids: uuid.UUID | None = Field(None, q='effects__id')
    talents_ids: uuid.UUID | None = Field(None, q='talents__id')
    requisites_ids: uuid.UUID | None = Field(None, q='requisites__id')
    tradition_id: uuid.UUID | None = Field(None, q='tradition_id')
    source_id: uuid.UUID | None = Field(None, q='source_id')
    locus_id: uuid.UUID | None = Field(None, q='locus_id')
    instruments_ids: uuid.UUID | None = Field(None, q='instruments__id')
    systems_ids: uuid.UUID | None = Field(None, q='systems__id')


class AbilityOutSchema(AbstractElementBaseSchema):

    # Mechanics
    activation: str | None = None
    duration: int | None = None
    potency: int | None = Field(None, le=100)
    range: int | None = None
    effects: List[ElementNestedOutSchema] = []
    challenges: str | None = None
    talents: List[ElementNestedOutSchema] = []
    requisites: List[ElementNestedOutSchema] = []

    # World
    prevalence: str | None = None
    tradition: ElementNestedOutSchema | None = None
    source: ElementNestedOutSchema | None = None
    locus: ElementNestedOutSchema | None = None
    instruments: List[ElementNestedOutSchema] = []
    systems: List[ElementNestedOutSchema] = []

