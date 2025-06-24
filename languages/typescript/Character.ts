import { BaseElement } from './base_elements';

export interface Character extends BaseElement {
  // Constitution
  physicality?: string | null;
  mentality?: string | null;
  height?: number | null;
  weight?: number | null;
  speciesIds?: string[] | null;
  traitsIds?: string[] | null;
  abilitiesIds?: string[] | null;
  // Origins
  background?: string | null;
  motivations?: string | null;
  birthDate?: number | null;
  birthplaceId?: string | null;
  languagesIds?: string[] | null;
  // World
  reputation?: string | null;
  locationId?: string | null;
  objectsIds?: string[] | null;
  institutionsIds?: string[] | null;
  // Personality
  charisma?: number | null;
  coercion?: number | null;
  competence?: number | null;
  compassion?: number | null;
  creativity?: number | null;
  courage?: number | null;
  // Social
  familyIds?: string[] | null;
  friendsIds?: string[] | null;
  rivalsIds?: string[] | null;
  // TTRPG
  level?: number | null;
  hitPoints?: number | null;
  STR?: number | null;
  DEX?: number | null;
  CON?: number | null;
  INT?: number | null;
  WIS?: number | null;
  CHA?: number | null;
}
