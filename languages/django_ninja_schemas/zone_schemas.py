from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class ZoneBaseSchema(AbstractElementBaseSchema):

    # Scope
    function: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    phenomena_ids: list[uuid.UUID] | None = None

    # World
    history: str | None = None
    claimed_by_ids: list[uuid.UUID] | None = None
    roamed_by_ids: list[uuid.UUID] | None = None
    titles_ids: list[uuid.UUID] | None = None


class ZoneCreateInSchema(ZoneBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class ZoneUpdateInSchema(ZoneBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class ZoneFilterSchema(BaseFilterSchema):
    phenomena_ids: uuid.UUID | None = Field(None, q='phenomena__id')
    claimed_by_ids: uuid.UUID | None = Field(None, q='claimed_by__id')
    roamed_by_ids: uuid.UUID | None = Field(None, q='roamed_by__id')
    titles_ids: uuid.UUID | None = Field(None, q='titles__id')


class ZoneOutSchema(AbstractElementBaseSchema):

    # Scope
    function: str | None = None
    start_date: int | None = None
    end_date: int | None = None
    phenomena: List[ElementNestedOutSchema] = []

    # World
    history: str | None = None
    claimed_by: List[ElementNestedOutSchema] = []
    roamed_by: List[ElementNestedOutSchema] = []
    titles: List[ElementNestedOutSchema] = []

