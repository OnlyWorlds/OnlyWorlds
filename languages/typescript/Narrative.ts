import { BaseElement } from './base_elements';

export interface Narrative extends BaseElement {
  // Context
  story?: string | null;
  consequences?: string | null;
  startDate?: number | null;
  endDate?: number | null;
  order?: number | null;
  parentNarrativeId?: string | null;
  protagonistId?: string | null;
  antagonistId?: string | null;
  narratorId?: string | null;
  conservatorId?: string | null;
  // Involves
  eventsIds?: string[] | null;
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
  lawsIds?: string[] | null;
}
