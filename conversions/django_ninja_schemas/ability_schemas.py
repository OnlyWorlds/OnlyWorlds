from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class AbilityBaseSchema(AbstractElementBaseSchema):

    # Mechanics
    usage: str | None = None
    range: int | None = None
    strength: int | None = Field(None, le=100)
    effects: list[uuid.UUID] | None = None
    utility: list[uuid.UUID] | None = None

    # Dynamics
    difficulty: str | None = None
    talent: list[uuid.UUID] | None = None
    enablers: list[uuid.UUID] | None = None
    requirements: list[uuid.UUID] | None = None

    # World
    prevalence: str | None = None
    system: uuid.UUID | None = None
    construct: uuid.UUID | None = None


class AbilityCreateInSchema(AbilityBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class AbilityUpdateInSchema(AbilityBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class AbilityFilterSchema(BaseFilterSchema):
    effects_ids: Optional[uuid.UUID] = Field(None, q='effects__id')
    utility_ids: Optional[uuid.UUID] = Field(None, q='utility__id')
    talent_ids: Optional[uuid.UUID] = Field(None, q='talent__id')
    enablers_ids: Optional[uuid.UUID] = Field(None, q='enablers__id')
    requirements_ids: Optional[uuid.UUID] = Field(None, q='requirements__id')
    system_id: Optional[uuid.UUID] = Field(None, q='system_id')
    construct_id: Optional[uuid.UUID] = Field(None, q='construct_id')


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
    system: Optional[ElementNestedOutSchema] = None
    construct: Optional[ElementNestedOutSchema] = None

