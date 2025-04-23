import { BaseElement } from './base_elements';

export interface Collective extends BaseElement {
  // Formation
  composition?: string | null;
  count?: number | null;
  formationDate?: number | null;
  operatorId?: string | null;
  equipmentIds?: string[] | null;
  // Agency
  activity?: string | null;
  temperance?: string | null;
  skillsIds?: string[] | null;
  ritualsIds?: string[] | null;
  // World
  speciesIds?: string[] | null;
  charactersIds?: string[] | null;
  creaturesIds?: string[] | null;
  phenomenaIds?: string[] | null;
}
