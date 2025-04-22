from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class PhenomenonBaseSchema(AbstractElementBaseSchema):

    # Manifest
    presence: str | None = None
    scope: str | None = None
    duration: int | None = None
    intensity: str | None = None
    empowerments_ids: list[uuid.UUID] | None = []
    environments_ids: list[uuid.UUID] | None = []
    carriers_ids: list[uuid.UUID] | None = []

    # Actuate
    effect: str | None = None
    catalysts_id: uuid.UUID | None = None
    wielders_ids: list[uuid.UUID] | None = []
    handlers_ids: list[uuid.UUID] | None = []
    enablers_ids: list[uuid.UUID] | None = []
    triggers_ids: list[uuid.UUID] | None = []
    affinity_ids: list[uuid.UUID] | None = []


class PhenomenonCreateInSchema(PhenomenonBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class PhenomenonUpdateInSchema(PhenomenonBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class PhenomenonFilterSchema(BaseFilterSchema):
    empowerments_ids: uuid.UUID | None = Field(None, q='empowerments__id')
    environments_ids: uuid.UUID | None = Field(None, q='environments__id')
    carriers_ids: uuid.UUID | None = Field(None, q='carriers__id')
    catalysts_id: uuid.UUID | None = Field(None, q='catalysts_id')
    wielders_ids: uuid.UUID | None = Field(None, q='wielders__id')
    handlers_ids: uuid.UUID | None = Field(None, q='handlers__id')
    enablers_ids: uuid.UUID | None = Field(None, q='enablers__id')
    triggers_ids: uuid.UUID | None = Field(None, q='triggers__id')
    affinity_ids: uuid.UUID | None = Field(None, q='affinity__id')


class PhenomenonOutSchema(AbstractElementBaseSchema):

    # Manifest
    presence: str | None = None
    scope: str | None = None
    duration: int | None = None
    intensity: str | None = None
    empowerments: List[ElementNestedOutSchema] = []
    environments: List[ElementNestedOutSchema] = []
    carriers: List[ElementNestedOutSchema] = []

    # Actuate
    effect: str | None = None
    catalysts: ElementNestedOutSchema | None = None
    wielders: List[ElementNestedOutSchema] = []
    handlers: List[ElementNestedOutSchema] = []
    enablers: List[ElementNestedOutSchema] = []
    triggers: List[ElementNestedOutSchema] = []
    affinity: List[ElementNestedOutSchema] = []

