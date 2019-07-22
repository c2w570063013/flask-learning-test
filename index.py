from flask import Flask

app = Flask(__name__)

from website import auth, home
from api import payment

# register blueprints from website package
app.register_blueprint(auth.auth_blueprint)
app.register_blueprint(home.home_blueprint)
# register blueprints from api package
app.register_blueprint(payment.payment_bp)


@app.route('/hello')
def hello():
    return 'hello'
