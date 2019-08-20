from flask import Flask
# can not do like this "from . import config", which will get an error cause this project is
# initialed from a file 'index.py' not a directory
from config import *
from website import routes as website
from api import payment
from admin import routes as manual_admin
from website.models import db
from admin.models import db as db2
from website.repositories.home import index
from flask_admin import Admin
from flask_celery import make_celery
import click
from flask.cli import AppGroup
import flask_cmd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
app.secret_key = SECRET_KEY
db.init_app(app)
db2.init_app(app)

celery = make_celery(app)


@app.route('/test_celery')
def test_celery():
    add_together.delay('sss', 'bbb')
    return 'shit'


@celery.task()
def add_together(a, b):
    file = 'aaa.log'
    with open(file, 'a') as fo:
        fo.write(a + b + "\n")
    return a + b


# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='microblog', template_mode='bootstrap3')

app.register_blueprint(payment.payment_bp)
app.register_blueprint(manual_admin.admin)
app.register_blueprint(website.website)
app.register_blueprint(flask_cmd.bp)


# home page
@app.route('/')
def home():
    return index()


# flask command test 'flask create-user admin'
@app.cli.command('create-user')
@click.argument("name")
def create_user(name):
    print('hello ' + name)


user_cli = AppGroup('user')


# flask group command test 'flask user  create demo'
@user_cli.command('create')
@click.argument('name')
def create_user(name):
    print(name)


app.cli.add_command(user_cli)
