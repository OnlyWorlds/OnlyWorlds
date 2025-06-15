import { BaseElement } from './base_elements';

export interface Law extends BaseElement {
  // Code
  decree?: string | null;
  date?: number | null;
  purpose?: string | null;
  authorId?: string | null;
  // Compulsion
  jurisdictionsIds?: string[] | null;
  prohibitionsIds?: string[] | null;
  penaltiesIds?: string[] | null;
  adjudicatorsIds?: string[] | null;
  enforcersIds?: string[] | null;
}
