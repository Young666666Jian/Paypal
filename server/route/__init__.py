from flask import Blueprint
paypal = Blueprint("paypal", __name__, url_prefix="/api/v1/paypal")
alipay = Blueprint("alipay", __name__, url_prefix="/api/v1/alipay")