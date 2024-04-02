from flask import Flask,jsonify
from flask_cors import CORS
from src import blueprint
app = Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(blueprint.main_blueprint,url_prefix='/api')

@app.route("/")
def index():
  return "Welcome"
if __name__ == '__main__':
  app.run(debug=True, port=2004,host='0.0.0.0')