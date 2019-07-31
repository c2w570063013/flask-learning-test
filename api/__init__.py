from flask import Flask
from api.payment import payment_bp

def create_api_app():
    api_app = Flask(__name__)
    api_app.register_blueprint(payment_bp)
