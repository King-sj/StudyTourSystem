__all__ = ['main_blueprint']
from flask import Blueprint,jsonify,request
from typing import Set,Tuple
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/',methods=['POST','GET'])
def main():
  return "test"