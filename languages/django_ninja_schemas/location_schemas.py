from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field # type: ignore
from typing import List
import uuid


class LocationBaseSchema(AbstractElementBaseSchema):

    # Setting
    form: str | None = None
    function: str | None = None
    founding_date: int | None = None
    parent_location_id: uuid.UUID | None = None
    populations_ids: list[uuid.UUID] | None = None

    # Politics
    political_climate: str | None = None
    primary_power_id: uuid.UUID | None = None
    governing_title_id: uuid.UUID | None = None
    secondary_powers_ids: list[uuid.UUID] | None = None
    zone_id: uuid.UUID | None = None
    rival_id: uuid.UUID | None = None
    partner_id: uuid.UUID | None = None

    # Production
    extraction_methods_ids: list[uuid.UUID] | None = None
    extraction_goods_ids: list[uuid.UUID] | None = None
    industry_methods_ids: list[uuid.UUID] | None = None
    industry_goods_ids: list[uuid.UUID] | None = None

    # Commerce
    infrastructure: str | None = None
    extraction_markets_ids: list[uuid.UUID] | None = None
    industry_markets_ids: list[uuid.UUID] | None = None
    currencies_ids: list[uuid.UUID] | None = None

    # Construction
    architecture: str | None = None
    buildings_ids: list[uuid.UUID] | None = None
    building_methods_ids: list[uuid.UUID] | None = None

    # World
    customs: str | None = None
    founders_ids: list[uuid.UUID] | None = None
    cults_ids: list[uuid.UUID] | None = None
    delicacies_ids: list[uuid.UUID] | None = None

    # Defense
    defensibility: str | None = None
    elevation: int | None = None
    fighters_ids: list[uuid.UUID] | None = None
    defensive_objects_ids: list[uuid.UUID] | None = None


class LocationCreateInSchema(LocationBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)


class LocationUpdateInSchema(LocationBaseSchema):
    id: uuid.UUID | None = Field(None, exclude=True)
    name: str | None = None


class LocationFilterSchema(BaseFilterSchema):
    parent_location_id: uuid.UUID | None = Field(None, q='parent_location_id')
    populations_ids: uuid.UUID | None = Field(None, q='populations__id')
    primary_power_id: uuid.UUID | None = Field(None, q='primary_power_id')
    governing_title_id: uuid.UUID | None = Field(None, q='governing_title_id')
    secondary_powers_ids: uuid.UUID | None = Field(None, q='secondary_powers__id')
    zone_id: uuid.UUID | None = Field(None, q='zone_id')
    rival_id: uuid.UUID | None = Field(None, q='rival_id')
    partner_id: uuid.UUID | None = Field(None, q='partner_id')
    extraction_methods_ids: uuid.UUID | None = Field(None, q='extraction_methods__id')
    extraction_goods_ids: uuid.UUID | None = Field(None, q='extraction_goods__id')
    industry_methods_ids: uuid.UUID | None = Field(None, q='industry_methods__id')
    industry_goods_ids: uuid.UUID | None = Field(None, q='industry_goods__id')
    extraction_markets_ids: uuid.UUID | None = Field(None, q='extraction_markets__id')
    industry_markets_ids: uuid.UUID | None = Field(None, q='industry_markets__id')
    currencies_ids: uuid.UUID | None = Field(None, q='currencies__id')
    buildings_ids: uuid.UUID | None = Field(None, q='buildings__id')
    building_methods_ids: uuid.UUID | None = Field(None, q='building_methods__id')
    founders_ids: uuid.UUID | None = Field(None, q='founders__id')
    cults_ids: uuid.UUID | None = Field(None, q='cults__id')
    delicacies_ids: uuid.UUID | None = Field(None, q='delicacies__id')
    fighters_ids: uuid.UUID | None = Field(None, q='fighters__id')
    defensive_objects_ids: uuid.UUID | None = Field(None, q='defensive_objects__id')


class LocationOutSchema(AbstractElementBaseSchema):

    # Setting
    form: str | None = None
    function: str | None = None
    founding_date: int | None = None
    parent_location: ElementNestedOutSchema | None = None
    populations: List[ElementNestedOutSchema] = []

    # Politics
    political_climate: str | None = None
    primary_power: ElementNestedOutSchema | None = None
    governing_title: ElementNestedOutSchema | None = None
    secondary_powers: List[ElementNestedOutSchema] = []
    zone: ElementNestedOutSchema | None = None
    rival: ElementNestedOutSchema | None = None
    partner: ElementNestedOutSchema | None = None

    # Production
    extraction_methods: List[ElementNestedOutSchema] = []
    extraction_goods: List[ElementNestedOutSchema] = []
    industry_methods: List[ElementNestedOutSchema] = []
    industry_goods: List[ElementNestedOutSchema] = []

    # Commerce
    infrastructure: str | None = None
    extraction_markets: List[ElementNestedOutSchema] = []
    industry_markets: List[ElementNestedOutSchema] = []
    currencies: List[ElementNestedOutSchema] = []

    # Construction
    architecture: str | None = None
    buildings: List[ElementNestedOutSchema] = []
    building_methods: List[ElementNestedOutSchema] = []

    # World
    customs: str | None = None
    founders: List[ElementNestedOutSchema] = []
    cults: List[ElementNestedOutSchema] = []
    delicacies: List[ElementNestedOutSchema] = []

    # Defense
    defensibility: str | None = None
    elevation: int | None = None
    fighters: List[ElementNestedOutSchema] = []
    defensive_objects: List[ElementNestedOutSchema] = []

