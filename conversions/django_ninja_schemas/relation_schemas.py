from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class RelationBaseSchema(AbstractElementBaseSchema):

    # Nature
    history: str | None = None
    impact: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    debt: int | None = None
    events: list[uuid.UUID] | None = None

    # Involves
    primary_character: uuid.UUID | None = None
    primary_creature: uuid.UUID | None = None
    primary_institution: uuid.UUID | None = None
    secondary_characters: list[uuid.UUID] | None = None
    secondary_creatures: list[uuid.UUID] | None = None
    secondary_institutions: list[uuid.UUID] | None = None


class RelationCreateInSchema(RelationBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class RelationUpdateInSchema(RelationBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class RelationFilterSchema(BaseFilterSchema):
    events_ids: Optional[uuid.UUID] = Field(None, q='events__id')
    primary_character_id: Optional[uuid.UUID] = Field(None, q='primary_character_id')
    primary_creature_id: Optional[uuid.UUID] = Field(None, q='primary_creature_id')
    primary_institution_id: Optional[uuid.UUID] = Field(None, q='primary_institution_id')
    secondary_characters_ids: Optional[uuid.UUID] = Field(None, q='secondary_characters__id')
    secondary_creatures_ids: Optional[uuid.UUID] = Field(None, q='secondary_creatures__id')
    secondary_institutions_ids: Optional[uuid.UUID] = Field(None, q='secondary_institutions__id')


class RelationOutSchema(AbstractElementBaseSchema):

    # Nature
    history: str | None = None
    impact: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    debt: int | None = None
    events: List[ElementNestedOutSchema] = []

    # Involves
    primary_character: Optional[ElementNestedOutSchema] = None
    primary_creature: Optional[ElementNestedOutSchema] = None
    primary_institution: Optional[ElementNestedOutSchema] = None
    secondary_characters: List[ElementNestedOutSchema] = []
    secondary_creatures: List[ElementNestedOutSchema] = []
    secondary_institutions: List[ElementNestedOutSchema] = []

