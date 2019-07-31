from flask import Blueprint, render_template

bp = Blueprint('admin.auth', __name__, template_folder='templates', static_folder='static',
               url_prefix='/admin')


@bp.route('/login')
def login():
    return render_template('login.html')
