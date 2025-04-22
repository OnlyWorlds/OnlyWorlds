from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class RelationBaseSchema(AbstractElementBaseSchema):

    # Nature
    history: str | None = None
    impact: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    debt: int | None = None
    events_ids: list[uuid.UUID] | None = []

    # Involves
    primary_character_id: uuid.UUID | None = None
    primary_creature_id: uuid.UUID | None = None
    primary_institution_id: uuid.UUID | None = None
    secondary_characters_ids: list[uuid.UUID] | None = []
    secondary_creatures_ids: list[uuid.UUID] | None = []
    secondary_institutions_ids: list[uuid.UUID] | None = []


class RelationCreateInSchema(RelationBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class RelationUpdateInSchema(RelationBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class RelationFilterSchema(BaseFilterSchema):
    events_ids: uuid.UUID | None = Field(None, q='events__id')
    primary_character_id: uuid.UUID | None = Field(None, q='primary_character_id')
    primary_creature_id: uuid.UUID | None = Field(None, q='primary_creature_id')
    primary_institution_id: uuid.UUID | None = Field(None, q='primary_institution_id')
    secondary_characters_ids: uuid.UUID | None = Field(None, q='secondary_characters__id')
    secondary_creatures_ids: uuid.UUID | None = Field(None, q='secondary_creatures__id')
    secondary_institutions_ids: uuid.UUID | None = Field(None, q='secondary_institutions__id')


class RelationOutSchema(AbstractElementBaseSchema):

    # Nature
    history: str | None = None
    impact: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    debt: int | None = None
    events: List[ElementNestedOutSchema] = []

    # Involves
    primary_character: ElementNestedOutSchema | None = None
    primary_creature: ElementNestedOutSchema | None = None
    primary_institution: ElementNestedOutSchema | None = None
    secondary_characters: List[ElementNestedOutSchema] = []
    secondary_creatures: List[ElementNestedOutSchema] = []
    secondary_institutions: List[ElementNestedOutSchema] = []

