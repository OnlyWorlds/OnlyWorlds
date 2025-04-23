import { BaseElement } from './base_elements';

export interface Family extends BaseElement {
  // Community
  spirit?: string | null;
  alliancesIds?: string[] | null;
  rivalriesIds?: string[] | null;
  // Lineage
  history?: string | null;
  ancestorsIds?: string[] | null;
  traitsIds?: string[] | null;
  abilitiesIds?: string[] | null;
  languagesIds?: string[] | null;
  // World
  status?: string | null;
  competitionIds?: string[] | null;
  administratesIds?: string[] | null;
  creaturesIds?: string[] | null;
  // Legacy
  traditions?: string | null;
  estateId?: string | null;
  heirloomsIds?: string[] | null;
}
