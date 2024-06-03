# encoding:utf-8
import motor.motor_asyncio
from typing import List, Dict
import json
from src.Route_select import *
from src.DataType import *


# class Coordinate:
#   def __init__(self, lat: float, lng: float) -> None:
#     self.lat = lat
#     self.lng = lng


class Scop:
  """
    景区类
  """

  def __init__(self, name: str, lat: float, lng: float, province:str,city:str) -> None:
    self.name = name
    self.lat = lat
    self.lng = lng
    self.buildings: List[Scop] = []
    self.routes: List = []
    self.province : str = province
    self.city : str = city

  def add_building(self, name, lat: float, lng: float):
    self.buildings.append(Scop(name, lat, lng, self.province, self.city))

  def add_route(self, origin: str, dest: str, routes):
    routes["origin"] = origin
    routes["dest"] = dest
    self.routes.append(routes)

  async def save(self):
    await Scop_Manager.insert_record(self)

  @staticmethod
  def from_dict(data: dict) -> 'Scop':
    """
    Recursively builds a Scop object from a dictionary.
    """
    # TODO: 这里的处理逻辑有问题，需要改进
    if "province" not in data:
      data["province"] = ""
    if "city" not in data:
      data["city"] = ""
    scop = Scop(data['name'], data['lat'], data['lng'], data["province"], data["city"])
    for building_data in data.get('buildings', []):
      scop.buildings.append(Scop.from_dict(building_data))
    scop.routes = data["routes"]
    return scop

  @staticmethod
  def from_json(json_str: str) -> 'Scop':
    """
    Deserialize JSON string to a Scop object.
    """
    data = json.loads(json_str)
    return Scop.from_dict(data)

  def to_dict(self):
    return {
      'name': self.name,
      'lat': self.lat,
      'lng': self.lng,
      'buildings': [building.to_dict() for building in self.buildings],
      "routes": self.routes,
      "province": self.province,
      "city": self.city
    }


class Scop_Manager:
  def __init__(self) -> None:
    pass
  # 连接到MongoDB

  @staticmethod
  async def link():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        'mongodb://localhost:27017/')
    db = client['StudyTourSystem']
    collection = db['scops']
    # Ensure a unique index on the 'name' field
    # await collection.create_index("name", unique=True)
    return collection

  @staticmethod
  async def insert_record(scop: Scop):
    """异步插入景区"""
    collection = await Scop_Manager.link()
    res = await collection.find_one({"name": scop.name})
    if res:
      print("already exist", res)
      return
    await collection.insert_one(scop.to_dict())
    print(f"Search record for user {scop.name} added asynchronously.")

  @staticmethod
  async def get_scop(name: str):
    """
    异步获取景区dict data
    """
    collection = await Scop_Manager.link()
    return await collection.find_one({'name': name})

  @staticmethod
  async def get_all() -> List[Dict]:
    collection = await Scop_Manager.link()
    cursor = collection.find()
    res = []
    async for record in cursor:
      res.append(record)
    return res

  @staticmethod
  async def get_scop_min_path(name:str,origin:str,dest:str):
    """
    返回景区两点最短距离
    """
    data = await Scop_Manager.get_scop(name)
    if(not data):
      print("no data")
      return ""
    scop = Scop.from_dict(data)
    # 名字到编号的映射
    n2i = {scop.buildings[i].name:i+1 for i in range(0, len(scop.buildings))}
    # 编号到名字的映射
    i2n = {i+1:scop.buildings[i].name for i in range(0, len(scop.buildings))}
    # 创建Building对象
    buildings = {
      i: Building((scop.buildings[i].lat,scop.buildings[i].lng),
      set(),scop.buildings[i].name, n2i[scop.buildings[i].name])
      for i in range(0, len(scop.buildings))
    }
    # # 创建Road对象，每条Road的起点和终点都是一个Building idx
    roads = {
      i: Road('road',n2i.get(scop.routes[i]['origin']),
      n2i.get(scop.routes[i]["dest"]),scop.routes[i]["distance"],0)
      for i in range(0, len(scop.routes))
    }

    # # 创建一个Area对象
    area = Area(dict(),dict(),set(),0,0)
    for b in buildings.values():area.add_building(b)
    for r in roads.values():area.add_road(r)

    dist, route_order = get_shortest_road(area,n2i[origin],n2i[dest])
    path = ""
    for i in range(1, len(route_order)):
      res = [
        route for route in scop.routes
        if route["origin"] == i2n[route_order[i-1]] and route["dest"] == i2n[route_order[i]]
      ][0]
      for step in res["step"]:
        path += step["path"]+";"
    return path

  @staticmethod
  async def get_hot_scop():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
    db = client['StudyTourSystem']
    collection = db['score']
    cursor = collection.find({}).sort([("score", -1), ("visited_person", -1)]).limit(50)
    res = []
    async for doc in cursor:
      res.append(doc)
    client.close()
    return res
if __name__ == "__main__":
  import asyncio

  async def main():
    print(await Scop_Manager.get_all())
  asyncio.run(main())
