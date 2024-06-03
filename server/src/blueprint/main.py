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
  return res


@main_blueprint.route('/get_routes', methods=["POST", "GET"])
async def get_routes():
  data = request.json
  print(data)
  if not data:
    return "req is null", 402
  area_name = data["area"]
  origin = data["origin"]
  dest = data["dest"]
  token = data["token"]
  #TODO(SJ) 根据 token获取 account
  path = await Scop_Manager.get_scop_min_path(area_name,origin,dest)
  return path

@main_blueprint.route('/get_hot_scop', methods=["POST","GET"])
async def get_hot_scop():
  res = await Scop_Manager.get_hot_scop()
  for scop in res:
    del scop['_id'] # Note: 不能带有 "_id" 字段
  return res
