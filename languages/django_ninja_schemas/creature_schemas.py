from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class CreatureBaseSchema(AbstractElementBaseSchema):

    # Physiology
    appearance: str | None = None
    weight: int | None = None
    height: int | None = None
    species_ids: list[uuid.UUID] | None = None

    # Lifestyle
    behaviour: str | None = None
    demeanour: str | None = None
    traits_ids: list[uuid.UUID] | None = None
    abilities_ids: list[uuid.UUID] | None = None
    languages_ids: list[uuid.UUID] | None = None

    # World
    birth_date: int | None = None
    location_id: uuid.UUID | None = None
    territory_id: uuid.UUID | None = None

    # Games
    lore: str | None = None
    senses: str | None = None
    hit_points: int | None = None
    armor_class: int | None = None
    challenge_rating: int | None = None
    speed: int | None = None
    tt_str: int | None = Field(None, le=20)
    tt_int: int | None = Field(None, le=20)
    tt_con: int | None = Field(None, le=20)
    tt_dex: int | None = Field(None, le=20)
    tt_wis: int | None = Field(None, le=20)
    tt_cha: int | None = Field(None, le=20)
    actions_ids: list[uuid.UUID] | None = None
    reactions_ids: list[uuid.UUID] | None = None
    alignment: str | None = None


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
    territory_id: uuid.UUID | None = Field(None, q='territory_id')
    actions_ids: uuid.UUID | None = Field(None, q='actions__id')
    reactions_ids: uuid.UUID | None = Field(None, q='reactions__id')


class CreatureOutSchema(AbstractElementBaseSchema):

    # Physiology
    appearance: str | None = None
    weight: int | None = None
    height: int | None = None
    species: List[ElementNestedOutSchema] = []

    # Lifestyle
    behaviour: str | None = None
    demeanour: str | None = None
    traits: List[ElementNestedOutSchema] = []
    abilities: List[ElementNestedOutSchema] = []
    languages: List[ElementNestedOutSchema] = []

    # World
    birth_date: int | None = None
    location: ElementNestedOutSchema | None = None
    territory: ElementNestedOutSchema | None = None

    # Games
    lore: str | None = None
    senses: str | None = None
    hit_points: int | None = None
    armor_class: int | None = None
    challenge_rating: int | None = None
    speed: int | None = None
    tt_str: int | None = Field(None, le=20)
    tt_int: int | None = Field(None, le=20)
    tt_con: int | None = Field(None, le=20)
    tt_dex: int | None = Field(None, le=20)
    tt_wis: int | None = Field(None, le=20)
    tt_cha: int | None = Field(None, le=20)
    actions: List[ElementNestedOutSchema] = []
    reactions: List[ElementNestedOutSchema] = []
    alignment: str | None = None

