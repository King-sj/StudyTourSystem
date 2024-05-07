__all__ = ['main_blueprint']
from flask import Blueprint, jsonify, request
from typing import Set, Tuple
from src.ScopData import Scop_Manager
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
