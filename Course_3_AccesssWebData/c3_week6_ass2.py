import urllib.request as ur
import urllib.parse as up
import json

service_url = "http://python-data.dr-chuck.net/geojson?"

address = input("Enter location: ")
params = {"sensor": "false", "address": address}
url = service_url + up.urlencode(params)
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id", place_id)