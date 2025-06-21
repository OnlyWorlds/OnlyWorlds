from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class ZoneBaseSchema(AbstractElementBaseSchema):

    # Scope
    role: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    phenomena_ids: list[uuid.UUID] | None = None
    linked_zones_ids: list[uuid.UUID] | None = None

    # World
    context: str | None = None
    populations_ids: list[uuid.UUID] | None = None
    titles_ids: list[uuid.UUID] | None = None
    principles_ids: list[uuid.UUID] | None = None


class ZoneCreateInSchema(ZoneBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class ZoneUpdateInSchema(ZoneBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class ZoneFilterSchema(BaseFilterSchema):
    phenomena_ids: uuid.UUID | None = Field(None, q='phenomena__id')
    linked_zones_ids: uuid.UUID | None = Field(None, q='linked_zones__id')
    populations_ids: uuid.UUID | None = Field(None, q='populations__id')
    titles_ids: uuid.UUID | None = Field(None, q='titles__id')
    principles_ids: uuid.UUID | None = Field(None, q='principles__id')


class ZoneOutSchema(AbstractElementBaseSchema):

    # Scope
    role: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    phenomena: List[ElementNestedOutSchema] = []
    linked_zones: List[ElementNestedOutSchema] = []

    # World
    context: str | None = None
    populations: List[ElementNestedOutSchema] = []
    titles: List[ElementNestedOutSchema] = []
    principles: List[ElementNestedOutSchema] = []

