from flask import Blueprint, render_template
from .repositories import role
from .models import Role

admin = Blueprint('manual_admin', __name__, template_folder='templates', static_folder='static',
                  url_prefix='/manual_admin')


# admin home page
@admin.route('/')
def home():
    roles = Role.query.limit(20).all()
    return render_template('home.html', roles=roles)


# role
admin.route('/role', methods=["GET", "POST"])(role.add_role)
# delete role
admin.route('/role/<int:id>/delete')(role.delete_role)
# edit role
admin.route('role/<int:id>/edit', methods=["GET", "POST"])(role.edit_role)
