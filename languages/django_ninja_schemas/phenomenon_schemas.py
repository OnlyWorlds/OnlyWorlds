from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class PhenomenonBaseSchema(AbstractElementBaseSchema):

    # Mechanics
    expression: str | None = None
    effects: str | None = None
    duration: int | None = None
    catalysts_ids: list[uuid.UUID] | None = None
    empowerments_ids: list[uuid.UUID] | None = None

    # World
    mythology: str | None = None
    system_id: uuid.UUID | None = None
    triggers_ids: list[uuid.UUID] | None = None
    wielders_ids: list[uuid.UUID] | None = None
    environments_ids: list[uuid.UUID] | None = None


class PhenomenonCreateInSchema(PhenomenonBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class PhenomenonUpdateInSchema(PhenomenonBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class PhenomenonFilterSchema(BaseFilterSchema):
    catalysts_ids: uuid.UUID | None = Field(None, q='catalysts__id')
    empowerments_ids: uuid.UUID | None = Field(None, q='empowerments__id')
    system_id: uuid.UUID | None = Field(None, q='system_id')
    triggers_ids: uuid.UUID | None = Field(None, q='triggers__id')
    wielders_ids: uuid.UUID | None = Field(None, q='wielders__id')
    environments_ids: uuid.UUID | None = Field(None, q='environments__id')


class PhenomenonOutSchema(AbstractElementBaseSchema):

    # Mechanics
    expression: str | None = None
    effects: str | None = None
    duration: int | None = None
    catalysts: List[ElementNestedOutSchema] = []
    empowerments: List[ElementNestedOutSchema] = []

    # World
    mythology: str | None = None
    system: ElementNestedOutSchema | None = None
    triggers: List[ElementNestedOutSchema] = []
    wielders: List[ElementNestedOutSchema] = []
    environments: List[ElementNestedOutSchema] = []

