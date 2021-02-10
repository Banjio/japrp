from pyradios import RadioBrowser
from pprint import pprint

rb = RadioBrowser()
stations = rb.search(name="Swr3", limit=1)
pprint(stations)