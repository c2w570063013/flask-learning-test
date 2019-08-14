from flask import render_template


def index():
    from website.models import User, db
    xx = User.query.filter_by(id=1).first()
    # print(xx['email'], 'ksdkgkdskg')
    return render_template('home/index.html')


def error_page():
    return render_template('error.html')
