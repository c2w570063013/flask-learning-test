from flask import Blueprint
from .repositories import auth
from .repositories import home

website = Blueprint('website', __name__, template_folder='templates', static_folder='static')

# home
website.route('/')(home.index)

# register
website.route('/register', methods=["GET", "POST"])(auth.register)

# login
website.route('/login', methods=["GET", "POST"])(auth.login)
