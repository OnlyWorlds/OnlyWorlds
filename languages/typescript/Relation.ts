import { BaseElement } from './base_elements';

export interface Relation extends BaseElement {
  // Nature
  background?: string | null;
  startDate?: number | null;
  endDate?: number | null;
  intensity?: number | null;
  actorId?: string | null;
  eventsIds?: string[] | null;
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
  titlesIds?: string[] | null;
  constructsIds?: string[] | null;
  eventsIds?: string[] | null;
  narrativesIds?: string[] | null;
}
