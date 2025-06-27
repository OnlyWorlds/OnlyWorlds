from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class CreatureBaseSchema(AbstractElementBaseSchema):

    # Biology
    appearance: str | None = None
    weight: int | None = None
    height: int | None = None
    species_ids: list[uuid.UUID] | None = None

    # Behaviour
    habits: str | None = None
    demeanor: str | None = None
    traits_ids: list[uuid.UUID] | None = None
    abilities_ids: list[uuid.UUID] | None = None
    languages_ids: list[uuid.UUID] | None = None

    # World
    status: str | None = None
    birth_date: int | None = None
    location_id: uuid.UUID | None = None
    zone_id: uuid.UUID | None = None

    # Ttrpg
    challenge_rating: int | None = None
    hit_points: int | None = None
    armor_class: int | None = None
    speed: int | None = None
    actions_ids: list[uuid.UUID] | None = None


class CreatureCreateInSchema(CreatureBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class CreatureUpdateInSchema(CreatureBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class CreatureFilterSchema(BaseFilterSchema):
    species_ids: uuid.UUID | None = Field(None, q='species__id')
    traits_ids: uuid.UUID | None = Field(None, q='traits__id')
    abilities_ids: uuid.UUID | None = Field(None, q='abilities__id')
    languages_ids: uuid.UUID | None = Field(None, q='languages__id')
    location_id: uuid.UUID | None = Field(None, q='location_id')
    zone_id: uuid.UUID | None = Field(None, q='zone_id')
    actions_ids: uuid.UUID | None = Field(None, q='actions__id')


class CreatureOutSchema(AbstractElementBaseSchema):

    # Biology
    appearance: str | None = None
    weight: int | None = None
    height: int | None = None
    species: List[ElementNestedOutSchema] = []

    # Behaviour
    habits: str | None = None
    demeanor: str | None = None
    traits: List[ElementNestedOutSchema] = []
    abilities: List[ElementNestedOutSchema] = []
    languages: List[ElementNestedOutSchema] = []

    # World
    status: str | None = None
    birth_date: int | None = None
    location: ElementNestedOutSchema | None = None
    zone: ElementNestedOutSchema | None = None

    # Ttrpg
    challenge_rating: int | None = None
    hit_points: int | None = None
    armor_class: int | None = None
    speed: int | None = None
    actions: List[ElementNestedOutSchema] = []

