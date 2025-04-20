from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class EventBaseSchema(AbstractElementBaseSchema):

    # Nature
    history: str | None = None
    consequences: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    adversity: str | None = None

    # Involves
    characters: list[uuid.UUID] | None = None
    objects: list[uuid.UUID] | None = None
    locations: list[uuid.UUID] | None = None
    species: list[uuid.UUID] | None = None
    creatures: list[uuid.UUID] | None = None
    institutions: list[uuid.UUID] | None = None
    traits: list[uuid.UUID] | None = None
    collectives: list[uuid.UUID] | None = None
    territories: list[uuid.UUID] | None = None
    abilities: list[uuid.UUID] | None = None
    phenomena: list[uuid.UUID] | None = None
    languages: list[uuid.UUID] | None = None
    families: list[uuid.UUID] | None = None
    relations: list[uuid.UUID] | None = None
    titles: list[uuid.UUID] | None = None
    constructs: list[uuid.UUID] | None = None


class EventCreateInSchema(EventBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class EventUpdateInSchema(EventBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class EventFilterSchema(BaseFilterSchema):
    characters_ids: Optional[uuid.UUID] = Field(None, q='characters__id')
    objects_ids: Optional[uuid.UUID] = Field(None, q='objects__id')
    locations_ids: Optional[uuid.UUID] = Field(None, q='locations__id')
    species_ids: Optional[uuid.UUID] = Field(None, q='species__id')
    creatures_ids: Optional[uuid.UUID] = Field(None, q='creatures__id')
    institutions_ids: Optional[uuid.UUID] = Field(None, q='institutions__id')
    traits_ids: Optional[uuid.UUID] = Field(None, q='traits__id')
    collectives_ids: Optional[uuid.UUID] = Field(None, q='collectives__id')
    territories_ids: Optional[uuid.UUID] = Field(None, q='territories__id')
    abilities_ids: Optional[uuid.UUID] = Field(None, q='abilities__id')
    phenomena_ids: Optional[uuid.UUID] = Field(None, q='phenomena__id')
    languages_ids: Optional[uuid.UUID] = Field(None, q='languages__id')
    families_ids: Optional[uuid.UUID] = Field(None, q='families__id')
    relations_ids: Optional[uuid.UUID] = Field(None, q='relations__id')
    titles_ids: Optional[uuid.UUID] = Field(None, q='titles__id')
    constructs_ids: Optional[uuid.UUID] = Field(None, q='constructs__id')


class EventOutSchema(AbstractElementBaseSchema):

    # Nature
    history: str | None = None
    consequences: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    adversity: str | None = None

    # Involves
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

