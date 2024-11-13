export interface RaceType {
  id: string;
  name: string;
  data: any[]; // Response Type needed
  created_at: Date;
  updated_atDate;
  driver: string;
  event: string
  lap_number: number;
  lap_time: number;
}
