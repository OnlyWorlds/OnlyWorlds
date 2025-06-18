from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class LawBaseSchema(AbstractElementBaseSchema):

    # Code
    declaration: str | None = None
    purpose: str | None = None
    date: int | None = None
    parent_law_id: uuid.UUID | None = None
    penalties_ids: list[uuid.UUID] | None = None

    # World
    author_id: uuid.UUID | None = None
    locations_ids: list[uuid.UUID] | None = None
    zones_ids: list[uuid.UUID] | None = None
    prohibitions_ids: list[uuid.UUID] | None = None
    adjudicators_ids: list[uuid.UUID] | None = None
    enforcers_ids: list[uuid.UUID] | None = None


class LawCreateInSchema(LawBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class LawUpdateInSchema(LawBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class LawFilterSchema(BaseFilterSchema):
    parent_law_id: uuid.UUID | None = Field(None, q='parent_law_id')
    penalties_ids: uuid.UUID | None = Field(None, q='penalties__id')
    author_id: uuid.UUID | None = Field(None, q='author_id')
    locations_ids: uuid.UUID | None = Field(None, q='locations__id')
    zones_ids: uuid.UUID | None = Field(None, q='zones__id')
    prohibitions_ids: uuid.UUID | None = Field(None, q='prohibitions__id')
    adjudicators_ids: uuid.UUID | None = Field(None, q='adjudicators__id')
    enforcers_ids: uuid.UUID | None = Field(None, q='enforcers__id')


class LawOutSchema(AbstractElementBaseSchema):

    # Code
    declaration: str | None = None
    purpose: str | None = None
    date: int | None = None
    parent_law: ElementNestedOutSchema | None = None
    penalties: List[ElementNestedOutSchema] = []

    # World
    author: ElementNestedOutSchema | None = None
    locations: List[ElementNestedOutSchema] = []
    zones: List[ElementNestedOutSchema] = []
    prohibitions: List[ElementNestedOutSchema] = []
    adjudicators: List[ElementNestedOutSchema] = []
    enforcers: List[ElementNestedOutSchema] = []

