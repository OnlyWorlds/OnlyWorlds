import { BaseElement } from './base_elements';

export interface Object extends BaseElement {
  // Form
  aesthetics?: string | null;
  weight?: number | null;
  amount?: number | null;
  parentObjectId?: string | null;
  materialsIds?: string[] | null;
  technologyIds?: string[] | null;
  // Function
  utility?: string | null;
  effectsIds?: string[] | null;
  abilitiesIds?: string[] | null;
  consumesIds?: string[] | null;
  // World
  origins?: string | null;
  locationId?: string | null;
  languageId?: string | null;
  affinitiesIds?: string[] | null;
}
