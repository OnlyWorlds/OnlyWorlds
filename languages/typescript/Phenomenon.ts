import { BaseElement } from './base_elements';

export interface Phenomenon extends BaseElement {
  // Mechanics
  expression?: string | null;
  effects?: string | null;
  duration?: number | null;
  catalystsIds?: string[] | null;
  empowermentsIds?: string[] | null;
  // World
  mythology?: string | null;
  systemId?: string | null;
  triggersIds?: string[] | null;
  wieldersIds?: string[] | null;
  environmentsIds?: string[] | null;
}
