export interface ICoord{
  lng: number,
  lat: number,
}
export type ILocation = ICoord | string;

export interface ScopBasicInfo{
  name:string,
  province:string,
  city:string
}