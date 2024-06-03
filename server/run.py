from src import blueprint
from src.utils import app
from src.LoginSystem import login_signup_blueprint
from src.DataServer import data_server
app.register_blueprint(blueprint.main_blueprint, url_prefix='/api')
app.register_blueprint(login_signup_blueprint, url_prefix='/loginSystem')
app.register_blueprint(data_server, url_prefix='/resource')


@app.route("/")
def index():
  return "Welcome"

if __name__ == '__main__':
  app.run(debug=True, port=2004, host='0.0.0.0')
