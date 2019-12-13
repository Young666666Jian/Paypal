
from . import payment
from flask import jsonify, request
from paypal.checkout import GetOrder
import traceback

@payment.route("/order", methods=["POST"])
def order():
    if not request.json:
        return jsonify( {"message": "Missing JSON in request"} ), 400
    print (request.json['response']['orderID'])
    try:
        GetOrder().get_order(request.json['response']['orderID'])
    except Exception:
        traceback.print_exc()
    return jsonify({"message": "Payment Successfully."}), 200



