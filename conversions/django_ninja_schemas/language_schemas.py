from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class LanguageBaseSchema(AbstractElementBaseSchema):

    # Syntax
    writing: str | None = None
    phonology: str | None = None
    grammar: str | None = None
    vocabulary: str | None = None
    classification: uuid.UUID | None = None

    # Spread
    prose: str | None = None
    speakers: int | None = None
    dialects: list[uuid.UUID] | None = None
    range: list[uuid.UUID] | None = None


class LanguageCreateInSchema(LanguageBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class LanguageUpdateInSchema(LanguageBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class LanguageFilterSchema(BaseFilterSchema):
    classification_id: Optional[uuid.UUID] = Field(None, q='classification_id')
    dialects_ids: Optional[uuid.UUID] = Field(None, q='dialects__id')
    range_ids: Optional[uuid.UUID] = Field(None, q='range__id')


class LanguageOutSchema(AbstractElementBaseSchema):

    # Syntax
    writing: str | None = None
    phonology: str | None = None
    grammar: str | None = None
    vocabulary: str | None = None
    classification: Optional[ElementNestedOutSchema] = None

    # Spread
    prose: str | None = None
    speakers: int | None = None
    dialects: List[ElementNestedOutSchema] = []
    range: List[ElementNestedOutSchema] = []

