from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List
import uuid


class InstitutionBaseSchema(AbstractElementBaseSchema):

    # Foundation
    premise: str | None = None
    found_date: int | None = None
    end_date: int | None = None
    parent_institution_id: uuid.UUID | None = None

    # Claim
    territories_ids: list[uuid.UUID] | None = None
    objects_ids: list[uuid.UUID] | None = None
    creatures_ids: list[uuid.UUID] | None = None
    legal_ids: list[uuid.UUID] | None = None

    # World
    situation: str | None = None
    cooperates_ids: list[uuid.UUID] | None = None
    competition_ids: list[uuid.UUID] | None = None
    constructs_ids: list[uuid.UUID] | None = None
    phenomena_ids: list[uuid.UUID] | None = None


class InstitutionCreateInSchema(InstitutionBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class InstitutionUpdateInSchema(InstitutionBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class InstitutionFilterSchema(BaseFilterSchema):
    parent_institution_id: uuid.UUID | None = Field(None, q='parent_institution_id')
    territories_ids: uuid.UUID | None = Field(None, q='territories__id')
    objects_ids: uuid.UUID | None = Field(None, q='objects__id')
    creatures_ids: uuid.UUID | None = Field(None, q='creatures__id')
    legal_ids: uuid.UUID | None = Field(None, q='legal__id')
    cooperates_ids: uuid.UUID | None = Field(None, q='cooperates__id')
    competition_ids: uuid.UUID | None = Field(None, q='competition__id')
    constructs_ids: uuid.UUID | None = Field(None, q='constructs__id')
    phenomena_ids: uuid.UUID | None = Field(None, q='phenomena__id')


class InstitutionOutSchema(AbstractElementBaseSchema):

    # Foundation
    premise: str | None = None
    found_date: int | None = None
    end_date: int | None = None
    parent_institution: ElementNestedOutSchema | None = None

    # Claim
    territories: List[ElementNestedOutSchema] = []
    objects: List[ElementNestedOutSchema] = []
    creatures: List[ElementNestedOutSchema] = []
    legal: List[ElementNestedOutSchema] = []

    # World
    situation: str | None = None
    cooperates: List[ElementNestedOutSchema] = []
    competition: List[ElementNestedOutSchema] = []
    constructs: List[ElementNestedOutSchema] = []
    phenomena: List[ElementNestedOutSchema] = []

