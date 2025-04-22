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

    # Agency
    activity: str | None = None
    temperance: str | None = None
    skills_ids: list[uuid.UUID] | None = None
    rituals_ids: list[uuid.UUID] | None = None

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
    skills_ids: uuid.UUID | None = Field(None, q='skills__id')
    rituals_ids: uuid.UUID | None = Field(None, q='rituals__id')
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

    # Agency
    activity: str | None = None
    temperance: str | None = None
    skills: List[ElementNestedOutSchema] = []
    rituals: List[ElementNestedOutSchema] = []

    # World
    species: List[ElementNestedOutSchema] = []
    characters: List[ElementNestedOutSchema] = []
    creatures: List[ElementNestedOutSchema] = []
    phenomena: List[ElementNestedOutSchema] = []

