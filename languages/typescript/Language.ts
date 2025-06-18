import { BaseElement } from './base_elements';

export interface Language extends BaseElement {
  // Structure
  phonology?: string | null;
  grammar?: string | null;
  lexicon?: string | null;
  writing?: string | null;
  classificationId?: string | null;
  // World
  status?: string | null;
  spreadIds?: string[] | null;
  dialectsIds?: string[] | null;
}
