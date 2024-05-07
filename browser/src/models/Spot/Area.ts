import { reactive, ref, type Ref } from 'vue'
import Coordinate from './Coordinate'
import {cloneDeep} from "lodash"
import {Way} from './Way'
/**
 * 区域类
 */
class Area {
  public name:string = "";
  public center = new Coordinate();
  public sub_areas:Area[] = [];
  private _routes:Way[] = [];
  public constructor(name?:string, center?:Coordinate) {
    if (name) this.name = name;
    if (center) this.center = center;
  }
  public addSubArea(area:Area) {
    this.sub_areas.push(area)
  }
  public set routes(routes:Way[]) {
    this._routes = routes
  }
  public get routes() {
    return this._routes
  }
  public add_routes(route:Way) {
    this.routes.push(route)
  }
  public static from_json(json_str:string) : Area{
    var data = JSON.parse(json_str)
    var area =  new Area(data.get('name') as string,
    new Coordinate(
      Number(data.get('lat')),
      Number(data.get('lng'))
    ));
    (data.get("buildings") as Area[]).forEach(ele => {
      area.sub_areas.push(ele)
    });
    //TODO(SJ) add load routes
    return area
  }
  /**
   * 这个应该没什么用
   */
  public to_json() {
    // pass
  }
}
export default Area;
const t = new Area()