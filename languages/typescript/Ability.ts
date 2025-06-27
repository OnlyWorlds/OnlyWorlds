import { BaseElement } from './base_elements';

export interface Ability extends BaseElement {
  // Mechanics
  activation?: string | null;
  duration?: number | null;
  potency?: number | null;
  range?: number | null;
  effectsIds?: string[] | null;
  challenges?: string | null;
  talentsIds?: string[] | null;
  requisitesIds?: string[] | null;
  // World
  prevalence?: string | null;
  traditionId?: string | null;
  sourceId?: string | null;
  locusId?: string | null;
  instrumentsIds?: string[] | null;
  systemsIds?: string[] | null;
}
