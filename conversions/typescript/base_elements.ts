// Base interface for all world elements (Generated from base_properties.yaml)
export interface BaseElement {
  id: string;
  name: string;
  description?: string | null;
  supertype?: string | null;
  subtype?: string | null;
  imageUrl?: string | null;
  world?: string | null;
}
