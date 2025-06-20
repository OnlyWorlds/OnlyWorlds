import { BaseElement } from './base_elements';

export interface Ability extends BaseElement {
  // Mechanics
  activation?: string | null;
  duration?: number | null;
  potency?: number | null;
  range?: number | null;
  effectsIds?: string[] | null;
  // Enablement
  challenges?: string | null;
  sourceId?: string | null;
  talentsIds?: string[] | null;
  instrumentsIds?: string[] | null;
  requisitesIds?: string[] | null;
  // World
  prevalence?: string | null;
  traditionId?: string | null;
  locusId?: string | null;
}
