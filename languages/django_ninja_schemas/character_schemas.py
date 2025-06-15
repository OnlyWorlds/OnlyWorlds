from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class CharacterBaseSchema(AbstractElementBaseSchema):

    # Constitution
    physicality: str | None = None
    mentality: str | None = None
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
    reputation: str | None = None
    location_id: uuid.UUID | None = None
    objects_ids: list[uuid.UUID] | None = None
    institutions_ids: list[uuid.UUID] | None = None

    # Personality
    charisma: int | None = Field(None, le=100)
    coercion: int | None = Field(None, le=100)
    competence: int | None = Field(None, le=100)
    compassion: int | None = Field(None, le=100)
    creativity: int | None = Field(None, le=100)
    courage: int | None = Field(None, le=100)

    # Social
    family_ids: list[uuid.UUID] | None = None
    friends_ids: list[uuid.UUID] | None = None
    rivals_ids: list[uuid.UUID] | None = None

    # Ttrpg
    level: int | None = None
    STR: int | None = None
    DEX: int | None = None
    CON: int | None = None
    INT: int | None = None
    WIS: int | None = None
    CHA: int | None = None
    hit_points: int | None = None


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
    objects_ids: uuid.UUID | None = Field(None, q='objects__id')
    institutions_ids: uuid.UUID | None = Field(None, q='institutions__id')
    family_ids: uuid.UUID | None = Field(None, q='family__id')
    friends_ids: uuid.UUID | None = Field(None, q='friends__id')
    rivals_ids: uuid.UUID | None = Field(None, q='rivals__id')


class CharacterOutSchema(AbstractElementBaseSchema):

    # Constitution
    physicality: str | None = None
    mentality: str | None = None
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
    reputation: str | None = None
    location: ElementNestedOutSchema | None = None
    objects: List[ElementNestedOutSchema] = []
    institutions: List[ElementNestedOutSchema] = []

    # Personality
    charisma: int | None = Field(None, le=100)
    coercion: int | None = Field(None, le=100)
    competence: int | None = Field(None, le=100)
    compassion: int | None = Field(None, le=100)
    creativity: int | None = Field(None, le=100)
    courage: int | None = Field(None, le=100)

    # Social
    family: List[ElementNestedOutSchema] = []
    friends: List[ElementNestedOutSchema] = []
    rivals: List[ElementNestedOutSchema] = []

    # Ttrpg
    level: int | None = None
    STR: int | None = None
    DEX: int | None = None
    CON: int | None = None
    INT: int | None = None
    WIS: int | None = None
    CHA: int | None = None
    hit_points: int | None = None

