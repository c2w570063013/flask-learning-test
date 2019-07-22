from flask import Flask

app = Flask(__name__)

from website.home import home_blueprint
from website.auth import auth_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)
