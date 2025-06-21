import { BaseElement } from './base_elements';

export interface Marker extends BaseElement {
  // Details
  mapId: string;
  zoneId: string;
  x: number;
  y: number;
  z?: number | null;
}
