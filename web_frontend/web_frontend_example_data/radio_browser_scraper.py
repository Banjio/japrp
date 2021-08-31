from pyradios import RadioBrowser
import json

browser = RadioBrowser()

res = browser.search(name="Rockantenne")

with open("example_frontend.json", "w") as f:
    json.dump(res, f)