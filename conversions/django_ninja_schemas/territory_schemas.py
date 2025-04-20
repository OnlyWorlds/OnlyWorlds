from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class TerritoryBaseSchema(AbstractElementBaseSchema):

    # Situation
    terrain: str | None = None
    size: int | None = None
    parent_territory: uuid.UUID | None = None

    # Yield
    maintenance: str | None = None
    primary_output: int | None = None
    secondary_output: int | None = None
    primary_resource: uuid.UUID | None = None
    secondary_resources: list[uuid.UUID] | None = None

    # World
    history: str | None = None
    occupants: list[uuid.UUID] | None = None
    occurrences: list[uuid.UUID] | None = None


class TerritoryCreateInSchema(TerritoryBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class TerritoryUpdateInSchema(TerritoryBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class TerritoryFilterSchema(BaseFilterSchema):
    parent_territory_id: Optional[uuid.UUID] = Field(None, q='parent_territory_id')
    primary_resource_id: Optional[uuid.UUID] = Field(None, q='primary_resource_id')
    secondary_resources_ids: Optional[uuid.UUID] = Field(None, q='secondary_resources__id')
    occupants_ids: Optional[uuid.UUID] = Field(None, q='occupants__id')
    occurrences_ids: Optional[uuid.UUID] = Field(None, q='occurrences__id')


class TerritoryOutSchema(AbstractElementBaseSchema):

    # Situation
    terrain: str | None = None
    size: int | None = None
    parent_territory: Optional[ElementNestedOutSchema] = None

    # Yield
    maintenance: str | None = None
    primary_output: int | None = None
    secondary_output: int | None = None
    primary_resource: Optional[ElementNestedOutSchema] = None
    secondary_resources: List[ElementNestedOutSchema] = []

    # World
    history: str | None = None
    occupants: List[ElementNestedOutSchema] = []
    occurrences: List[ElementNestedOutSchema] = []

