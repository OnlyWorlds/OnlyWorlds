from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid
from django.apps import apps


class TitleBaseSchema(AbstractElementBaseSchema):

    # Mandate
    authority: str | None = None
    eligibility: str | None = None
    grant_date: int | None = None
    revoke_date: int | None = None
    issuer_id: uuid.UUID | None = None
    body_id: uuid.UUID | None = None
    superior_title_id: uuid.UUID | None = None
    holders_ids: list[uuid.UUID] | None = None
    symbols_ids: list[uuid.UUID] | None = None

    # World
    status: str | None = None
    history: str | None = None
    characters_ids: list[uuid.UUID] | None = None
    institutions_ids: list[uuid.UUID] | None = None
    families_ids: list[uuid.UUID] | None = None
    zones_ids: list[uuid.UUID] | None = None
    locations_ids: list[uuid.UUID] | None = None
    objects_ids: list[uuid.UUID] | None = None
    constructs_ids: list[uuid.UUID] | None = None
    laws_ids: list[uuid.UUID] | None = None
    collectives_ids: list[uuid.UUID] | None = None
    creatures_ids: list[uuid.UUID] | None = None
    phenomena_ids: list[uuid.UUID] | None = None
    species_ids: list[uuid.UUID] | None = None
    languages_ids: list[uuid.UUID] | None = None


class TitleCreateInSchema(TitleBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class TitleUpdateInSchema(TitleBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class TitleFilterSchema(BaseFilterSchema):
    issuer_id: uuid.UUID | None = Field(None, q='issuer_id')
    body_id: uuid.UUID | None = Field(None, q='body_id')
    superior_title_id: uuid.UUID | None = Field(None, q='superior_title_id')
    holders_ids: uuid.UUID | None = Field(None, q='holders__id')
    symbols_ids: uuid.UUID | None = Field(None, q='symbols__id')
    characters_ids: uuid.UUID | None = Field(None, q='characters__id')
    institutions_ids: uuid.UUID | None = Field(None, q='institutions__id')
    families_ids: uuid.UUID | None = Field(None, q='families__id')
    zones_ids: uuid.UUID | None = Field(None, q='zones__id')
    locations_ids: uuid.UUID | None = Field(None, q='locations__id')
    objects_ids: uuid.UUID | None = Field(None, q='objects__id')
    constructs_ids: uuid.UUID | None = Field(None, q='constructs__id')
    laws_ids: uuid.UUID | None = Field(None, q='laws__id')
    collectives_ids: uuid.UUID | None = Field(None, q='collectives__id')
    creatures_ids: uuid.UUID | None = Field(None, q='creatures__id')
    phenomena_ids: uuid.UUID | None = Field(None, q='phenomena__id')
    species_ids: uuid.UUID | None = Field(None, q='species__id')
    languages_ids: uuid.UUID | None = Field(None, q='languages__id')


class TitleOutSchema(AbstractElementBaseSchema):

    # Mandate
    authority: str | None = None
    eligibility: str | None = None
    grant_date: int | None = None
    revoke_date: int | None = None
    issuer: ElementNestedOutSchema | None = None
    body: ElementNestedOutSchema | None = None
    superior_title: ElementNestedOutSchema | None = None
    holders: List[ElementNestedOutSchema] = []
    symbols: List[ElementNestedOutSchema] = []

    # World
    status: str | None = None
    history: str | None = None
    characters: List[ElementNestedOutSchema] = []
    institutions: List[ElementNestedOutSchema] = []
    families: List[ElementNestedOutSchema] = []
    zones: List[ElementNestedOutSchema] = []
    locations: List[ElementNestedOutSchema] = []
    objects: List[ElementNestedOutSchema] = []
    constructs: List[ElementNestedOutSchema] = []
    laws: List[ElementNestedOutSchema] = []
    collectives: List[ElementNestedOutSchema] = []
    creatures: List[ElementNestedOutSchema] = []
    phenomena: List[ElementNestedOutSchema] = []
    species: List[ElementNestedOutSchema] = []
    languages: List[ElementNestedOutSchema] = []

    @staticmethod
    def resolve_objects(obj) -> List[ElementNestedOutSchema]:
        """Resolves the 'objects' field overlap for django by querying the reverse M2M relation."""
        try:
            Object = apps.get_model("elements", "Object") 
            return list(Object.objects.filter(title_objects=obj)) # type: ignore
        except LookupError:
            print("Error: Could not find Object model in resolve_objects.")
            return []
        except AttributeError: 
            print(f"Error: Attribute error resolving objects for title {obj.pk}. Check related_name.")
            return []
        except Exception as e:
            print(f"Error resolving objects for title {obj.pk}: {e}")
            return []
