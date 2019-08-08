from flask import Blueprint
from . import auth

website = Blueprint('website', __name__, template_folder='templates', static_folder='static')

website.route('/login', methods=["GET", "POST"])(auth.login)
