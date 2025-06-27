
export interface World {
  id?: string | null;
  name?: string | null;
  description?: string | null;
  imageUrl?: string | null;
  apiKey?: string | null;
  version?: string | null;
  user?: string | null;
  timeFormatEquivalents?: number[] | null;
  timeFormatNames?: string[] | null;
  timeBasicUnit?: string | null;
  timeRangeMin?: number | null;
  timeRangeMax?: number | null;
  timeCurrent?: number | null;
}
