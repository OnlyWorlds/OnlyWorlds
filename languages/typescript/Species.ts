import { BaseElement } from './base_elements';

export interface Species extends BaseElement {
  // Biology
  appearance?: string | null;
  lifeSpan?: number | null;
  typicalWeight?: number | null;
  dietIds?: string[] | null;
  reproductionIds?: string[] | null;
  // Psychology
  instincts?: string | null;
  sociality?: string | null;
  temperament?: string | null;
  communication?: string | null;
  aggression?: number | null;
  traitsIds?: string[] | null;
  // World
  role?: string | null;
  parentSpeciesId?: string | null;
  locationsIds?: string[] | null;
  zonesIds?: string[] | null;
  affinitiesIds?: string[] | null;
}
