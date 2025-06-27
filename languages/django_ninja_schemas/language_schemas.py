from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class LanguageBaseSchema(AbstractElementBaseSchema):

    # Structure
    phonology: str | None = None
    grammar: str | None = None
    lexicon: str | None = None
    writing: str | None = None
    classification_id: uuid.UUID | None = None

    # World
    status: str | None = None
    spread_ids: list[uuid.UUID] | None = None
    dialects_ids: list[uuid.UUID] | None = None


class LanguageCreateInSchema(LanguageBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class LanguageUpdateInSchema(LanguageBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class LanguageFilterSchema(BaseFilterSchema):
    classification_id: uuid.UUID | None = Field(None, q='classification_id')
    spread_ids: uuid.UUID | None = Field(None, q='spread__id')
    dialects_ids: uuid.UUID | None = Field(None, q='dialects__id')


class LanguageOutSchema(AbstractElementBaseSchema):

    # Structure
    phonology: str | None = None
    grammar: str | None = None
    lexicon: str | None = None
    writing: str | None = None
    classification: ElementNestedOutSchema | None = None

    # World
    status: str | None = None
    spread: List[ElementNestedOutSchema] = []
    dialects: List[ElementNestedOutSchema] = []

