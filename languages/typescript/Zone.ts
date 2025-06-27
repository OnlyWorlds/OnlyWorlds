import { BaseElement } from './base_elements';

export interface Zone extends BaseElement {
  // Scope
  role?: string | null;
  startDate?: number | null;
  endDate?: number | null;
  phenomenaIds?: string[] | null;
  linkedZonesIds?: string[] | null;
  // World
  context?: string | null;
  populationsIds?: string[] | null;
  titlesIds?: string[] | null;
  principlesIds?: string[] | null;
}
