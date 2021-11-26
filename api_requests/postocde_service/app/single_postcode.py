from .config_manager import base_url
from .models.single_postcode_model import SinglePostcodeModel
import requests


class SinglePostcode:
    def __init__(self, single_postcode):
        # make a request
        # Provide a method returns the response data modelling as a singlepostcodemodel
        self.url = base_url() + single_postcode
        self.request = requests.get(self.url)
        self.headers = self.request.headers
        self.response_json = self.request.json()

    def response_data(self):
        return SinglePostcodeModel(self.response_json)


# x = SinglePostcode("SW1A1AA")
# print(x.url)
