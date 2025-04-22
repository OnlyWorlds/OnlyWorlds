from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class LanguageBaseSchema(AbstractElementBaseSchema):

    # Syntax
    writing: str | None = None
    phonology: str | None = None
    grammar: str | None = None
    vocabulary: str | None = None
    classification_id: uuid.UUID | None = None

    # Spread
    prose: str | None = None
    speakers: int | None = None
    dialects_ids: list[uuid.UUID] | None = []
    range_ids: list[uuid.UUID] | None = []


class LanguageCreateInSchema(LanguageBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class LanguageUpdateInSchema(LanguageBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class LanguageFilterSchema(BaseFilterSchema):
    classification_id: uuid.UUID | None = Field(None, q='classification_id')
    dialects_ids: uuid.UUID | None = Field(None, q='dialects__id')
    range_ids: uuid.UUID | None = Field(None, q='range__id')


class LanguageOutSchema(AbstractElementBaseSchema):

    # Syntax
    writing: str | None = None
    phonology: str | None = None
    grammar: str | None = None
    vocabulary: str | None = None
    classification: ElementNestedOutSchema | None = None

    # Spread
    prose: str | None = None
    speakers: int | None = None
    dialects: List[ElementNestedOutSchema] = []
    range: List[ElementNestedOutSchema] = []

