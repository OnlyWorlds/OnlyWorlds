from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class CollectiveBaseSchema(AbstractElementBaseSchema):

    # Formation
    composition: str | None = None
    count: int | None = None
    formation_date: int | None = None
    operator: uuid.UUID | None = None
    equipment: list[uuid.UUID] | None = None

    # Agency
    activity: str | None = None
    temperance: str | None = None
    skills: list[uuid.UUID] | None = None
    rituals: list[uuid.UUID] | None = None

    # World
    species: list[uuid.UUID] | None = None
    characters: list[uuid.UUID] | None = None
    creatures: list[uuid.UUID] | None = None
    phenomena: list[uuid.UUID] | None = None


class CollectiveCreateInSchema(CollectiveBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class CollectiveUpdateInSchema(CollectiveBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class CollectiveFilterSchema(BaseFilterSchema):
    operator_id: Optional[uuid.UUID] = Field(None, q='operator_id')
    equipment_ids: Optional[uuid.UUID] = Field(None, q='equipment__id')
    skills_ids: Optional[uuid.UUID] = Field(None, q='skills__id')
    rituals_ids: Optional[uuid.UUID] = Field(None, q='rituals__id')
    species_ids: Optional[uuid.UUID] = Field(None, q='species__id')
    characters_ids: Optional[uuid.UUID] = Field(None, q='characters__id')
    creatures_ids: Optional[uuid.UUID] = Field(None, q='creatures__id')
    phenomena_ids: Optional[uuid.UUID] = Field(None, q='phenomena__id')


class CollectiveOutSchema(AbstractElementBaseSchema):

    # Formation
    composition: str | None = None
    count: int | None = None
    formation_date: int | None = None
    operator: Optional[ElementNestedOutSchema] = None
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

