from pyradios import RadioBrowser
from pprint import pprint


class RadioBrowserSimple(RadioBrowser):

    def __init__(self):
        super(RadioBrowserSimple, self).__init__()


    def search_limited(self, name, limit=20, **kwargs):
        return self.search(name=name, limit=limit, **kwargs)

    def search_filter_by_country(self, name, country):
        return self.search(name=name, country=country)

    def search_filter_by_tag(self, name, tag):
        return self.search(name=name, tag=tag)

    def search_filter_by_coded(self, name, codec):
        codec = codec.upper()
        return self.search(name=name, codec=codec)

    def search_station_no_proxy(self, name):
        temp_res = self.search(name=name)
        res = list(filter(lambda x: "addradio" not in x["url"], temp_res))
        return res

    @staticmethod
    def process_result(result):
        unique_names = []
        unique_names_counter = {}
        res = {}
        for item in result:
            name_temp = item["name"]
            if item["name"] not in unique_names:
                unique_names.append(item["name"])
                unique_names_counter[item["name"]] = 1
                res[name_temp] = item
            elif item["name"] in unique_names:
                name_temp += "_" + str(unique_names_counter[item["name"]])
                unique_names_counter[item["name"]] += 1
                res[name_temp] = item
        return res

if __name__ == "__main__":
    rbs = RadioBrowserSimple()
    pprint(rbs.search_filter_by_tag("Swr", "rock"))
    res = rbs.search_station_no_proxy("swr")
    pprint(rbs.process_result(res))
