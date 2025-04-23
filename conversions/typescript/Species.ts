import { BaseElement } from './base_elements';

export interface Species extends BaseElement {
  // Biology
  appearance?: string | null;
  lifeSpan?: number | null;
  averageWeight?: number | null;
  nourishmentIds?: string[] | null;
  // Psychology
  instincts?: string | null;
  aggression?: number | null;
  agency?: string | null;
  languagesIds?: string[] | null;
  // World
  impact?: string | null;
  habitatIds?: string[] | null;
  interactionIds?: string[] | null;
  consumablesIds?: string[] | null;
}
