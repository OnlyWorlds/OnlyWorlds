from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class TraitBaseSchema(AbstractElementBaseSchema):

    # Qualitative
    social_effects: str | None = None
    physical_effects: str | None = None
    skill_effects: str | None = None
    personality_effects: str | None = None
    artistic_effects: str | None = None
    behaviour_effects: str | None = None

    # Quantitative
    charisma: int | None = Field(None, le=100)
    coercion: int | None = Field(None, le=100)
    capability: int | None = Field(None, le=100)
    compassion: int | None = Field(None, le=100)
    creativity: int | None = Field(None, le=100)
    courage: int | None = Field(None, le=100)

    # World
    anti_trait: uuid.UUID | None = None
    empowered_abilities: list[uuid.UUID] | None = None


class TraitCreateInSchema(TraitBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class TraitUpdateInSchema(TraitBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class TraitFilterSchema(BaseFilterSchema):
    anti_trait_id: Optional[uuid.UUID] = Field(None, q='anti_trait_id')
    empowered_abilities_ids: Optional[uuid.UUID] = Field(None, q='empowered_abilities__id')


class TraitOutSchema(AbstractElementBaseSchema):

    # Qualitative
    social_effects: str | None = None
    physical_effects: str | None = None
    skill_effects: str | None = None
    personality_effects: str | None = None
    artistic_effects: str | None = None
    behaviour_effects: str | None = None

    # Quantitative
    charisma: int | None = Field(None, le=100)
    coercion: int | None = Field(None, le=100)
    capability: int | None = Field(None, le=100)
    compassion: int | None = Field(None, le=100)
    creativity: int | None = Field(None, le=100)
    courage: int | None = Field(None, le=100)

    # World
    anti_trait: Optional[ElementNestedOutSchema] = None
    empowered_abilities: List[ElementNestedOutSchema] = []

