from flask import render_template, request, redirect, url_for


def role():
    if request.method == 'POST':
        return redirect(url_for('website.index'))
    return render_template('role.html')
