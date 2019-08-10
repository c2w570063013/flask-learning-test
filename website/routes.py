from flask import Blueprint, redirect, url_for, flash
from .repositories import auth
from .repositories import home
from .models import db

website = Blueprint('website', __name__, template_folder='templates',
                    static_folder='static', url_prefix='/home')

# before login (like middleware in laravel??)
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


# global handling errors
@website.errorhandler(Exception)
def handler_error(e):
    from website.fun import logger
    logger(str(e))
    flash(str(e))
    return redirect(url_for('website.error_page'))
