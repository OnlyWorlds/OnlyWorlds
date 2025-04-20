from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class CharacterBaseSchema(AbstractElementBaseSchema):

    # Constitution
    physicality: str | None = None
    psychology: str | None = None
    height: int | None = None
    weight: int | None = None
    species: list[uuid.UUID] | None = None
    traits: list[uuid.UUID] | None = None
    abilities: list[uuid.UUID] | None = None

    # Origins
    background: str | None = None
    motivations: str | None = None
    birth_date: int | None = None
    birthplace: uuid.UUID | None = None
    languages: list[uuid.UUID] | None = None

    # World
    situation: str | None = None
    location: uuid.UUID | None = None
    titles: list[uuid.UUID] | None = None
    objects: list[uuid.UUID] | None = None
    institutions: list[uuid.UUID] | None = None

    # Personality
    charisma: int | None = Field(None, le=100)
    coercion: int | None = Field(None, le=100)
    capability: int | None = Field(None, le=100)
    compassion: int | None = Field(None, le=100)
    creativity: int | None = Field(None, le=100)
    courage: int | None = Field(None, le=100)

    # Social
    family: list[uuid.UUID] | None = None
    friends: list[uuid.UUID] | None = None
    rivals: list[uuid.UUID] | None = None

    # Games
    backstory: str | None = None
    level: int | None = None
    power: int | None = None
    price: int | None = Field(None, le=9999)
    hit_points: int | None = Field(None, le=999)
    skill_stealth: int | None = None
    tt_str: int | None = Field(None, le=20)
    tt_int: int | None = Field(None, le=20)
    tt_con: int | None = Field(None, le=20)
    tt_dex: int | None = Field(None, le=20)
    tt_wis: int | None = Field(None, le=20)
    tt_cha: int | None = Field(None, le=20)
    class_: str | None = Field(None, alias='class')
    alignment: str | None = None
    equipment: list[uuid.UUID] | None = None
    backpack: list[uuid.UUID] | None = None
    proficiencies: list[uuid.UUID] | None = None
    features: list[uuid.UUID] | None = None
    spells: list[uuid.UUID] | None = None
    inspirations: list[uuid.UUID] | None = None


class CharacterCreateInSchema(CharacterBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class CharacterUpdateInSchema(CharacterBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class CharacterFilterSchema(BaseFilterSchema):
    species_ids: Optional[uuid.UUID] = Field(None, q='species__id')
    traits_ids: Optional[uuid.UUID] = Field(None, q='traits__id')
    abilities_ids: Optional[uuid.UUID] = Field(None, q='abilities__id')
    birthplace_id: Optional[uuid.UUID] = Field(None, q='birthplace_id')
    languages_ids: Optional[uuid.UUID] = Field(None, q='languages__id')
    location_id: Optional[uuid.UUID] = Field(None, q='location_id')
    titles_ids: Optional[uuid.UUID] = Field(None, q='titles__id')
    objects_ids: Optional[uuid.UUID] = Field(None, q='objects__id')
    institutions_ids: Optional[uuid.UUID] = Field(None, q='institutions__id')
    family_ids: Optional[uuid.UUID] = Field(None, q='family__id')
    friends_ids: Optional[uuid.UUID] = Field(None, q='friends__id')
    rivals_ids: Optional[uuid.UUID] = Field(None, q='rivals__id')
    equipment_ids: Optional[uuid.UUID] = Field(None, q='equipment__id')
    backpack_ids: Optional[uuid.UUID] = Field(None, q='backpack__id')
    proficiencies_ids: Optional[uuid.UUID] = Field(None, q='proficiencies__id')
    features_ids: Optional[uuid.UUID] = Field(None, q='features__id')
    spells_ids: Optional[uuid.UUID] = Field(None, q='spells__id')
    inspirations_ids: Optional[uuid.UUID] = Field(None, q='inspirations__id')


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
    birthplace: Optional[ElementNestedOutSchema] = None
    languages: List[ElementNestedOutSchema] = []

    # World
    situation: str | None = None
    location: Optional[ElementNestedOutSchema] = None
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
    price: int | None = Field(None, le=9999)
    hit_points: int | None = Field(None, le=999)
    skill_stealth: int | None = None
    tt_str: int | None = Field(None, le=20)
    tt_int: int | None = Field(None, le=20)
    tt_con: int | None = Field(None, le=20)
    tt_dex: int | None = Field(None, le=20)
    tt_wis: int | None = Field(None, le=20)
    tt_cha: int | None = Field(None, le=20)
    class_: str | None = Field(None, alias='class')
    alignment: str | None = None
    equipment: List[ElementNestedOutSchema] = []
    backpack: List[ElementNestedOutSchema] = []
    proficiencies: List[ElementNestedOutSchema] = []
    features: List[ElementNestedOutSchema] = []
    spells: List[ElementNestedOutSchema] = []
    inspirations: List[ElementNestedOutSchema] = []

