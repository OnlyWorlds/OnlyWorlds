from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class FamilyBaseSchema(AbstractElementBaseSchema):

    # Community
    spirit: str | None = None
    alliances: list[uuid.UUID] | None = None
    rivalries: list[uuid.UUID] | None = None

    # Lineage
    history: str | None = None
    ancestors: list[uuid.UUID] | None = None
    traits: list[uuid.UUID] | None = None
    abilities: list[uuid.UUID] | None = None
    languages: list[uuid.UUID] | None = None

    # World
    status: str | None = None
    competition: list[uuid.UUID] | None = None
    administrates: list[uuid.UUID] | None = None
    creatures: list[uuid.UUID] | None = None

    # Legacy
    traditions: str | None = None
    estate: uuid.UUID | None = None
    heirlooms: list[uuid.UUID] | None = None


class FamilyCreateInSchema(FamilyBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class FamilyUpdateInSchema(FamilyBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class FamilyFilterSchema(BaseFilterSchema):
    alliances_ids: Optional[uuid.UUID] = Field(None, q='alliances__id')
    rivalries_ids: Optional[uuid.UUID] = Field(None, q='rivalries__id')
    ancestors_ids: Optional[uuid.UUID] = Field(None, q='ancestors__id')
    traits_ids: Optional[uuid.UUID] = Field(None, q='traits__id')
    abilities_ids: Optional[uuid.UUID] = Field(None, q='abilities__id')
    languages_ids: Optional[uuid.UUID] = Field(None, q='languages__id')
    competition_ids: Optional[uuid.UUID] = Field(None, q='competition__id')
    administrates_ids: Optional[uuid.UUID] = Field(None, q='administrates__id')
    creatures_ids: Optional[uuid.UUID] = Field(None, q='creatures__id')
    estate_id: Optional[uuid.UUID] = Field(None, q='estate_id')
    heirlooms_ids: Optional[uuid.UUID] = Field(None, q='heirlooms__id')


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
    estate: Optional[ElementNestedOutSchema] = None
    heirlooms: List[ElementNestedOutSchema] = []

