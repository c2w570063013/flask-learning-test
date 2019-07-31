from flask import Flask

from admin import auth

app = Flask(__name__)
app.register_blueprint(auth.bp)
