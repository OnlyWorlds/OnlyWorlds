import { BaseElement } from './base_elements';

export interface Object extends BaseElement {
  // Form
  aesthetics?: string | null;
  weight?: number | null;
  amount?: number | null;
  parentObjectId?: string | null;
  technologyIds?: string[] | null;
  // Function
  utility?: string | null;
  effectsIds?: string[] | null;
  enablesIds?: string[] | null;
  consumesIds?: string[] | null;
  // World
  origins?: string | null;
  locationId?: string | null;
  // Games
  craftsmanship?: string | null;
  requirements?: string | null;
  durability?: string | null;
  value?: number | null;
  damage?: number | null;
  armor?: number | null;
  rarity?: string | null;
  languageId?: string | null;
  requiresIds?: string[] | null;
}
