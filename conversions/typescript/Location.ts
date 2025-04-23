import { BaseElement } from './base_elements';

export interface Location extends BaseElement {
  // Locality
  scene?: string | null;
  activity?: string | null;
  foundingDate?: number | null;
  populationSize?: number | null;
  parentLocationId?: string | null;
  populationsIds?: string[] | null;
  // Culture
  traditions?: string | null;
  celebrations?: string | null;
  primaryCultId?: string | null;
  secondaryCultsIds?: string[] | null;
  delicaciesIds?: string[] | null;
  // World
  coordinates?: string | null;
  foundersIds?: string[] | null;
  // Construction
  logistics?: string | null;
  architecture?: string | null;
  constructionRate?: number | null;
  buildingsIds?: string[] | null;
  buildingExpertiseIds?: string[] | null;
  // Production
  extraction?: string | null;
  industry?: string | null;
  extractionOutput?: number | null;
  industryOutput?: number | null;
  primaryResourceId?: string | null;
  primaryIndustryId?: string | null;
  secondaryResourcesIds?: string[] | null;
  secondaryIndustriesIds?: string[] | null;
  // Commerce
  trade?: string | null;
  infrastructure?: string | null;
  currency?: string | null;
  primaryExtractionMarketId?: string | null;
  primaryIndustryMarketId?: string | null;
  secondaryExtractionMarketsIds?: string[] | null;
  secondaryIndustryMarketsIds?: string[] | null;
  // LocalPolitics
  government?: string | null;
  opposition?: string | null;
  governingTitleId?: string | null;
  primaryFactionId?: string | null;
  secondaryFactionsIds?: string[] | null;
  // RegionalPolitics
  territorialPolicies?: string | null;
  territoryId?: string | null;
  rivalId?: string | null;
  friendId?: string | null;
  softInfluenceOnIds?: string[] | null;
  hardInfluenceOnIds?: string[] | null;
  // Strategics
  defensibility?: string | null;
  height?: number | null;
  primaryFighterId?: string | null;
  secondaryFightersIds?: string[] | null;
  defensesIds?: string[] | null;
  fortificationsIds?: string[] | null;
}
