import { BaseElement } from './base_elements';

export interface Relation extends BaseElement {
  // Nature
  history?: string | null;
  impact?: string | null;
  startDate?: number | null;
  endDate?: number | null;
  debt?: number | null;
  eventsIds?: string[] | null;
  // Involves
  primaryCharacterId?: string | null;
  primaryCreatureId?: string | null;
  primaryInstitutionId?: string | null;
  secondaryCharactersIds?: string[] | null;
  secondaryCreaturesIds?: string[] | null;
  secondaryInstitutionsIds?: string[] | null;
}
