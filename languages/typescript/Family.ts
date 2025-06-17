import { BaseElement } from './base_elements';

export interface Family extends BaseElement {
  // Identity
  spirit?: string | null;
  history?: string | null;
  traditionsIds?: string[] | null;
  traitsIds?: string[] | null;
  abilitiesIds?: string[] | null;
  languagesIds?: string[] | null;
  ancestorsIds?: string[] | null;
  // World
  reputation?: string | null;
  estatesIds?: string[] | null;
  governsIds?: string[] | null;
  heirloomsIds?: string[] | null;
  creaturesIds?: string[] | null;
}
