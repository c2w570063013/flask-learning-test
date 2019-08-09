from flask import render_template


def index():
    return render_template('home/index.html')


def error_page():
    return render_template('error.html')
