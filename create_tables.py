from index import app
from config import *
from website.models import db

# create a database: CREATE DATABASE flask_test CHARACTER SET UTF8MB4;
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)
with app.app_context():
    db.create_all()
