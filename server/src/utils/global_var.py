from flask import Flask, jsonify, request, url_for
import os
from flask_cors import CORS
DEBUG = True
SERVER = 'http://127.0.0.1:2004'
template_dir = os.path.abspath('src/templates')
print("abspath: ", template_dir)
app = Flask(__name__, template_folder=template_dir)
CORS(app, supports_credentials=True)  # 启用CORS
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = 'm18146295489@163.com'
app.config['MAIL_PASSWORD'] = 'NRAGIYGMLFOSGQPS'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'm18146295489@163.com'
app.config['MAIL_ADMIN'] = 'm18146295489@163.com'
app.config['DEBUG'] = False
