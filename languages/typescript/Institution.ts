import { BaseElement } from './base_elements';

export interface Institution extends BaseElement {
  // Foundation
  premise?: string | null;
  foundDate?: number | null;
  endDate?: number | null;
  parentInstitutionId?: string | null;
  // Claim
  territoriesIds?: string[] | null;
  objectsIds?: string[] | null;
  creaturesIds?: string[] | null;
  legalIds?: string[] | null;
  // World
  situation?: string | null;
  cooperatesIds?: string[] | null;
  competitionIds?: string[] | null;
  constructsIds?: string[] | null;
  phenomenaIds?: string[] | null;
}
