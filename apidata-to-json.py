
import json
import requests

data = requests.get("https://ssd-api.jpl.nasa.gov/fireball.api")
json_data = json.loads(data.text)
# print(json_data)
json_object = json.dumps(json_data, indent = 4) 
# print(json_object)
with open("api_data.json", "w") as outfile:
    outfile.write(json_object)