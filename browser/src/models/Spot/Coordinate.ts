import { ref,type Ref } from "vue";

class Coordinate {
  public longitude: Ref<number>;
  public latitude: Ref<number>
  constructor(lnt?: number, lat?: number) {
    this.longitude = ref(lnt !== undefined ? lnt : 0);
    this.latitude = ref(lat !== undefined ? lat : 0);
  }
}

export default Coordinate;