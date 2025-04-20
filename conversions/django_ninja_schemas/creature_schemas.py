from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class CreatureBaseSchema(AbstractElementBaseSchema):

    # Physiology
    appearance: str | None = None
    weight: int | None = None
    height: int | None = None
    species: list[uuid.UUID] | None = None

    # Lifestyle
    behaviour: str | None = None
    demeanour: str | None = None
    traits: list[uuid.UUID] | None = None
    abilities: list[uuid.UUID] | None = None
    languages: list[uuid.UUID] | None = None

    # World
    birth_date: int | None = None
    location: uuid.UUID | None = None
    territory: uuid.UUID | None = None

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
    actions: list[uuid.UUID] | None = None
    reactions: list[uuid.UUID] | None = None
    alignment: str | None = None


class CreatureCreateInSchema(CreatureBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class CreatureUpdateInSchema(CreatureBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class CreatureFilterSchema(BaseFilterSchema):
    species_ids: Optional[uuid.UUID] = Field(None, q='species__id')
    traits_ids: Optional[uuid.UUID] = Field(None, q='traits__id')
    abilities_ids: Optional[uuid.UUID] = Field(None, q='abilities__id')
    languages_ids: Optional[uuid.UUID] = Field(None, q='languages__id')
    location_id: Optional[uuid.UUID] = Field(None, q='location_id')
    territory_id: Optional[uuid.UUID] = Field(None, q='territory_id')
    actions_ids: Optional[uuid.UUID] = Field(None, q='actions__id')
    reactions_ids: Optional[uuid.UUID] = Field(None, q='reactions__id')


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
    location: Optional[ElementNestedOutSchema] = None
    territory: Optional[ElementNestedOutSchema] = None

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

