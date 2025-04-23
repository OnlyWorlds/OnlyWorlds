import { BaseElement } from './base_elements';

export interface Language extends BaseElement {
  // Syntax
  writing?: string | null;
  phonology?: string | null;
  grammar?: string | null;
  vocabulary?: string | null;
  classificationId?: string | null;
  // Spread
  prose?: string | null;
  speakers?: number | null;
  dialectsIds?: string[] | null;
  rangeIds?: string[] | null;
}
