from flask import Flask
from .config import SQLALCHEMY_DATABASE_URI
from .models import db
from .routes import website

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = config.SECRET_KEY
db.init_app(app)

app.register_blueprint(website)
