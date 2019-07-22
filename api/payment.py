from flask import Blueprint

payment_bp = Blueprint('payment', __name__, url_prefix='/api/payment/')


@payment_bp.route('/test')
def test():
    return 'this is for debugging test'
