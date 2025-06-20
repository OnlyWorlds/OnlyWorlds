from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class NarrativeBaseSchema(AbstractElementBaseSchema):

    # Context
    story: str | None = None
    consequences: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    order: int | None = None
    parent_narrative_id: uuid.UUID | None = None
    protagonist_id: uuid.UUID | None = None
    antagonist_id: uuid.UUID | None = None
    narrator_id: uuid.UUID | None = None
    conservator_id: uuid.UUID | None = None

    # Involves
    events_ids: list[uuid.UUID] | None = None
    characters_ids: list[uuid.UUID] | None = None
    objects_ids: list[uuid.UUID] | None = None
    locations_ids: list[uuid.UUID] | None = None
    species_ids: list[uuid.UUID] | None = None
    creatures_ids: list[uuid.UUID] | None = None
    institutions_ids: list[uuid.UUID] | None = None
    traits_ids: list[uuid.UUID] | None = None
    collectives_ids: list[uuid.UUID] | None = None
    territories_ids: list[uuid.UUID] | None = None
    abilities_ids: list[uuid.UUID] | None = None
    phenomena_ids: list[uuid.UUID] | None = None
    languages_ids: list[uuid.UUID] | None = None
    families_ids: list[uuid.UUID] | None = None
    relations_ids: list[uuid.UUID] | None = None
    titles_ids: list[uuid.UUID] | None = None
    constructs_ids: list[uuid.UUID] | None = None
    laws_ids: list[uuid.UUID] | None = None


class NarrativeCreateInSchema(NarrativeBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class NarrativeUpdateInSchema(NarrativeBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class NarrativeFilterSchema(BaseFilterSchema):
    parent_narrative_id: uuid.UUID | None = Field(None, q='parent_narrative_id')
    protagonist_id: uuid.UUID | None = Field(None, q='protagonist_id')
    antagonist_id: uuid.UUID | None = Field(None, q='antagonist_id')
    narrator_id: uuid.UUID | None = Field(None, q='narrator_id')
    conservator_id: uuid.UUID | None = Field(None, q='conservator_id')
    events_ids: uuid.UUID | None = Field(None, q='events__id')
    characters_ids: uuid.UUID | None = Field(None, q='characters__id')
    objects_ids: uuid.UUID | None = Field(None, q='objects__id')
    locations_ids: uuid.UUID | None = Field(None, q='locations__id')
    species_ids: uuid.UUID | None = Field(None, q='species__id')
    creatures_ids: uuid.UUID | None = Field(None, q='creatures__id')
    institutions_ids: uuid.UUID | None = Field(None, q='institutions__id')
    traits_ids: uuid.UUID | None = Field(None, q='traits__id')
    collectives_ids: uuid.UUID | None = Field(None, q='collectives__id')
    territories_ids: uuid.UUID | None = Field(None, q='territories__id')
    abilities_ids: uuid.UUID | None = Field(None, q='abilities__id')
    phenomena_ids: uuid.UUID | None = Field(None, q='phenomena__id')
    languages_ids: uuid.UUID | None = Field(None, q='languages__id')
    families_ids: uuid.UUID | None = Field(None, q='families__id')
    relations_ids: uuid.UUID | None = Field(None, q='relations__id')
    titles_ids: uuid.UUID | None = Field(None, q='titles__id')
    constructs_ids: uuid.UUID | None = Field(None, q='constructs__id')
    laws_ids: uuid.UUID | None = Field(None, q='laws__id')


class NarrativeOutSchema(AbstractElementBaseSchema):

    # Context
    story: str | None = None
    consequences: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    order: int | None = None
    parent_narrative: ElementNestedOutSchema | None = None
    protagonist: ElementNestedOutSchema | None = None
    antagonist: ElementNestedOutSchema | None = None
    narrator: ElementNestedOutSchema | None = None
    conservator: ElementNestedOutSchema | None = None

    # Involves
    events: List[ElementNestedOutSchema] = []
    characters: List[ElementNestedOutSchema] = []
    objects: List[ElementNestedOutSchema] = []
    locations: List[ElementNestedOutSchema] = []
    species: List[ElementNestedOutSchema] = []
    creatures: List[ElementNestedOutSchema] = []
    institutions: List[ElementNestedOutSchema] = []
    traits: List[ElementNestedOutSchema] = []
    collectives: List[ElementNestedOutSchema] = []
    territories: List[ElementNestedOutSchema] = []
    abilities: List[ElementNestedOutSchema] = []
    phenomena: List[ElementNestedOutSchema] = []
    languages: List[ElementNestedOutSchema] = []
    families: List[ElementNestedOutSchema] = []
    relations: List[ElementNestedOutSchema] = []
    titles: List[ElementNestedOutSchema] = []
    constructs: List[ElementNestedOutSchema] = []
    laws: List[ElementNestedOutSchema] = []

