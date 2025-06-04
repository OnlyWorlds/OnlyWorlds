import { BaseElement } from './base_elements';

export interface Territory extends BaseElement {
  // Situation
  terrain?: string | null;
  size?: number | null;
  parentTerritoryId?: string | null;
  // Yield
  maintenance?: string | null;
  primaryOutput?: number | null;
  secondaryOutput?: number | null;
  primaryResourceId?: string | null;
  secondaryResourcesIds?: string[] | null;
  // World
  history?: string | null;
  occupantsIds?: string[] | null;
  occurrencesIds?: string[] | null;
}
