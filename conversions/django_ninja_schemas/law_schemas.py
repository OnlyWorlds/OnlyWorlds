from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class LawBaseSchema(AbstractElementBaseSchema):

    # Code
    decree: str | None = None
    date: int | None = None
    purpose: str | None = None
    author: uuid.UUID | None = None

    # Compulsion
    jurisdictions: list[uuid.UUID] | None = None
    prohibitions: list[uuid.UUID] | None = None
    penalties: list[uuid.UUID] | None = None
    adjudicators: list[uuid.UUID] | None = None
    enforcers: list[uuid.UUID] | None = None


class LawCreateInSchema(LawBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class LawUpdateInSchema(LawBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class LawFilterSchema(BaseFilterSchema):
    author_id: Optional[uuid.UUID] = Field(None, q='author_id')
    jurisdictions_ids: Optional[uuid.UUID] = Field(None, q='jurisdictions__id')
    prohibitions_ids: Optional[uuid.UUID] = Field(None, q='prohibitions__id')
    penalties_ids: Optional[uuid.UUID] = Field(None, q='penalties__id')
    adjudicators_ids: Optional[uuid.UUID] = Field(None, q='adjudicators__id')
    enforcers_ids: Optional[uuid.UUID] = Field(None, q='enforcers__id')


class LawOutSchema(AbstractElementBaseSchema):

    # Code
    decree: str | None = None
    date: int | None = None
    purpose: str | None = None
    author: Optional[ElementNestedOutSchema] = None

    # Compulsion
    jurisdictions: List[ElementNestedOutSchema] = []
    prohibitions: List[ElementNestedOutSchema] = []
    penalties: List[ElementNestedOutSchema] = []
    adjudicators: List[ElementNestedOutSchema] = []
    enforcers: List[ElementNestedOutSchema] = []

