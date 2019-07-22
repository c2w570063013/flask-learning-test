from flask import Blueprint
from flask import request
from flask import render_template

auth_blueprint = Blueprint('auth', __name__, template_folder='website/auth/templates')


@auth_blueprint.route('/login', methods=('GET', 'POST'))
def login():
    """
    login function
    :return:
    """
    if request.method == 'POST':
        return 'post test'
    return render_template('login.html')
