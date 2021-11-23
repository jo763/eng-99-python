# PIP - PIP Installs packages

import requests

request_bbc = requests.get("http://www.bbc.co.uk")

print(request_bbc, type(request_bbc), repr(request_bbc))

print(request_bbc.status_code)

print(request_bbc.headers)

print(request_bbc.content)