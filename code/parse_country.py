import geoplotlib
from geoplotlib.utils import read_csv
import csv



def grab_csv(file):
    with open(file) as file_csv:
        reader = csv.reader(file_csv, delimiter=',')
        return reader


def parse_country(file, country):
    with open(file) as file_csv:
        reader = csv.reader(file_csv, delimiter=',')
        count = 0
        for row in reader:
            if count == 0:
                count+= 1
            else:
                if country == row[0]:
                    return row[1]
                else:
                    pass


file = "data_sets/countries.csv"
grabbed_country = parse_country(file,"IT")
print(grabbed_country)
