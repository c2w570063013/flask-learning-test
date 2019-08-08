from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from website import auth, home
from api import payment
from admin import auth as admin_auth

app.config.from_mapping(
    # a default secret that should be overridden by instance config
    SECRET_KEY="dev",
    # store the database in the instance folder
    # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:wayne@127.0.0.1/flask_test'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)

app.register_blueprint(auth.auth_blueprint)
app.register_blueprint(home.home_blueprint)
app.register_blueprint(payment.payment_bp)
app.register_blueprint(admin_auth.bp)

@app.route('/hello')
def hello():
    return 'hello'
