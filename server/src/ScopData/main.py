# encoding:utf-8
import sys
sys.path.append("server")
from datetime import datetime
import asyncio
import requests
import time
from src.ScopData import Scop
ak = "obh0u6Si9EEYanw8WI8x9CNtRqe0FYG4"


async def get_routes(origin_lat: float, origin_lng: float, dest_lat: float, dest_lng: float,
    method:str="walking"):
  # 接口地址
  url = f"https://api.map.baidu.com/directionlite/v1/{method}"

  params = {
      "origin":    f"{origin_lat},{origin_lng}",
      "destination":    f"{dest_lat},{dest_lng}",
      "ak":       ak,
  }

  response = requests.get(url=url, params=params)
  if response:
    try:
      data = response.json()["result"]
    except Exception as e:
      return dict()
    res = dict()
    res["distance"] = data["routes"][0]["distance"]
    res["duration"] = data["routes"][0]["duration"]
    steps = []
    for step in data["routes"][0]["steps"]:
      temp = dict()
      temp["path"] = step["path"]
      steps.append(temp)
    res["step"] = steps
    return res


async def create_scop(data):
  # 接口地址
  url = "https://api.map.baidu.com/place/v2/suggestion"

  params = {
      "query":    data['name'],
      "region":    data['city'],
      "city_limit":    "true",
      "output":    "json",
      "ak":       ak,
  }
  scop = Scop(
    data['name'], data['location']
    ['lat'], data['location']['lng'],
    data['province'], data['city']
  )
  response = requests.get(url=url, params=params)
  if response:
    # print(response.json())
    for build in response.json()['result']:
      try:
        scop.add_building(build['name'], build['location']
                          ['lat'], build['location']['lng'])
      except Exception as e:
        print(e)
  for fro in scop.buildings:
    for to in scop.buildings:
      if fro.lat != to.lat and fro.lng != to.lng:  # 坐标不同
        routes = await get_routes(fro.lat, fro.lng, to.lat, to.lng)
        scop.add_route(fro.name, to.name, routes)
  await scop.save()


async def create_city(city_code: str):
  if not str.isdigit(city_code):
    return
  # 接口地址
  url = "https://api.map.baidu.com/place/v2/search"
  # 此处填写你在控制台-应用管理-创建应用后获取的AK
  params = {
      "query":    "景区",
      "tag":    "景区",
      "region":    city_code,
      "output":    "json",
      "ak":       ak,
      "scop": 2,
      "city_limit": True,
  }

  response = requests.get(url=url, params=params)
  if response:
    for scop in response.json()['results']:
      await create_scop(scop)
      time.sleep(0.1)
if __name__ == "__main__":
  async def main():
    # await create_city("131")
    with open(r"D:\code\StudyTourSystem\server\src\ScopData\BaiduMap_cityCode_1102.txt",encoding='utf-8') as file:
      for city in file.readlines():
        await create_city(city.split(',')[0])
  asyncio.run(main())
  print("done")
