import { BaseElement } from './base_elements';

export interface Pin extends BaseElement {
  // Details
  mapId: string;
  elementId: string;
  x: number;
  y: number;
  z?: number | null;
}
