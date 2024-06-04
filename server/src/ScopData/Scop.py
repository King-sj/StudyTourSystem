# encoding:utf-8
import motor.motor_asyncio
from typing import List, Dict
import json
from src.Route_select import *
from src.DataType import *
from redis import asyncio as aioredis
from datetime import datetime

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
  async def link_database():
    client = motor.motor_asyncio.AsyncIOMotorClient(
      'mongodb://localhost:27017/')
    db = client['StudyTourSystem']
    return db
  @staticmethod
  async def insert_record(scop: Scop):
    """异步插入景区"""
    db = await Scop_Manager.link_database()
    collection = db['scops']
    res = await collection.find_one({"name": scop.name})
    if res:
      print("already exist", res)
      return
    await collection.insert_one(scop.to_dict())
    print(f"Search record for user {scop.name} added asynchronously.")

  @staticmethod
  async def get_scops(name:str, province:str, city:str):
    db = await Scop_Manager.link_database()
    collection = db["scops"]
    query = {
      "name": {"$regex": f'.*{name}.*'},
      "province":{"$regex":f'.*{province}.*'},
      "city":{"$regex":f'.*{city}.*'}
    }
    res = []
    async for doc in collection.find(query):
      del doc['_id']
      score_doc = await db["score"].find_one({"name":doc["name"]})
      if (score_doc):
        doc["score"] = score_doc['score']
        doc["visited_person"] = score_doc['visited_person']
      res.append(doc)
    # print("get_scops", query , res)
    return res

  @staticmethod
  async def get_scop(name: str):
    """
    异步获取景区dict data
    """
    db = await Scop_Manager.link_database()
    collection = db['scops']
    return await collection.find_one({'name': name})

  @staticmethod
  async def get_all() -> List[Dict]:
    db = await Scop_Manager.link_database()
    collection = db['scops']
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
      return "",""
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
    key_node = ""
    for idx in route_order:
      for building in data.get("buildings", []):
        if building["name"] == i2n[idx]:
          key_node += str(building['lng'])+","+str(building['lat'])+";"
          break

    for i in range(1, len(route_order)):
      res = [
        route for route in scop.routes
        if route["origin"] == i2n[route_order[i-1]] and route["dest"] == i2n[route_order[i]]
      ][0]
      for step in res["step"]:
        path += step["path"]+";"
    return path,key_node

  @staticmethod
  async def get_hot_scop():
    db = await Scop_Manager.link_database()
    collection = db['score']
    cursor = collection.find({}).sort([("score", -1), ("visited_person", -1)]).limit(51)
    res = []
    async for doc in cursor:
      res.append(doc)
    return res

  @staticmethod
  async def uploadJour(jour:str,name:str,score:float,province:str,city:str,token:str)->bool:
    db = await Scop_Manager.link_database()
    collection = db['jour']
    await collection.create_index("user",unique=True)
    redis_client = await aioredis.from_url('redis://localhost')
    user = await redis_client.get(token)
    if not user:
      await redis_client.aclose()
      return False
    await collection.update_one(
      {"user":user.decode('utf-8')},
      {
        "$push":{
          "jour":{
            "date":datetime.now().strftime(r'%Y-%m-%d  %H:%M:%S'),
            "data":jour,
            "score":score,
            "scop_name":name,
            "province":province,
            "city":city
          }
        }
      },
      upsert=True
    )
    score_doc = await db['score'].find_one({"name":name})
    if score_doc:
      new_score = (score_doc["score"]*score_doc['visited_person'] + score)/(score_doc['visited_person']+1)
      await db['score'].update_one({"name":name},
        {
          "$inc": {"visited_person": 1},
          "$set": {"score": new_score}
        }
      )
    else:
      print("score_doc is null", name)
      await db['score'].insert_one({
        "name":name,
        "score":score,
        "visited_person":1,
        "province":province,
        "city":city
      })
    await redis_client.aclose()
    return True

  @staticmethod
  async def get_history(token:str):
    db = await Scop_Manager.link_database()
    collection = db['jour']
    redis_client = await aioredis.from_url('redis://localhost')
    user = await redis_client.get(token)
    if not user:
      await redis_client.aclose()
      return False,"redis is closed"
    docs = await collection.find_one({"user":user.decode('utf-8')})
    if not docs:
      await redis_client.aclose()
      return False,"can not find docs"
    return True,docs["jour"]
if __name__ == "__main__":
  import asyncio

  async def main():
    print(await Scop_Manager.get_all())
  asyncio.run(main())
