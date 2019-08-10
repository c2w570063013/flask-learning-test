from flask import Flask
from . import config
from .models import db
from .routes import website
from .repositories.home import index

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = config.SECRET_KEY
db.init_app(app)

app.register_blueprint(website)


# set index page when this package is run independently
@app.route('/')
def home():
    return index()
