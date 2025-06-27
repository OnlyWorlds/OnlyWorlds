import { BaseElement } from './base_elements';

export interface Institution extends BaseElement {
  // Foundation
  doctrine?: string | null;
  foundingDate?: number | null;
  parentInstitutionId?: string | null;
  // Claims
  zonesIds?: string[] | null;
  objectsIds?: string[] | null;
  creaturesIds?: string[] | null;
  // World
  status?: string | null;
  alliesIds?: string[] | null;
  adversariesIds?: string[] | null;
  constructsIds?: string[] | null;
}
