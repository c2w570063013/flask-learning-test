from flask import Flask


def create_website_app():
    website_app = Flask(__name__)

    from website.home import home_blueprint
    from website.auth import auth_blueprint

    website_app.register_blueprint(home_blueprint)
    website_app.register_blueprint(auth_blueprint)
    return website_app
