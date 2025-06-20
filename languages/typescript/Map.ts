import { BaseElement } from './base_elements';

export interface Map extends BaseElement {
  // Details
  backgroundColor?: string | null;
  hierarchy?: number | null;
  width?: number | null;
  height?: number | null;
  depth?: number | null;
  parentMapId?: string | null;
  locationId?: string | null;
}
