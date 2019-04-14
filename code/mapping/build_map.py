import geoplotlib
from geoplotlib.utils import read_csv

data = read_csv('test_map2.csv')
geoplotlib.dot(data)
geoplotlib.show()