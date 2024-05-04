import { reactive, ref, type Ref } from 'vue'
import Coordinate from './Coordinate'
import {cloneDeep} from "lodash"
import Scop from "./Scop"
/**
 * 区域类
 */
class Area {
  private name:string = "";
  private scop = new Scop();
  private center = new Coordinate();
  private sub_areas:Area[] = [];
  public constructor(name?:string, scop?:Scop, center?:Coordinate) {
    if (name) this.name = name;
    if (scop) this.scop = scop;
    if (center) this.center = center;
  }
}
export default Area;
const t = new Area()