from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class FamilyBaseSchema(AbstractElementBaseSchema):

    # Community
    spirit: str | None = None
    alliances_ids: list[uuid.UUID] | None = None
    rivalries_ids: list[uuid.UUID] | None = None

    # Lineage
    history: str | None = None
    ancestors_ids: list[uuid.UUID] | None = None
    traits_ids: list[uuid.UUID] | None = None
    abilities_ids: list[uuid.UUID] | None = None
    languages_ids: list[uuid.UUID] | None = None

    # World
    status: str | None = None
    competition_ids: list[uuid.UUID] | None = None
    administrates_ids: list[uuid.UUID] | None = None
    creatures_ids: list[uuid.UUID] | None = None

    # Legacy
    traditions: str | None = None
    estate_id: uuid.UUID | None = None
    heirlooms_ids: list[uuid.UUID] | None = None


class FamilyCreateInSchema(FamilyBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class FamilyUpdateInSchema(FamilyBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class FamilyFilterSchema(BaseFilterSchema):
    alliances_ids: uuid.UUID | None = Field(None, q='alliances__id')
    rivalries_ids: uuid.UUID | None = Field(None, q='rivalries__id')
    ancestors_ids: uuid.UUID | None = Field(None, q='ancestors__id')
    traits_ids: uuid.UUID | None = Field(None, q='traits__id')
    abilities_ids: uuid.UUID | None = Field(None, q='abilities__id')
    languages_ids: uuid.UUID | None = Field(None, q='languages__id')
    competition_ids: uuid.UUID | None = Field(None, q='competition__id')
    administrates_ids: uuid.UUID | None = Field(None, q='administrates__id')
    creatures_ids: uuid.UUID | None = Field(None, q='creatures__id')
    estate_id: uuid.UUID | None = Field(None, q='estate_id')
    heirlooms_ids: uuid.UUID | None = Field(None, q='heirlooms__id')


class FamilyOutSchema(AbstractElementBaseSchema):

    # Community
    spirit: str | None = None
    alliances: List[ElementNestedOutSchema] = []
    rivalries: List[ElementNestedOutSchema] = []

    # Lineage
    history: str | None = None
    ancestors: List[ElementNestedOutSchema] = []
    traits: List[ElementNestedOutSchema] = []
    abilities: List[ElementNestedOutSchema] = []
    languages: List[ElementNestedOutSchema] = []

    # World
    status: str | None = None
    competition: List[ElementNestedOutSchema] = []
    administrates: List[ElementNestedOutSchema] = []
    creatures: List[ElementNestedOutSchema] = []

    # Legacy
    traditions: str | None = None
    estate: ElementNestedOutSchema | None = None
    heirlooms: List[ElementNestedOutSchema] = []

