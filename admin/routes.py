from flask import Blueprint,render_template
from .repositories import role

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static', url_prefix='/admin')


# admin home page
@admin.route('/')
def home():
    return render_template('home.html')


# role
admin.route('/role', methods=["GET", "POST"])(role.role)
