from flask import Blueprint

payment_bp = Blueprint('payment', __name__, url_prefix='/api')


@payment_bp.route('/test')
def test1():
    return 'this is for debugging test'
