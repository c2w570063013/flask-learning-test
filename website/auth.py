# from flask import Blueprint
from flask import request
from flask import render_template

# auth_blueprint = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


# @auth_blueprint.route('/login', methods=('GET', 'POST'))
def login():
    """
    login function
    :return:
    """
    if request.method == 'POST':
        return 'post test'
    return render_template('auth/login.html')
