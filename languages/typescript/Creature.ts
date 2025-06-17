import { BaseElement } from './base_elements';

export interface Creature extends BaseElement {
  // Biology
  appearance?: string | null;
  weight?: number | null;
  height?: number | null;
  speciesIds?: string[] | null;
  // Behaviour
  habits?: string | null;
  demeanor?: string | null;
  traitsIds?: string[] | null;
  abilitiesIds?: string[] | null;
  languagesIds?: string[] | null;
  // World
  status?: string | null;
  birthDate?: number | null;
  locationId?: string | null;
  zoneId?: string | null;
  // TTRPG
  challengeRating?: number | null;
  hitPoints?: number | null;
  armorClass?: number | null;
  speed?: number | null;
  actionsIds?: string[] | null;
}
