import requests
import json
import keys

def get_geo_api(country, key):
    url="https://api.opencagedata.com/geocode/v1/json?key=" + key + "&q=" + country + "&pretty=1&no_annotations=1"

    got = requests.get(url)

    data = got.json()

    with open('./json/single_country.json', 'w') as f:
        json.dump(data,f, indent=2)

    return data

print(get_geo_api("Denmark", keys.key))