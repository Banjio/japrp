from japrp.app_parts import qt_search
import sys

def test_qt_search():
    result = qt_search.ClickableSearchResult("Name", {})
    result.show()
    sys.exit(result.close())