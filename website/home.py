from flask import Blueprint
from flask import render_template

home_blueprint = Blueprint('home', __name__, url_prefix='/home', template_folder='templates',
                           static_folder='static')


@home_blueprint.route('/')
def index():
    return render_template('home/index.html')
