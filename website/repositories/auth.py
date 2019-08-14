from flask import request, redirect, url_for, render_template, session, g, flash
import hashlib
from website.models import User, db


def load_logged_in_user():
    """
    invoked before login
    :return:
    """
    user_id = session.get('user_id')
    g.user = None
    if user_id is not None:
        g.user = User.query.filter_by(id=user_id).first()


def login():
    """
    login function
    :return:
    """
    if request.method == 'POST':
        email = request.form['email']
        pwd = hashlib.md5(request.form['password'].encode()).hexdigest()
        user = User.query.filter_by(email=email, password=pwd).first()
        if user is None:
            return redirect(url_for('website.login'))
        session.clear()
        session['user_id'] = user.id
        return redirect(url_for('website.index'))
    return render_template('auth/login.html')


def register():
    """
    login function
    :return:
    """

    if request.method == 'POST':
        email = request.form['email']
        # hashing pwd with md5 encryption
        pwd = hashlib.md5(request.form['password'].encode()).hexdigest()
        user = User(email=email, password=pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('website.login'))
    return render_template('auth/register.html')


def logout():
    """
    logout
    :return:
    """
    session.clear()
    return redirect(url_for('website.index'))
