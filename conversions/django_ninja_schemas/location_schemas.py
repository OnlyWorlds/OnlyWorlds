from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema
from ninja import Field, FilterSchema  # type: ignore
from typing import List, Optional
import uuid


class LocationBaseSchema(AbstractElementBaseSchema):

    # Locality
    scene: str | None = None
    activity: str | None = None
    founding_date: int | None = None
    population_size: int | None = None
    parent_location: uuid.UUID | None = None
    populations: list[uuid.UUID] | None = None

    # Culture
    traditions: str | None = None
    celebrations: str | None = None
    primary_cult: uuid.UUID | None = None
    secondary_cults: list[uuid.UUID] | None = None
    delicacies: list[uuid.UUID] | None = None

    # World
    coordinates: str | None = None
    founders: list[uuid.UUID] | None = None

    # Construction
    logistics: str | None = None
    architecture: str | None = None
    construction_rate: int | None = Field(None, le=100)
    buildings: list[uuid.UUID] | None = None
    building_expertise: list[uuid.UUID] | None = None

    # Production
    extraction: str | None = None
    industry: str | None = None
    extraction_output: int | None = None
    industry_output: int | None = None
    primary_resource: uuid.UUID | None = None
    primary_industry: uuid.UUID | None = None
    secondary_resources: list[uuid.UUID] | None = None
    secondary_industries: list[uuid.UUID] | None = None

    # Commerce
    trade: str | None = None
    infrastructure: str | None = None
    currency: str | None = None
    primary_extraction_market: uuid.UUID | None = None
    primary_industry_market: uuid.UUID | None = None
    secondary_extraction_markets: list[uuid.UUID] | None = None
    secondary_industry_markets: list[uuid.UUID] | None = None

    # Localpolitics
    government: str | None = None
    opposition: str | None = None
    governing_title: uuid.UUID | None = None
    primary_faction: uuid.UUID | None = None
    secondary_factions: list[uuid.UUID] | None = None

    # Regionalpolitics
    territorial_policies: str | None = None
    territory: uuid.UUID | None = None
    rival: uuid.UUID | None = None
    friend: uuid.UUID | None = None
    soft_influence_on: list[uuid.UUID] | None = None
    hard_influence_on: list[uuid.UUID] | None = None

    # Strategics
    defensibility: str | None = None
    height: int | None = None
    primary_fighter: uuid.UUID | None = None
    secondary_fighters: list[uuid.UUID] | None = None
    defenses: list[uuid.UUID] | None = None
    fortifications: list[uuid.UUID] | None = None


class LocationCreateInSchema(LocationBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)


class LocationUpdateInSchema(LocationBaseSchema):
    id: Optional[uuid.UUID] = Field(None, exclude=True)
    name: Optional[str] = None


class LocationFilterSchema(BaseFilterSchema):
    parent_location_id: Optional[uuid.UUID] = Field(None, q='parent_location_id')
    populations_ids: Optional[uuid.UUID] = Field(None, q='populations__id')
    primary_cult_id: Optional[uuid.UUID] = Field(None, q='primary_cult_id')
    secondary_cults_ids: Optional[uuid.UUID] = Field(None, q='secondary_cults__id')
    delicacies_ids: Optional[uuid.UUID] = Field(None, q='delicacies__id')
    founders_ids: Optional[uuid.UUID] = Field(None, q='founders__id')
    buildings_ids: Optional[uuid.UUID] = Field(None, q='buildings__id')
    building_expertise_ids: Optional[uuid.UUID] = Field(None, q='building_expertise__id')
    primary_resource_id: Optional[uuid.UUID] = Field(None, q='primary_resource_id')
    primary_industry_id: Optional[uuid.UUID] = Field(None, q='primary_industry_id')
    secondary_resources_ids: Optional[uuid.UUID] = Field(None, q='secondary_resources__id')
    secondary_industries_ids: Optional[uuid.UUID] = Field(None, q='secondary_industries__id')
    primary_extraction_market_id: Optional[uuid.UUID] = Field(None, q='primary_extraction_market_id')
    primary_industry_market_id: Optional[uuid.UUID] = Field(None, q='primary_industry_market_id')
    secondary_extraction_markets_ids: Optional[uuid.UUID] = Field(None, q='secondary_extraction_markets__id')
    secondary_industry_markets_ids: Optional[uuid.UUID] = Field(None, q='secondary_industry_markets__id')
    governing_title_id: Optional[uuid.UUID] = Field(None, q='governing_title_id')
    primary_faction_id: Optional[uuid.UUID] = Field(None, q='primary_faction_id')
    secondary_factions_ids: Optional[uuid.UUID] = Field(None, q='secondary_factions__id')
    territory_id: Optional[uuid.UUID] = Field(None, q='territory_id')
    rival_id: Optional[uuid.UUID] = Field(None, q='rival_id')
    friend_id: Optional[uuid.UUID] = Field(None, q='friend_id')
    soft_influence_on_ids: Optional[uuid.UUID] = Field(None, q='soft_influence_on__id')
    hard_influence_on_ids: Optional[uuid.UUID] = Field(None, q='hard_influence_on__id')
    primary_fighter_id: Optional[uuid.UUID] = Field(None, q='primary_fighter_id')
    secondary_fighters_ids: Optional[uuid.UUID] = Field(None, q='secondary_fighters__id')
    defenses_ids: Optional[uuid.UUID] = Field(None, q='defenses__id')
    fortifications_ids: Optional[uuid.UUID] = Field(None, q='fortifications__id')


class LocationOutSchema(AbstractElementBaseSchema):

    # Locality
    scene: str | None = None
    activity: str | None = None
    founding_date: int | None = None
    population_size: int | None = None
    parent_location: Optional[ElementNestedOutSchema] = None
    populations: List[ElementNestedOutSchema] = []

    # Culture
    traditions: str | None = None
    celebrations: str | None = None
    primary_cult: Optional[ElementNestedOutSchema] = None
    secondary_cults: List[ElementNestedOutSchema] = []
    delicacies: List[ElementNestedOutSchema] = []

    # World
    coordinates: str | None = None
    founders: List[ElementNestedOutSchema] = []

    # Construction
    logistics: str | None = None
    architecture: str | None = None
    construction_rate: int | None = Field(None, le=100)
    buildings: List[ElementNestedOutSchema] = []
    building_expertise: List[ElementNestedOutSchema] = []

    # Production
    extraction: str | None = None
    industry: str | None = None
    extraction_output: int | None = None
    industry_output: int | None = None
    primary_resource: Optional[ElementNestedOutSchema] = None
    primary_industry: Optional[ElementNestedOutSchema] = None
    secondary_resources: List[ElementNestedOutSchema] = []
    secondary_industries: List[ElementNestedOutSchema] = []

    # Commerce
    trade: str | None = None
    infrastructure: str | None = None
    currency: str | None = None
    primary_extraction_market: Optional[ElementNestedOutSchema] = None
    primary_industry_market: Optional[ElementNestedOutSchema] = None
    secondary_extraction_markets: List[ElementNestedOutSchema] = []
    secondary_industry_markets: List[ElementNestedOutSchema] = []

    # Localpolitics
    government: str | None = None
    opposition: str | None = None
    governing_title: Optional[ElementNestedOutSchema] = None
    primary_faction: Optional[ElementNestedOutSchema] = None
    secondary_factions: List[ElementNestedOutSchema] = []

    # Regionalpolitics
    territorial_policies: str | None = None
    territory: Optional[ElementNestedOutSchema] = None
    rival: Optional[ElementNestedOutSchema] = None
    friend: Optional[ElementNestedOutSchema] = None
    soft_influence_on: List[ElementNestedOutSchema] = []
    hard_influence_on: List[ElementNestedOutSchema] = []

    # Strategics
    defensibility: str | None = None
    height: int | None = None
    primary_fighter: Optional[ElementNestedOutSchema] = None
    secondary_fighters: List[ElementNestedOutSchema] = []
    defenses: List[ElementNestedOutSchema] = []
    fortifications: List[ElementNestedOutSchema] = []

