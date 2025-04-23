import { BaseElement } from './base_elements';

export interface Character extends BaseElement {
  // Constitution
  physicality?: string | null;
  psychology?: string | null;
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
  situation?: string | null;
  locationId?: string | null;
  titlesIds?: string[] | null;
  objectsIds?: string[] | null;
  institutionsIds?: string[] | null;
  // Personality
  charisma?: number | null;
  coercion?: number | null;
  capability?: number | null;
  compassion?: number | null;
  creativity?: number | null;
  courage?: number | null;
  // Social
  familyIds?: string[] | null;
  friendsIds?: string[] | null;
  rivalsIds?: string[] | null;
  // Games
  backstory?: string | null;
  level?: number | null;
  power?: number | null;
  price?: number | null;
  hitPoints?: number | null;
  skillStealth?: number | null;
  ttStr?: number | null;
  ttInt?: number | null;
  ttCon?: number | null;
  ttDex?: number | null;
  ttWis?: number | null;
  ttCha?: number | null;
  class?: string | null;
  alignment?: string | null;
  equipmentIds?: string[] | null;
  backpackIds?: string[] | null;
  proficienciesIds?: string[] | null;
  featuresIds?: string[] | null;
  spellsIds?: string[] | null;
  inspirationsIds?: string[] | null;
}
