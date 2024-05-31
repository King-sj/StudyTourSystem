__all__ = ['main_blueprint']
from flask import Blueprint, jsonify, request
from typing import Set, Tuple
from src.ScopData import Scop_Manager
from src.DataType import *
from src.Route_select import *
main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/', methods=['POST', 'GET'])
async def main():
  return "test"


@main_blueprint.route('/get_all_scop', methods=['POST', "GET"])
async def get_all_scop():
  res = await Scop_Manager.get_all()
  for scop in res:
    del scop['_id']
  print(res)
  return res


@main_blueprint.route('/ ', methods=["POST", "GET"])
async def get_routes():
  data = request.json
  print(data)
  if not data:
    return "req is null", 402
  area_name = data["area"]
  token = data["token"]
  #TODO(SJ) 根据 token获取 account
  # 创建一个Area对象
  area = Area(dict(), dict(), set(), 0, 0)
  json_data = await Scop_Manager.get_scop(area_name)
  print(json_data)
  # 创建10个Building对象
  buildings = {i: Building((0, 0), set(), str(i)) for i in range(1, 11)}

  # 创建10条Road对象，每条Road的起点和终点都是一个Building
  roads = {i: Road('road', i, (i % 10) + 1, i, 0) for i in range(1, 11)}

  for b in buildings.values():
    area.add_building(b)
  for r in roads.values():
    area.add_road(r)
  result = get_shortest_road(area, 1, 10)
  assert result[0] == 10 and result[1][10] == 1
  return ""
