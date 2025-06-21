import { BaseElement } from './base_elements';

export interface Zone extends BaseElement {
  // Scope
  function?: string | null;
  startDate?: number | null;
  endDate?: number | null;
  phenomenaIds?: string[] | null;
  // World
  history?: string | null;
  claimedByIds?: string[] | null;
  roamedByIds?: string[] | null;
  titlesIds?: string[] | null;
}
