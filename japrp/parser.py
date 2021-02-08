from pyradios import RadioBrowser
from pprint import pprint

rb = RadioBrowser()
stations = rb.search(name="BBC", limit=20)
pprint(stations)