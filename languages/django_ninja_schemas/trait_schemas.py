from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class TraitBaseSchema(AbstractElementBaseSchema):

    # Qualitative
    social_effects: str | None = None
    physical_effects: str | None = None
    functional_effects: str | None = None
    personality_effects: str | None = None
    behaviour_effects: str | None = None

    # Quantitative
    charisma: int | None = Field(None, le=100)
    coercion: int | None = Field(None, le=100)
    competence: int | None = Field(None, le=100)
    compassion: int | None = Field(None, le=100)
    creativity: int | None = Field(None, le=100)
    courage: int | None = Field(None, le=100)

    # World
    significance: str | None = None
    anti_trait_id: uuid.UUID | None = None
    empowered_abilities_ids: list[uuid.UUID] | None = None


class TraitCreateInSchema(TraitBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class TraitUpdateInSchema(TraitBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class TraitFilterSchema(BaseFilterSchema):
    anti_trait_id: uuid.UUID | None = Field(None, q='anti_trait_id')
    empowered_abilities_ids: uuid.UUID | None = Field(None, q='empowered_abilities__id')


class TraitOutSchema(AbstractElementBaseSchema):

    # Qualitative
    social_effects: str | None = None
    physical_effects: str | None = None
    functional_effects: str | None = None
    personality_effects: str | None = None
    behaviour_effects: str | None = None

    # Quantitative
    charisma: int | None = Field(None, le=100)
    coercion: int | None = Field(None, le=100)
    competence: int | None = Field(None, le=100)
    compassion: int | None = Field(None, le=100)
    creativity: int | None = Field(None, le=100)
    courage: int | None = Field(None, le=100)

    # World
    significance: str | None = None
    anti_trait: ElementNestedOutSchema | None = None
    empowered_abilities: List[ElementNestedOutSchema] = []

