import Coordinate from "./Coordinate"
/**
 * 路线的一段
 */
export class Step {
  public origin: Coordinate;
  public dest: Coordinate;
  public path: Coordinate[] = [];
  public distance: number;
  constructor(
    origin: Coordinate, dest: Coordinate,
    dist: number, path?: Coordinate[]) {
    this.origin = origin;
    this.dest = dest;
    this.distance = dist;
    if (path) this.path = path;
  }
  public addPoint(point: Coordinate) {
    this.path.push(point)
  }
}
/**
 * 路线
 */
export class Way extends Step {
  public readonly routes: Step[] = [];
  public from_id:number;
  public to_id:number;
  constructor(
    from_id:number, to_id:number,
    origin: Coordinate, dest: Coordinate,
    dist: number, routes?: Step[]) {
    super(origin, dest, dist)
    this.from_id = from_id;
    this.to_id = to_id;
    if (routes) this.routes = routes
  }
  public addStep(step: Step) {
    this.routes.push(step)
  }
}
export default Way