from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class FamilyBaseSchema(AbstractElementBaseSchema):

    # Identity
    spirit: str | None = None
    history: str | None = None
    traditions_ids: list[uuid.UUID] | None = None
    traits_ids: list[uuid.UUID] | None = None
    abilities_ids: list[uuid.UUID] | None = None
    languages_ids: list[uuid.UUID] | None = None
    ancestors_ids: list[uuid.UUID] | None = None

    # World
    reputation: str | None = None
    estates_ids: list[uuid.UUID] | None = None
    governs_ids: list[uuid.UUID] | None = None
    heirlooms_ids: list[uuid.UUID] | None = None
    creatures_ids: list[uuid.UUID] | None = None


class FamilyCreateInSchema(FamilyBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class FamilyUpdateInSchema(FamilyBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class FamilyFilterSchema(BaseFilterSchema):
    traditions_ids: uuid.UUID | None = Field(None, q='traditions__id')
    traits_ids: uuid.UUID | None = Field(None, q='traits__id')
    abilities_ids: uuid.UUID | None = Field(None, q='abilities__id')
    languages_ids: uuid.UUID | None = Field(None, q='languages__id')
    ancestors_ids: uuid.UUID | None = Field(None, q='ancestors__id')
    estates_ids: uuid.UUID | None = Field(None, q='estates__id')
    governs_ids: uuid.UUID | None = Field(None, q='governs__id')
    heirlooms_ids: uuid.UUID | None = Field(None, q='heirlooms__id')
    creatures_ids: uuid.UUID | None = Field(None, q='creatures__id')


class FamilyOutSchema(AbstractElementBaseSchema):

    # Identity
    spirit: str | None = None
    history: str | None = None
    traditions: List[ElementNestedOutSchema] = []
    traits: List[ElementNestedOutSchema] = []
    abilities: List[ElementNestedOutSchema] = []
    languages: List[ElementNestedOutSchema] = []
    ancestors: List[ElementNestedOutSchema] = []

    # World
    reputation: str | None = None
    estates: List[ElementNestedOutSchema] = []
    governs: List[ElementNestedOutSchema] = []
    heirlooms: List[ElementNestedOutSchema] = []
    creatures: List[ElementNestedOutSchema] = []

