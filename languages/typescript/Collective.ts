import { BaseElement } from './base_elements';

export interface Collective extends BaseElement {
  // Formation
  composition?: string | null;
  count?: number | null;
  formationDate?: number | null;
  operatorId?: string | null;
  equipmentIds?: string[] | null;
  // Dynamics
  activity?: string | null;
  disposition?: string | null;
  state?: string | null;
  abilitiesIds?: string[] | null;
  symbolismIds?: string[] | null;
  // World
  speciesIds?: string[] | null;
  charactersIds?: string[] | null;
  creaturesIds?: string[] | null;
  phenomenaIds?: string[] | null;
}
