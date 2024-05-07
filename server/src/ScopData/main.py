# encoding:utf-8
from datetime import datetime
import asyncio
import requests
import time
import Scop
ak = "obh0u6Si9EEYanw8WI8x9CNtRqe0FYG4"


async def create_scop(data):
  # 接口地址
  url = "https://api.map.baidu.com/place/v2/suggestion"

  params = {
      "query":    data['name'],
      "region":    "北京",
      "city_limit":    "true",
      "output":    "json",
      "ak":       ak,

  }
  scop = Scop.Scop(data['name'], data['location']
                   ['lat'], data['location']['lng'])
  response = requests.get(url=url, params=params)
  if response:
    print(response.json())
    for build in response.json()['result']:
      scop.add_building(build['name'], build['location']
                        ['lat'], build['location']['lng'])
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
    with open("./BaiduMap_cityCode_1102.txt") as file:
      for city in file.readlines():
        await create_city(city.split(',')[0])
  asyncio.run(main())
