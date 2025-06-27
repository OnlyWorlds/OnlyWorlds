from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class CollectiveBaseSchema(AbstractElementBaseSchema):

    # Formation
    composition: str | None = None
    count: int | None = None
    formation_date: int | None = None
    operator_id: uuid.UUID | None = None
    equipment_ids: list[uuid.UUID] | None = None

    # Dynamics
    activity: str | None = None
    disposition: str | None = None
    state: str | None = None
    abilities_ids: list[uuid.UUID] | None = None
    symbolism_ids: list[uuid.UUID] | None = None

    # World
    species_ids: list[uuid.UUID] | None = None
    characters_ids: list[uuid.UUID] | None = None
    creatures_ids: list[uuid.UUID] | None = None
    phenomena_ids: list[uuid.UUID] | None = None


class CollectiveCreateInSchema(CollectiveBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class CollectiveUpdateInSchema(CollectiveBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class CollectiveFilterSchema(BaseFilterSchema):
    operator_id: uuid.UUID | None = Field(None, q='operator_id')
    equipment_ids: uuid.UUID | None = Field(None, q='equipment__id')
    abilities_ids: uuid.UUID | None = Field(None, q='abilities__id')
    symbolism_ids: uuid.UUID | None = Field(None, q='symbolism__id')
    species_ids: uuid.UUID | None = Field(None, q='species__id')
    characters_ids: uuid.UUID | None = Field(None, q='characters__id')
    creatures_ids: uuid.UUID | None = Field(None, q='creatures__id')
    phenomena_ids: uuid.UUID | None = Field(None, q='phenomena__id')


class CollectiveOutSchema(AbstractElementBaseSchema):

    # Formation
    composition: str | None = None
    count: int | None = None
    formation_date: int | None = None
    operator: ElementNestedOutSchema | None = None
    equipment: List[ElementNestedOutSchema] = []

    # Dynamics
    activity: str | None = None
    disposition: str | None = None
    state: str | None = None
    abilities: List[ElementNestedOutSchema] = []
    symbolism: List[ElementNestedOutSchema] = []

    # World
    species: List[ElementNestedOutSchema] = []
    characters: List[ElementNestedOutSchema] = []
    creatures: List[ElementNestedOutSchema] = []
    phenomena: List[ElementNestedOutSchema] = []

