__all__ = ['data_server']
from flask import Blueprint,jsonify,request,send_file
import os

data_server = Blueprint('data_server', __name__)
RESOURCE_DIR = './data/'

@data_server.route('/<path:resource_path>')
def serve_resource(resource_path):
  """
  根据路径返回对应的资源。
  """
  # 构造文件的完整路径

  full_path = os.path.abspath(os.path.join(RESOURCE_DIR, resource_path))

  # 检查文件是否存在
  if not os.path.exists(full_path):
      return "Resource not found : " + full_path, 404

  # 根据文件类型（扩展名）决定如何返回
  if full_path.endswith('.json'):
      with open(full_path, 'r') as file:
          data = file.read()
          return jsonify(data)
  else:
      return send_file(full_path)