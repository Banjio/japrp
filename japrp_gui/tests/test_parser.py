from japrp.parser import RadioBrowserSimple

searcher = RadioBrowserSimple()

def test_search_limited():
    name = "Swr 3"
    res = searcher.search_filter_by_codec(name, codecs=("mp3", "aac"), limit=10)
    print(res)
