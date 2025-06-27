import { BaseElement } from './base_elements';

export interface Law extends BaseElement {
  // Code
  declaration?: string | null;
  purpose?: string | null;
  date?: number | null;
  parentLawId?: string | null;
  penaltiesIds?: string[] | null;
  // World
  authorId?: string | null;
  locationsIds?: string[] | null;
  zonesIds?: string[] | null;
  prohibitionsIds?: string[] | null;
  adjudicatorsIds?: string[] | null;
  enforcersIds?: string[] | null;
}
