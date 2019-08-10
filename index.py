from flask import Flask
# can not do like this "from . import config", which will get an error cause this project is
# initialed from a file 'index.py' not a directory
from config import *
from website import routes as website
from api import payment
from admin import routes as admin
from website.models import db
from admin.models import db as db2
from website.repositories.home import index

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = SECRET_KEY
db.init_app(app)
db2.init_app(app)

app.register_blueprint(payment.payment_bp)
app.register_blueprint(admin.admin)
app.register_blueprint(website.website)


# home page
@app.route('/')
def home():
    return index()
