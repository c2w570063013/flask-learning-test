from flask import Blueprint
from .repositories import auth
from .repositories import home

website = Blueprint('website', __name__, template_folder='templates', static_folder='static')

# before login
website.before_app_request(auth.load_logged_in_user)
# home
website.route('/')(home.index)
# register
website.route('/register', methods=["GET", "POST"])(auth.register)
# login
website.route('/login', methods=["GET", "POST"])(auth.login)
# logout
website.route('/logout')(auth.logout)
# error page
website.route('/error')(home.error_page)
