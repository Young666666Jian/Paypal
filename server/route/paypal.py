
from . import paypal
from flask import jsonify, request
from paypal.checkout import GetOrder
from paypalrestsdk import BillingPlan, configure, Payment, Api
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
        return jsonify( {"message": "Missing JSON in request"} ), 400
    print (request.json['response']['orderID'])
    try:
        GetOrder().get_order(request.json['response']['orderID'])
    except Exception:
        return jsonify({"Error": "Payment Failed."}), 500
    print ("Info: Payment Successfully.")
    return jsonify({"message": "Payment Successfully."}), 200

#  api v1/payments has deprecated
@paypal.route("/paymentDetail", methods=["GET"])
def paymentDetail():
    arguments = request.args
    orderId = arguments.get('orderID')
    authorizationId = arguments.get('authorizationId')
    if orderId:
        paymentInfo = GetOrder().get_order(orderId)
    elif authorizationId:
        paymentInfo = GetOrder().get_order(authorizationId)
    print(paymentInfo)
    return jsonify({"result": paymentInfo}), 200

@paypal.route("/refund", methods=["GET"])
def refund():
    return jsonify({"message": "Payment Successfully."}), 200

@paypal.route("/execute", methods=["GET"])
def execute():
    arguments = request.args
    print(arguments)

@paypal.route("/subscription", methods=["POST"])
def subscription():
    if not request.json and request.json['response']:
        return jsonify( {"message": "Missing JSON in request"} ), 400
    elif not request.json['response']['plan'] and request.json['response']['payment_definitions'] and request.json['response']['type']:
        return jsonify( {"message": "Missing parameters in request"} ), 400
    plan = request.json['response']['plan']
    payment_definitions = request.json['response']['payment_definitions']
    subscriptionType = request.json['response']['type']
    billing_plan = BillingPlan(plan, payment_definitions, subscriptionType)
    try:
        response = billing_plan.create()
        print (response)
    except Exception:
        return jsonify({"Error": response.error}), 500