from flask import render_template, request, redirect, url_for, flash
from admin.models import Role, db


def add_role():
    if request.method == 'POST':
        name = request.form['role_name']
        level = request.form['type']
        role_model = Role(name=name, type=level)
        db.session.add(role_model)
        db.session.commit()
        return redirect(url_for('manual_admin.home'))
    return render_template('role.html')


def delete_role(id):
    role = Role.query.get(id)
    error = 'id: ' + str(id) + " not exists"
    if role is not None:
        db.session.delete(role)
        db.session.commit()
        error = None
    if error is not None:
        flash(error)
    return redirect(url_for('manual_admin.home'))


def edit_role(id):
    role = Role.query.get(id)
    if request.method == 'POST':
        if role is not None:
            role.name = request.form['role_name']
            role.type = request.form['type']
            db.session.commit()
            return redirect(url_for('manual_admin.home'))
        flash('id: ' + str(id) + " not exists")
    return render_template('role.html', role=role)
