
export interface World {
  id: string;
  name: string;
  description?: string | null;
  imageUrl?: string | null;
  apiKey: string;
  version: string;
  user: string;
  timeFormatEquivalents?: number[] | null;
  timeFormatNames?: string[] | null;
  timeBasicUnit?: string | null;
  timeRangeMin?: number | null;
  timeRangeMax?: number | null;
  timeCurrent?: number | null;
}
