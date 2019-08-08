from flask import Flask
from .config import SQLALCHEMY_DATABASE_URI
from .models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

from .home import home_blueprint
# from website.auth import auth_blueprint
from .routes import website

app.register_blueprint(home_blueprint)
# app.register_blueprint(auth_blueprint)
app.register_blueprint(website)

