from .paypalClient import PayPalClient
from paypalcheckoutsdk.orders import OrdersGetRequest
import json

class GetOrder(PayPalClient):
    # 2. Set up your server to receive a call from the client
    """You can use this function to retrieve an order by passing order ID as an argument"""

    def get_order(self, order_id):
        """Method to get order"""
        request = OrdersGetRequest(order_id)
        # 3. Call PayPal to get the transaction
        response = self.client.execute(request)
        # 4. Save the transaction in your database. Implement logic to save transaction to your database for future reference.
        transaction = {}
        transaction.update({ 'statusCode': response.status_code})
        print('Status Code: ', response.status_code)

        transaction.update({ 'status': response.result.status})
        print('Status: ', response.result.status)

        transaction.update({ 'orderId': response.result.id})
        print('Order ID: ', response.result.id)
        
        transaction.update({ 'inde': response.result.status})
        print('Intent: ', response.result.intent)
        
        print('Links:')
        links = []
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(
                link.rel, link.href, link.method))
            linkEle = { 'rel': link.rel, 'href': link.href, 'method':link.method }
            links.append(linkEle)
        transaction.update({ 'links': links })

        transaction.update({ 'currency': response.result.purchase_units[0].amount.currency_code, 'amount': response.result.purchase_units[0].amount.value })
        print('Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                           response.result.purchase_units[0].amount.value))
        print ('Capture Ids: ')
        for purchase_unit in response.result.purchase_units:
            for capture in purchase_unit.payments.captures:
                print ('\t', capture.id)
                print (capture._dict)
        return transaction