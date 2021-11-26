import requests, json
from pprint import pprint
def find_location(postcode):
    request_link = 'https://api.postcodes.io/postcodes/' + postcode
    postcode_req = requests.get(
        request_link
    )

    print(postcode_req)
    if postcode_req.status_code == 200:
        # print(postcode_req.headers)
        # pprint(postcode_req.json(), sort_dicts=False)
        # print(type(postcode_req.json()))#
        # print(postcode_req.content)
        postcode = postcode_req.json()

    # Preint the eatings and northigns of the requested postcode

    print(postcode['result']["eastings"])
    print(postcode['result']["northings"])

find_location("SW1A1AA")
# HTTP Request

# VERB - URL - VERSION
# Header - key-value pairs (metadata)
# body - data that accompanies the text i.e. text, json, xml etc

# HTTP Response

# Response code (e.g. 200/404)
# HTTP Version
# Headers
# Body

postcode_headers = {"Content-Type": "application/json"}
#json_data = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
json_data = {"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]}

multi_req = requests.post(
    'https://api.postcodes.io/postcodes/',
    headers=postcode_headers,
    #data=json_data
    json = json_data
)
print("\n" *8)
#print(multi_req)
#print(multi_req.json())
results = multi_req.json()['result']
print(results)
for i in results:
    #print(i)
    postcode = i['query']
    latitude = i['result']['latitude']
    longitude = i['result']['longitude']
    print(f"{postcode} - Latitude: {latitude}, Longitude: {longitude}")

class postcode_finder:
    def __init__(self, postcode):
        self.postcode = postcode
        self.eastings, self.northings, self.lat, self.long = self.postcode_find(self.postcode)
        pass

    def postcode_find(self, postcode):
        request_link = 'https://api.postcodes.io/postcodes/' + postcode
        postcode_req = requests.get(
            request_link
        )

        print(postcode_req)
        if postcode_req.status_code == 200:
            postcode = postcode_req.json()
            results = postcode['result']
            eastings = results["eastings"]
            northings = results["northings"]
            lat = results["latitude"]
            long = results["longitude"]
            return eastings, northings, lat, long

x = postcode_finder("SW1A1AA")

print(f"{x.postcode} - Latitude: {x.lat}, Longitude: {x.long}")

# create a postcode class
# that can hold tat/long and eastings/northings
# for a single postcode
# Maybe a method is called in the __init__, which takes a postcode string and makes the API call









