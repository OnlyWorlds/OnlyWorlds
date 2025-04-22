from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class AbilityBaseSchema(AbstractElementBaseSchema):

    # Mechanics
    usage: str | None = None
    range: int | None = None
    strength: int | None = Field(None, le=100)
    effects_ids: list[uuid.UUID] | None = []
    utility_ids: list[uuid.UUID] | None = []

    # Dynamics
    difficulty: str | None = None
    talent_ids: list[uuid.UUID] | None = []
    enablers_ids: list[uuid.UUID] | None = []
    requirements_ids: list[uuid.UUID] | None = []

    # World
    prevalence: str | None = None
    system_id: uuid.UUID | None = None
    construct_id: uuid.UUID | None = None


class AbilityCreateInSchema(AbilityBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class AbilityUpdateInSchema(AbilityBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class AbilityFilterSchema(BaseFilterSchema):
    effects_ids: uuid.UUID | None = Field(None, q='effects__id')
    utility_ids: uuid.UUID | None = Field(None, q='utility__id')
    talent_ids: uuid.UUID | None = Field(None, q='talent__id')
    enablers_ids: uuid.UUID | None = Field(None, q='enablers__id')
    requirements_ids: uuid.UUID | None = Field(None, q='requirements__id')
    system_id: uuid.UUID | None = Field(None, q='system_id')
    construct_id: uuid.UUID | None = Field(None, q='construct_id')


class AbilityOutSchema(AbstractElementBaseSchema):

    # Mechanics
    usage: str | None = None
    range: int | None = None
    strength: int | None = Field(None, le=100)
    effects: List[ElementNestedOutSchema] = []
    utility: List[ElementNestedOutSchema] = []

    # Dynamics
    difficulty: str | None = None
    talent: List[ElementNestedOutSchema] = []
    enablers: List[ElementNestedOutSchema] = []
    requirements: List[ElementNestedOutSchema] = []

    # World
    prevalence: str | None = None
    system: ElementNestedOutSchema | None = None
    construct: ElementNestedOutSchema | None = None

