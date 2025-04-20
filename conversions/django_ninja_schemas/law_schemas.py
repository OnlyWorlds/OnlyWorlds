from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List
import uuid


class LawBaseSchema(AbstractElementBaseSchema):

    # Code
    decree: str | None = None
    date: int | None = None
    purpose: str | None = None
    author_id: uuid.UUID | None = None

    # Compulsion
    jurisdictions_ids: list[uuid.UUID] | None = None
    prohibitions_ids: list[uuid.UUID] | None = None
    penalties_ids: list[uuid.UUID] | None = None
    adjudicators_ids: list[uuid.UUID] | None = None
    enforcers_ids: list[uuid.UUID] | None = None


class LawCreateInSchema(LawBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class LawUpdateInSchema(LawBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class LawFilterSchema(BaseFilterSchema):
    author_id: uuid.UUID | None = Field(None, q='author_id')
    jurisdictions_ids: uuid.UUID | None = Field(None, q='jurisdictions__id')
    prohibitions_ids: uuid.UUID | None = Field(None, q='prohibitions__id')
    penalties_ids: uuid.UUID | None = Field(None, q='penalties__id')
    adjudicators_ids: uuid.UUID | None = Field(None, q='adjudicators__id')
    enforcers_ids: uuid.UUID | None = Field(None, q='enforcers__id')


class LawOutSchema(AbstractElementBaseSchema):

    # Code
    decree: str | None = None
    date: int | None = None
    purpose: str | None = None
    author: ElementNestedOutSchema | None = None

    # Compulsion
    jurisdictions: List[ElementNestedOutSchema] = []
    prohibitions: List[ElementNestedOutSchema] = []
    penalties: List[ElementNestedOutSchema] = []
    adjudicators: List[ElementNestedOutSchema] = []
    enforcers: List[ElementNestedOutSchema] = []

