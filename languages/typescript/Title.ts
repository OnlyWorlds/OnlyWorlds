import { BaseElement } from './base_elements';

export interface Title extends BaseElement {
  // Mandate
  authority?: string | null;
  eligibility?: string | null;
  grantDate?: number | null;
  revokeDate?: number | null;
  issuerId?: string | null;
  bodyId?: string | null;
  superiorTitleId?: string | null;
  holdersIds?: string[] | null;
  symbolsIds?: string[] | null;
  // World
  status?: string | null;
  history?: string | null;
  charactersIds?: string[] | null;
  institutionsIds?: string[] | null;
  familiesIds?: string[] | null;
  zonesIds?: string[] | null;
  locationsIds?: string[] | null;
  objectsIds?: string[] | null;
  constructsIds?: string[] | null;
  lawsIds?: string[] | null;
  collectivesIds?: string[] | null;
  creaturesIds?: string[] | null;
  phenomenaIds?: string[] | null;
  speciesIds?: string[] | null;
  languagesIds?: string[] | null;
}
