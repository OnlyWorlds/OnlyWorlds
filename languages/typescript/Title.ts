import { BaseElement } from './base_elements';

export interface Title extends BaseElement {
  // Nature
  privileges?: string | null;
  conditions?: string | null;
  createDate?: number | null;
  assignDate?: number | null;
  revokeDate?: number | null;
  hierarchy?: number | null;
  // Issue
  rights?: string | null;
  authorId?: string | null;
  // World
  characterId?: string | null;
  locationId?: string | null;
  objectId?: string | null;
  institutionId?: string | null;
  creatureId?: string | null;
  zoneId?: string | null;
  collectiveId?: string | null;
  constructId?: string | null;
}
