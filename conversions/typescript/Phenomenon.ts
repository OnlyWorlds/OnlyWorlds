import { BaseElement } from './base_elements';

export interface Phenomenon extends BaseElement {
  // Manifest
  presence?: string | null;
  scope?: string | null;
  duration?: number | null;
  intensity?: string | null;
  empowermentsIds?: string[] | null;
  environmentsIds?: string[] | null;
  carriersIds?: string[] | null;
  // Actuate
  effect?: string | null;
  catalystsId?: string | null;
  wieldersIds?: string[] | null;
  handlersIds?: string[] | null;
  enablersIds?: string[] | null;
  triggersIds?: string[] | null;
  affinityIds?: string[] | null;
}
