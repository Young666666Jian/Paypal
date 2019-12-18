# 1. Import the PayPal SDK client that was created in `Set up Server-Side SDK`.
from .paypalClient import PayPalClient
from paypalcheckoutsdk.payments import CapturesRefundRequest
import json


class RefundOrder(PayPalClient):

    # 2. Set up your server to receive a call from the client
    """Use the following function to refund an capture.
       Pass a valid capture ID as an argument."""

    def refund_order(self, capture_id, amount, currency_code, debug=False):
        request = CapturesRefundRequest(capture_id)
        request.prefer("return=representation")
        request.request_body(self.build_request_body(amount, currency_code))
        # 3. Call PayPal to refund an capture
        response = self.client.execute(request)
        if debug:
            print('Status Code:', response.status_code)
            print('Status:', response.result.status)
            print('Order ID:', response.result.id)
            print('Links:')
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(
                    link.rel, link.href, link.method))
            json_data = response.result._dict
            print("json_data: ", json_data)
        return response

    """Request body for building a partial refund request.
     For full refund, pass the empty body.
     For more details, refer to the Payments API refund captured payment reference."""
    @staticmethod
    def build_request_body(amount, currency_code):
        return \
            {
                "amount": {
                    "value": amount,
                    "currency_code": currency_code
                }
            }
