from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class PhenomenonBaseSchema(AbstractElementBaseSchema):

    # Manifest
    presence: str | None = None
    scope: str | None = None
    duration: int | None = None
    intensity: str | None = None
    empowerments: list[uuid.UUID] | None = None
    environments: list[uuid.UUID] | None = None
    carriers: list[uuid.UUID] | None = None

    # Actuate
    effect: str | None = None
    catalysts: uuid.UUID | None = None
    wielders: list[uuid.UUID] | None = None
    handlers: list[uuid.UUID] | None = None
    enablers: list[uuid.UUID] | None = None
    triggers: list[uuid.UUID] | None = None
    affinity: list[uuid.UUID] | None = None


class PhenomenonCreateInSchema(PhenomenonBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class PhenomenonUpdateInSchema(PhenomenonBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class PhenomenonFilterSchema(BaseFilterSchema):
    empowerments_ids: Optional[uuid.UUID] = Field(None, q='empowerments__id')
    environments_ids: Optional[uuid.UUID] = Field(None, q='environments__id')
    carriers_ids: Optional[uuid.UUID] = Field(None, q='carriers__id')
    catalysts_id: Optional[uuid.UUID] = Field(None, q='catalysts_id')
    wielders_ids: Optional[uuid.UUID] = Field(None, q='wielders__id')
    handlers_ids: Optional[uuid.UUID] = Field(None, q='handlers__id')
    enablers_ids: Optional[uuid.UUID] = Field(None, q='enablers__id')
    triggers_ids: Optional[uuid.UUID] = Field(None, q='triggers__id')
    affinity_ids: Optional[uuid.UUID] = Field(None, q='affinity__id')


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
    catalysts: Optional[ElementNestedOutSchema] = None
    wielders: List[ElementNestedOutSchema] = []
    handlers: List[ElementNestedOutSchema] = []
    enablers: List[ElementNestedOutSchema] = []
    triggers: List[ElementNestedOutSchema] = []
    affinity: List[ElementNestedOutSchema] = []

