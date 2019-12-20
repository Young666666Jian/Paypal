
from . import paypal
from flask import jsonify, request
from paypal.checkout import GetOrder
from paypal.refund import RefundOrder
from paypalrestsdk import BillingPlan, configure, Payment, Api, Sale
import logging
import json
logging.basicConfig(level=logging.INFO)
my_api = Api({
    'mode': 'sandbox',
    'client_id': 'AYt31Z0myIBIQFgluo0_MmIg9sbIhNgig7B7CL7iLXwPKeK9CMPyl1jsesT025Bm_rGHnpKTgaoyRLwM',
    'client_secret': 'ECvbE5-MGXyZ94u6ne8QqIbm2k0KHHb8GLsfhG9TsZSShfEIZDU89qHElfPNs2pplCkpwuPanmaRAanH'})
# verify payment
@paypal.route("/order", methods=["POST"])
def order():
    if not request.json:
        return jsonify({"message": "Missing JSON in request"}), 400
    print(request.json['response']['orderID'])
    try:
        GetOrder().get_order(request.json['response']['orderID'])
    except Exception:
        return jsonify({"Error": "Payment Failed."}), 500
    print("Info: Payment Successfully.")
    return jsonify({"message": "Payment Successfully."}), 200

#  api v1/payments has deprecated, only can get payment info from api order and authorized
@paypal.route("/paymentDetail", methods=["GET"])
def paymentDetail():
    arguments = request.args
    orderId = arguments.get('orderID')
    authorizationId = arguments.get('authorizationId')
    if orderId:
        # or from data base
        paymentInfo = GetOrder().get_order(orderId)
    elif authorizationId:
        paymentInfo = GetOrder().get_order(authorizationId)
    return jsonify({"result": json.dumps(paymentInfo)}), 200

@paypal.route("/refund", methods=["GET"])
def refund():
    arguments = request.args
    orderId = arguments.get('orderID')
    if not orderId:
        return jsonify({"error": "no order ID"}), 500
    paymentInfo = GetOrder().get_order(orderId)
    if paymentInfo:
        amount = paymentInfo['amount']
        currency = paymentInfo['currency']
    else:
        return jsonify({"error": "Cannot get payment info"}), 500
    try:
        RefundOrder().refund_order('14G34927SX986220R', amount, currency, debug=True)
    except Exception as err:
        errData = err.__dict__
        errMsg = json.loads(errData['message'])
        return jsonify({"error": errMsg['details']}), 500
    return jsonify({"message": "refund successfully"}), 200


@paypal.route("/execute", methods=["GET"])
def execute():
    arguments = request.args
    print(arguments)


@paypal.route("/createPlan", methods=["POST"])
def subscription():
    if not request.json or not request.json['plan']:
        return jsonify({"message": "Missing JSON in request"}), 400
    plan = request.json['plan']
    billing_plan = BillingPlan(plan, my_api)
    try:
        response = billing_plan.create()
        print(billing_plan)
    except Exception:
        return jsonify({"Error": response.error}), 500
    return jsonify({"message": "refund successfully"}), 200
