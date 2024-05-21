# encoding:utf-8
import motor.motor_asyncio
from typing import List, Dict
import json


# class Coordinate:
#   def __init__(self, lat: float, lng: float) -> None:
#     self.lat = lat
#     self.lng = lng


class Scop:
  """
    景区类
  """

  def __init__(self, name: str, lat: float, lng: float) -> None:
    self.name = name
    self.lat = lat
    self.lng = lng

    self.buildings: List[Scop] = []
    self.routes: List = []

  def add_building(self, name, lat: float, lng: float):
    self.buildings.append(Scop(name, lat, lng))

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
    scop = Scop(data['name'], data['lat'], data['lng'])
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
        "routes": self.routes
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
    collection = await Scop_Manager.link()
    cursor = collection.find({'name': name})
    res = []
    async for record in cursor:
      res.append(record)
    return res

  @staticmethod
  async def get_all() -> List[Dict]:
    collection = await Scop_Manager.link()
    cursor = collection.find()
    res = []
    async for record in cursor:
      res.append(record)
    return res


if __name__ == "__main__":
  import asyncio

  async def main():
    print(await Scop_Manager.get_all())
  asyncio.run(main())
