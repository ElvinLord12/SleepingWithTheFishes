import requests
import json
import keys
import csv

import random
import decimal

def get_geo_api(country, key):
    url="https://api.opencagedata.com/geocode/v1/json?key=" + key + "&q=" + country + "&pretty=1&no_annotations=1"

    got = requests.get(url)

    data = got.json()

    with open('./json/single_country.json', 'w') as f:
        json.dump(data,f, indent=2)

    return data

def create_csv(file_out, file_in):
    with open(file_out, mode='w') as out_file:
        writer = csv.writer(out_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")

        writer.writerow(["Name", "lat", "lon"])
        count = 0
        with open(file_in) as in_file:
            reader = csv.reader(in_file, delimiter=',')
            for row in reader:
                if count == 0:
                    count += 1
                else:
                    data = get_geo_api(row[1],keys.key)
                    writer.writerow([row[1], get_lat(data), get_lon(data)])


def get_lon(data):
    results = data['results']
    geometry = results[0]
    coord = geometry['geometry']
    long = coord['lng']
    lng_float = float(long)
    lng_noise = account_for_noise(lng_float)
    lng_final = str(lng_noise)
    return lng_final



def get_lat(data):
    results = data['results']
    geometry = results[0]
    coord = geometry['geometry']
    lati = coord['lat']
    lat_float = float(lati)
    lat_noise = account_for_noise(lat_float)
    lat_final = str(lat_noise)
    return lat_final


def account_for_noise(value):
    noise = float(random.randrange(5, 150))/100
    value += noise
    return value


create_csv("testmap1.csv", "out.csv")