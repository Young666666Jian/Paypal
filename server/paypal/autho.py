# 1. Import the PayPal SDK client that was created in `Set up Server-Side SDK`.
from .paypalClient import PayPalClient
from paypalcheckoutsdk.payments import AuthorizationsCaptureRequest
import json

class CaptureAuthorization(PayPalClient):

  #2. Set up your server to receive a call from the client
  """Use this function to capture an approved authorization.
     Pass a valid authorization ID as an argument to this function."""
  def capture_auth(self, authorization_id, debug=False):
    """Method to capture order using authorization_id"""
    request = AuthorizationsCaptureRequest(authorization_id)
    request.request_body(self.build_request_body())
    # 3. Call PayPal to capture an authorization.
    response = self.client.execute(request)
    # 4. Save the capture ID to your database for future reference.
    if debug:
      print 'Status Code: ', response.status_code
      print 'Status: ', response.result.status
      print 'Capture ID: ', response.result.id
      print 'Links: '
      for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
      json_data = self.object_to_json(response.result)
      print "json_data: ", json.dumps(json_data,indent=4)
    return response

  """Sample request body to Capture Authorization."""
  @staticmethod
  def build_request_body():
    return {}