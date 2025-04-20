from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List
import uuid


class TerritoryBaseSchema(AbstractElementBaseSchema):

    # Situation
    terrain: str | None = None
    size: int | None = None
    parent_territory_id: uuid.UUID | None = None

    # Yield
    maintenance: str | None = None
    primary_output: int | None = None
    secondary_output: int | None = None
    primary_resource_id: uuid.UUID | None = None
    secondary_resources_ids: list[uuid.UUID] | None = None

    # World
    history: str | None = None
    occupants_ids: list[uuid.UUID] | None = None
    occurrences_ids: list[uuid.UUID] | None = None


class TerritoryCreateInSchema(TerritoryBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class TerritoryUpdateInSchema(TerritoryBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class TerritoryFilterSchema(BaseFilterSchema):
    parent_territory_id: uuid.UUID | None = Field(None, q='parent_territory_id')
    primary_resource_id: uuid.UUID | None = Field(None, q='primary_resource_id')
    secondary_resources_ids: uuid.UUID | None = Field(None, q='secondary_resources__id')
    occupants_ids: uuid.UUID | None = Field(None, q='occupants__id')
    occurrences_ids: uuid.UUID | None = Field(None, q='occurrences__id')


class TerritoryOutSchema(AbstractElementBaseSchema):

    # Situation
    terrain: str | None = None
    size: int | None = None
    parent_territory: ElementNestedOutSchema | None = None

    # Yield
    maintenance: str | None = None
    primary_output: int | None = None
    secondary_output: int | None = None
    primary_resource: ElementNestedOutSchema | None = None
    secondary_resources: List[ElementNestedOutSchema] = []

    # World
    history: str | None = None
    occupants: List[ElementNestedOutSchema] = []
    occurrences: List[ElementNestedOutSchema] = []

