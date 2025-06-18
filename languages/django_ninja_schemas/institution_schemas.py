from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class InstitutionBaseSchema(AbstractElementBaseSchema):

    # Foundation
    doctrine: str | None = None
    founding_date: int | None = None
    parent_institution_id: uuid.UUID | None = None

    # Claims
    legislation_ids: list[uuid.UUID] | None = None
    zones_ids: list[uuid.UUID] | None = None
    objects_ids: list[uuid.UUID] | None = None
    creatures_ids: list[uuid.UUID] | None = None

    # World
    status: str | None = None
    allies_ids: list[uuid.UUID] | None = None
    adversaries_ids: list[uuid.UUID] | None = None
    constructs_ids: list[uuid.UUID] | None = None


class InstitutionCreateInSchema(InstitutionBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class InstitutionUpdateInSchema(InstitutionBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class InstitutionFilterSchema(BaseFilterSchema):
    parent_institution_id: uuid.UUID | None = Field(None, q='parent_institution_id')
    legislation_ids: uuid.UUID | None = Field(None, q='legislation__id')
    zones_ids: uuid.UUID | None = Field(None, q='zones__id')
    objects_ids: uuid.UUID | None = Field(None, q='objects__id')
    creatures_ids: uuid.UUID | None = Field(None, q='creatures__id')
    allies_ids: uuid.UUID | None = Field(None, q='allies__id')
    adversaries_ids: uuid.UUID | None = Field(None, q='adversaries__id')
    constructs_ids: uuid.UUID | None = Field(None, q='constructs__id')


class InstitutionOutSchema(AbstractElementBaseSchema):

    # Foundation
    doctrine: str | None = None
    founding_date: int | None = None
    parent_institution: ElementNestedOutSchema | None = None

    # Claims
    legislation: List[ElementNestedOutSchema] = []
    zones: List[ElementNestedOutSchema] = []
    objects: List[ElementNestedOutSchema] = []
    creatures: List[ElementNestedOutSchema] = []

    # World
    status: str | None = None
    allies: List[ElementNestedOutSchema] = []
    adversaries: List[ElementNestedOutSchema] = []
    constructs: List[ElementNestedOutSchema] = []

