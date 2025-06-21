import { BaseElement } from './base_elements';

export interface Construct extends BaseElement {
  // Nature
  rationale?: string | null;
  history?: string | null;
  status?: string | null;
  reach?: string | null;
  startDate?: number | null;
  endDate?: number | null;
  founderId?: string | null;
  custodianId?: string | null;
  // Involves
  charactersIds?: string[] | null;
  objectsIds?: string[] | null;
  locationsIds?: string[] | null;
  speciesIds?: string[] | null;
  creaturesIds?: string[] | null;
  institutionsIds?: string[] | null;
  traitsIds?: string[] | null;
  collectivesIds?: string[] | null;
  zonesIds?: string[] | null;
  abilitiesIds?: string[] | null;
  phenomenaIds?: string[] | null;
  languagesIds?: string[] | null;
  familiesIds?: string[] | null;
  relationsIds?: string[] | null;
  titlesIds?: string[] | null;
  constructsIds?: string[] | null;
  eventsIds?: string[] | null;
  narrativesIds?: string[] | null;
}
