import { BaseElement } from './base_elements';

export interface Location extends BaseElement {
  // Setting
  form?: string | null;
  function?: string | null;
  foundingDate?: number | null;
  parentLocationId?: string | null;
  populationsIds?: string[] | null;
  // Politics
  politicalClimate?: string | null;
  primaryPowerId?: string | null;
  governingTitleId?: string | null;
  secondaryPowersIds?: string[] | null;
  zoneId?: string | null;
  rivalId?: string | null;
  partnerId?: string | null;
  // World
  customs?: string | null;
  foundersIds?: string[] | null;
  cultsIds?: string[] | null;
  delicaciesIds?: string[] | null;
  // Production
  extractionMethodsIds?: string[] | null;
  extractionGoodsIds?: string[] | null;
  industryMethodsIds?: string[] | null;
  industryGoodsIds?: string[] | null;
  // Commerce
  infrastructure?: string | null;
  extractionMarketsIds?: string[] | null;
  industryMarketsIds?: string[] | null;
  currenciesIds?: string[] | null;
  // Construction
  architecture?: string | null;
  buildingsIds?: string[] | null;
  buildingMethodsIds?: string[] | null;
  // Defense
  defensibility?: string | null;
  elevation?: number | null;
  fightersIds?: string[] | null;
  defensiveObjectsIds?: string[] | null;
}
