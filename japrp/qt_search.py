import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from japrp.parser import RadioBrowserSimple
from pprint import pprint

class ClickableSearchResult(QPushButton):

    def __init__(self, name, value):
        super().__init__()
        self.name_ref = name
        self.setObjectName(self.name_ref)
        self.value = value
        self.clicked.connect(self.onClick)

    def onClick(self):
        return self.value

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        container = QWidget()
        containerLayout = QVBoxLayout()
        container.setLayout(containerLayout)


        self.setCentralWidget(container)
        self.searchbar = QLineEdit(container)
        self.searchbar.setGeometry(QtCore.QRect(140, 70, 104, 78))
        self.searchbar.returnPressed.connect(self.search_radio)
        self.searcher = RadioBrowserSimple()

        self.scroll_area = QScrollArea()

    def search_radio(self):
        temp_search = self.searcher.search_limited(name=self.searchbar.text(), limit=10)
        res = self.searcher.process_result(temp_search)
        pprint(res.keys())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())