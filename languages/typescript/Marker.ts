import { BaseElement } from './base_elements';

export interface Marker extends BaseElement {
  // Details
  x?: number | null;
  y?: number | null;
  z?: number | null;
  mapId?: string | null;
  zoneId?: string | null;
}
