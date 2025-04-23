import { BaseElement } from './base_elements';

export interface Trait extends BaseElement {
  // Qualitative
  socialEffects?: string | null;
  physicalEffects?: string | null;
  skillEffects?: string | null;
  personalityEffects?: string | null;
  artisticEffects?: string | null;
  behaviourEffects?: string | null;
  // Quantitative
  charisma?: number | null;
  coercion?: number | null;
  capability?: number | null;
  compassion?: number | null;
  creativity?: number | null;
  courage?: number | null;
  // World
  antiTraitId?: string | null;
  empoweredAbilitiesIds?: string[] | null;
}
