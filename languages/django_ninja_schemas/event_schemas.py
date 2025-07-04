from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid
from django.apps import apps


class EventBaseSchema(AbstractElementBaseSchema):

    # Nature
    history: str | None = None
    challenges: str | None = None
    consequences: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    triggers_ids: list[uuid.UUID] | None = None

    # Involves
    characters_ids: list[uuid.UUID] | None = None
    objects_ids: list[uuid.UUID] | None = None
    locations_ids: list[uuid.UUID] | None = None
    species_ids: list[uuid.UUID] | None = None
    creatures_ids: list[uuid.UUID] | None = None
    institutions_ids: list[uuid.UUID] | None = None
    traits_ids: list[uuid.UUID] | None = None
    collectives_ids: list[uuid.UUID] | None = None
    zones_ids: list[uuid.UUID] | None = None
    abilities_ids: list[uuid.UUID] | None = None
    phenomena_ids: list[uuid.UUID] | None = None
    languages_ids: list[uuid.UUID] | None = None
    families_ids: list[uuid.UUID] | None = None
    relations_ids: list[uuid.UUID] | None = None
    titles_ids: list[uuid.UUID] | None = None
    constructs_ids: list[uuid.UUID] | None = None


class EventCreateInSchema(EventBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class EventUpdateInSchema(EventBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class EventFilterSchema(BaseFilterSchema):
    triggers_ids: uuid.UUID | None = Field(None, q='triggers__id')
    characters_ids: uuid.UUID | None = Field(None, q='characters__id')
    objects_ids: uuid.UUID | None = Field(None, q='objects__id')
    locations_ids: uuid.UUID | None = Field(None, q='locations__id')
    species_ids: uuid.UUID | None = Field(None, q='species__id')
    creatures_ids: uuid.UUID | None = Field(None, q='creatures__id')
    institutions_ids: uuid.UUID | None = Field(None, q='institutions__id')
    traits_ids: uuid.UUID | None = Field(None, q='traits__id')
    collectives_ids: uuid.UUID | None = Field(None, q='collectives__id')
    zones_ids: uuid.UUID | None = Field(None, q='zones__id')
    abilities_ids: uuid.UUID | None = Field(None, q='abilities__id')
    phenomena_ids: uuid.UUID | None = Field(None, q='phenomena__id')
    languages_ids: uuid.UUID | None = Field(None, q='languages__id')
    families_ids: uuid.UUID | None = Field(None, q='families__id')
    relations_ids: uuid.UUID | None = Field(None, q='relations__id')
    titles_ids: uuid.UUID | None = Field(None, q='titles__id')
    constructs_ids: uuid.UUID | None = Field(None, q='constructs__id')


class EventOutSchema(AbstractElementBaseSchema):

    # Nature
    history: str | None = None
    challenges: str | None = None
    consequences: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    triggers: List[ElementNestedOutSchema] = []

    # Involves
    characters: List[ElementNestedOutSchema] = []
    objects: List[ElementNestedOutSchema] = []
    locations: List[ElementNestedOutSchema] = []
    species: List[ElementNestedOutSchema] = []
    creatures: List[ElementNestedOutSchema] = []
    institutions: List[ElementNestedOutSchema] = []
    traits: List[ElementNestedOutSchema] = []
    collectives: List[ElementNestedOutSchema] = []
    zones: List[ElementNestedOutSchema] = []
    abilities: List[ElementNestedOutSchema] = []
    phenomena: List[ElementNestedOutSchema] = []
    languages: List[ElementNestedOutSchema] = []
    families: List[ElementNestedOutSchema] = []
    relations: List[ElementNestedOutSchema] = []
    titles: List[ElementNestedOutSchema] = []
    constructs: List[ElementNestedOutSchema] = []

    @staticmethod
    def resolve_objects(obj) -> List[ElementNestedOutSchema]:
        """Resolves the 'objects' field overlap for django by querying the reverse M2M relation."""
        try:
            Object = apps.get_model("elements", "Object") 
            return list(Object.objects.filter(event_objects=obj)) # type: ignore
        except LookupError:
            print("Error: Could not find Object model in resolve_objects.")
            return []
        except AttributeError: 
            print(f"Error: Attribute error resolving objects for event {obj.pk}. Check related_name.")
            return []
        except Exception as e:
            print(f"Error resolving objects for event {obj.pk}: {e}")
            return []
