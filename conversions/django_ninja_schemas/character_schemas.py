from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List
import uuid


class CharacterBaseSchema(AbstractElementBaseSchema):

    # Constitution
    physicality: str | None = None
    psychology: str | None = None
    height: int | None = None
    weight: int | None = None
    species_ids: list[uuid.UUID] | None = None
    traits_ids: list[uuid.UUID] | None = None
    abilities_ids: list[uuid.UUID] | None = None

    # Origins
    background: str | None = None
    motivations: str | None = None
    birth_date: int | None = None
    birthplace_id: uuid.UUID | None = None
    languages_ids: list[uuid.UUID] | None = None

    # World
    situation: str | None = None
    location_id: uuid.UUID | None = None
    titles_ids: list[uuid.UUID] | None = None
    objects_ids: list[uuid.UUID] | None = None
    institutions_ids: list[uuid.UUID] | None = None

    # Personality
    charisma: int | None = Field(None, le=100)
    coercion: int | None = Field(None, le=100)
    capability: int | None = Field(None, le=100)
    compassion: int | None = Field(None, le=100)
    creativity: int | None = Field(None, le=100)
    courage: int | None = Field(None, le=100)

    # Social
    family_ids: list[uuid.UUID] | None = None
    friends_ids: list[uuid.UUID] | None = None
    rivals_ids: list[uuid.UUID] | None = None

    # Games
    backstory: str | None = None
    level: int | None = None
    power: int | None = None
    price: int | None = None
    hit_points: int | None = None
    skill_stealth: int | None = None
    tt_str: int | None = Field(None, le=20)
    tt_int: int | None = Field(None, le=20)
    tt_con: int | None = Field(None, le=20)
    tt_dex: int | None = Field(None, le=20)
    tt_wis: int | None = Field(None, le=20)
    tt_cha: int | None = Field(None, le=20)
    character_class: str | None = None
    alignment: str | None = None
    equipment_ids: list[uuid.UUID] | None = None
    backpack_ids: list[uuid.UUID] | None = None
    proficiencies_ids: list[uuid.UUID] | None = None
    features_ids: list[uuid.UUID] | None = None
    spells_ids: list[uuid.UUID] | None = None
    inspirations_ids: list[uuid.UUID] | None = None


class CharacterCreateInSchema(CharacterBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class CharacterUpdateInSchema(CharacterBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class CharacterFilterSchema(BaseFilterSchema):
    species_ids: uuid.UUID | None = Field(None, q='species__id')
    traits_ids: uuid.UUID | None = Field(None, q='traits__id')
    abilities_ids: uuid.UUID | None = Field(None, q='abilities__id')
    birthplace_id: uuid.UUID | None = Field(None, q='birthplace_id')
    languages_ids: uuid.UUID | None = Field(None, q='languages__id')
    location_id: uuid.UUID | None = Field(None, q='location_id')
    titles_ids: uuid.UUID | None = Field(None, q='titles__id')
    objects_ids: uuid.UUID | None = Field(None, q='objects__id')
    institutions_ids: uuid.UUID | None = Field(None, q='institutions__id')
    family_ids: uuid.UUID | None = Field(None, q='family__id')
    friends_ids: uuid.UUID | None = Field(None, q='friends__id')
    rivals_ids: uuid.UUID | None = Field(None, q='rivals__id')
    equipment_ids: uuid.UUID | None = Field(None, q='equipment__id')
    backpack_ids: uuid.UUID | None = Field(None, q='backpack__id')
    proficiencies_ids: uuid.UUID | None = Field(None, q='proficiencies__id')
    features_ids: uuid.UUID | None = Field(None, q='features__id')
    spells_ids: uuid.UUID | None = Field(None, q='spells__id')
    inspirations_ids: uuid.UUID | None = Field(None, q='inspirations__id')


class CharacterOutSchema(AbstractElementBaseSchema):

    # Constitution
    physicality: str | None = None
    psychology: str | None = None
    height: int | None = None
    weight: int | None = None
    species: List[ElementNestedOutSchema] = []
    traits: List[ElementNestedOutSchema] = []
    abilities: List[ElementNestedOutSchema] = []

    # Origins
    background: str | None = None
    motivations: str | None = None
    birth_date: int | None = None
    birthplace: ElementNestedOutSchema | None = None
    languages: List[ElementNestedOutSchema] = []

    # World
    situation: str | None = None
    location: ElementNestedOutSchema | None = None
    titles: List[ElementNestedOutSchema] = []
    objects: List[ElementNestedOutSchema] = []
    institutions: List[ElementNestedOutSchema] = []

    # Personality
    charisma: int | None = Field(None, le=100)
    coercion: int | None = Field(None, le=100)
    capability: int | None = Field(None, le=100)
    compassion: int | None = Field(None, le=100)
    creativity: int | None = Field(None, le=100)
    courage: int | None = Field(None, le=100)

    # Social
    family: List[ElementNestedOutSchema] = []
    friends: List[ElementNestedOutSchema] = []
    rivals: List[ElementNestedOutSchema] = []

    # Games
    backstory: str | None = None
    level: int | None = None
    power: int | None = None
    price: int | None = None
    hit_points: int | None = None
    skill_stealth: int | None = None
    tt_str: int | None = Field(None, le=20)
    tt_int: int | None = Field(None, le=20)
    tt_con: int | None = Field(None, le=20)
    tt_dex: int | None = Field(None, le=20)
    tt_wis: int | None = Field(None, le=20)
    tt_cha: int | None = Field(None, le=20)
    character_class: str | None = None
    alignment: str | None = None
    equipment: List[ElementNestedOutSchema] = []
    backpack: List[ElementNestedOutSchema] = []
    proficiencies: List[ElementNestedOutSchema] = []
    features: List[ElementNestedOutSchema] = []
    spells: List[ElementNestedOutSchema] = []
    inspirations: List[ElementNestedOutSchema] = []

