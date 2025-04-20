from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class InstitutionBaseSchema(AbstractElementBaseSchema):

    # Foundation
    premise: str | None = None
    found_date: int | None = None
    end_date: int | None = None
    parent_institution: uuid.UUID | None = None

    # Claim
    territories: list[uuid.UUID] | None = None
    objects: list[uuid.UUID] | None = None
    creatures: list[uuid.UUID] | None = None
    legal: list[uuid.UUID] | None = None

    # World
    situation: str | None = None
    cooperates: list[uuid.UUID] | None = None
    competition: list[uuid.UUID] | None = None
    constructs: list[uuid.UUID] | None = None
    phenomena: list[uuid.UUID] | None = None


class InstitutionCreateInSchema(InstitutionBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class InstitutionUpdateInSchema(InstitutionBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class InstitutionFilterSchema(BaseFilterSchema):
    parent_institution_id: Optional[uuid.UUID] = Field(None, q='parent_institution_id')
    territories_ids: Optional[uuid.UUID] = Field(None, q='territories__id')
    objects_ids: Optional[uuid.UUID] = Field(None, q='objects__id')
    creatures_ids: Optional[uuid.UUID] = Field(None, q='creatures__id')
    legal_ids: Optional[uuid.UUID] = Field(None, q='legal__id')
    cooperates_ids: Optional[uuid.UUID] = Field(None, q='cooperates__id')
    competition_ids: Optional[uuid.UUID] = Field(None, q='competition__id')
    constructs_ids: Optional[uuid.UUID] = Field(None, q='constructs__id')
    phenomena_ids: Optional[uuid.UUID] = Field(None, q='phenomena__id')


class InstitutionOutSchema(AbstractElementBaseSchema):

    # Foundation
    premise: str | None = None
    found_date: int | None = None
    end_date: int | None = None
    parent_institution: Optional[ElementNestedOutSchema] = None

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

