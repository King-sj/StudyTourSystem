__all__ = ['main_blueprint']
from flask import Blueprint, jsonify, request
from typing import Set, Tuple
from src.ScopData import Scop_Manager
from src.DataType import *
from src.Route_select import *
from src.ScopData import get_routes as get_routes_by_baidu
from src.ai import *
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
  # token = data["token"]
  #TODO(SJ) 根据 token获取 account
  path,key_node = await Scop_Manager.get_scop_min_path(area_name,origin,dest)
  return [path,key_node]

@main_blueprint.route('/get_hot_scop', methods=["POST","GET"])
async def get_hot_scop():
  res = await Scop_Manager.get_hot_scop()
  for scop in res:
    del scop['_id'] # Note: 不能带有 "_id" 字段
  return res

@main_blueprint.route('/get_scops_info',methods=["POST","GET"])
async def get_scops_info():
  data = request.json
  if not data:
    return "req is null",402
  name = data['name']
  province = data['province']
  city = data['city']
  res = await Scop_Manager.get_scops(name,province,city)
  return res

@main_blueprint.route('/upLoadJour', methods=["POST","GET"])
async def upLoadJour():
  data = request.json
  if not data:
    return jsonify({
      "status":False,
      "msg": "req is null"
    })
  name = data['scopName']
  province = data['province']
  city = data['city']
  score = data['score']
  token = data["token"]
  jour = data['jour']
  res = await Scop_Manager.uploadJour(jour,name,score,province,city,token)
  if (res):
    return jsonify({
      "status":True,
      "msg": "upload jour successfully"
    })
  else:
    return jsonify({
      "status":False,
      "msg": "upload jour failed"
    })

@main_blueprint.route('/get_history', methods=["POST","GET"])
async def get_history():
  data = request.json
  if not data:
    return jsonify({
      "status":False,
      "msg": "req is null"
    })
  token = data["token"]
  suc,res = await Scop_Manager.get_history(token)
  return jsonify({
    "status":suc,
    "res": res
  })


@main_blueprint.route('/get_routes_by_baidu', methods=["POST","GET"])
async def road_plan():
  data = request.json
  if not data:
    return jsonify({
      "status":False,
      "msg": "req is null"
    })
  origin_lat = data["origin_lat"]
  origin_lng = data["origin_lng"]
  dest_lat = data["dest_lat"]
  dest_lng = data["dest_lng"]
  res = await get_routes_by_baidu(origin_lat,origin_lng,dest_lat,dest_lng)
  return jsonify({
    "status":True,
    "msg": "success",
    "res":res
  })

@main_blueprint.route("/get_ai_suggestion", methods=['POST','GET'])
async def get_ai_suggestion():
  data = request.json
  if not data:
    return jsonify({
      "status":False,
      "msg": "req is null"
    })
  loc = data['name']
  # res = await get_suggestion(loc)
  res = "fahsdfkasdsdfasdfhkasdfjkasfkdsfks"
  if(res):
    return jsonify({
      "status":True,
      "msg": res
    })
  else:
    return jsonify({
      "status":False,
      "msg": "can not answer"
    })

@main_blueprint.route("/get_ai_response", methods=['POST','GET'])
async def get_ai_response():
  data = request.json
  if not data:
    return jsonify({
      "status":False,
      "msg": "req is null"
    })
  question = data['question']
  # res = await get_response(question)
  res = "fahsdfkasdsdfasdfhkasdfjkasfkdsfks"

  if(res):
    return jsonify({
      "status":True,
      "msg": res
    })
  else:
    return jsonify({
      "status":False,
      "msg": "can not answer"
    })

