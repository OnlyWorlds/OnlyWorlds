import { BaseElement } from './base_elements';

export interface Creature extends BaseElement {
  // Physiology
  appearance?: string | null;
  weight?: number | null;
  height?: number | null;
  speciesIds?: string[] | null;
  // Lifestyle
  behaviour?: string | null;
  demeanour?: string | null;
  traitsIds?: string[] | null;
  abilitiesIds?: string[] | null;
  languagesIds?: string[] | null;
  // World
  birthDate?: number | null;
  locationId?: string | null;
  territoryId?: string | null;
  // Games
  lore?: string | null;
  senses?: string | null;
  hitPoints?: number | null;
  armorClass?: number | null;
  challengeRating?: number | null;
  speed?: number | null;
  ttStr?: number | null;
  ttInt?: number | null;
  ttCon?: number | null;
  ttDex?: number | null;
  ttWis?: number | null;
  ttCha?: number | null;
  actionsIds?: string[] | null;
  reactionsIds?: string[] | null;
  alignment?: string | null;
}
