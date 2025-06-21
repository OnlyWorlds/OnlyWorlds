import { BaseElement } from './base_elements';

export interface Trait extends BaseElement {
  // Qualitative
  socialEffects?: string | null;
  physicalEffects?: string | null;
  functionalEffects?: string | null;
  personalityEffects?: string | null;
  behaviourEffects?: string | null;
  // Quantitative
  charisma?: number | null;
  coercion?: number | null;
  competence?: number | null;
  compassion?: number | null;
  creativity?: number | null;
  courage?: number | null;
  // World
  significance?: string | null;
  antiTraitId?: string | null;
  empoweredAbilitiesIds?: string[] | null;
}
