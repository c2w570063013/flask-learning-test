from flask import request, redirect, url_for, render_template, session
import hashlib
from website.models import User, db


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
        # session['user_id'] = user['id']
        # print(user['id'])
        print(user.__dict__)
        return redirect(url_for('website.index'))
    return render_template('auth/login.html')


def register():
    """
    login function
    :return:
    """
    if request.method == 'POST':
        email = request.form['email']
        pwd = hashlib.md5(request.form['password'].encode()).hexdigest()
        user = User(email=email, password=pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('website.login'))
    return render_template('auth/register.html')
