import { BaseElement } from './base_elements';

export interface Ability extends BaseElement {
  // Mechanics
  usage?: string | null;
  range?: number | null;
  strength?: number | null;
  effectsIds?: string[] | null;
  utilityIds?: string[] | null;
  // Dynamics
  difficulty?: string | null;
  talentIds?: string[] | null;
  enablersIds?: string[] | null;
  requirementsIds?: string[] | null;
  // World
  prevalence?: string | null;
  systemId?: string | null;
  constructId?: string | null;
}
