import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter
from japrp.parser import RadioBrowserSimple
from japrp.dict_viewer_pyqt5 import DictViewTree, DictTreeViewAsDialog
from pprint import pprint
import json

class ClickableSearchResult(QWidget):

    def __init__(self, name, value):
        super().__init__()
        self.name_ref = name
        self.value = value

        self.station_name = QLabel(self.name_ref)
        self.play_btn = QPushButton("Play")
        self.details = QPushButton("Details")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.station_name)
        self.hbox.addWidget(self.play_btn)
        self.hbox.addWidget(self.details)
        self.setLayout(self.hbox)

        self.details.clicked.connect(self.show_details)

    def show_details(self):
        view = DictTreeViewAsDialog(dict_=self.value)
        view.exec()

class RadioSearcher(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.search_results = []
        self.searchbar = QLineEdit()

        # Scroll area, i.e. space where results are displayed
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        #self.scroll.setWidget(self)

        #self.searchbar.setGeometry(QtCore.QRect(140, 70, 104, 78))

        # Add the items to VBoxLayout (applied to container widget)
        # which encompasses the whole window.
        #container = QWidget()
        #containerLayout = QVBoxLayout()
        #containerLayout.addWidget(self.searchbar)
        #containerLayout.addWidget(self.scroll)
        #container.setLayout(containerLayout)
        self.container = QWidget()
        self.containerLayout = QVBoxLayout()
        self.containerLayout.addWidget(self.searchbar)
        self.containerLayout.addWidget(self.scroll)
        self.container.setLayout(self.containerLayout)
        #self.setLayout(self.layout)

        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle("Control Panel")

        self.searchbar.returnPressed.connect(self.search_radio)
        self.searcher = RadioBrowserSimple()
        self.setCentralWidget(self.container)


    def search_radio(self):
        if not self.search_results:
            self.search_results = []
        temp_search = self.searcher.search_limited(name=self.searchbar.text(), limit=10)
        res = self.searcher.process_result(temp_search)
        for key, val in res.items():
            widget = ClickableSearchResult(key, val)
            widget.play_btn.clicked.connect(lambda: self.openPlayer(widget))
            self.search_results.append(widget)
            self.containerLayout.addWidget(widget)


    def openPlayer(self, clickable_search_result):
        print(clickable_search_result.value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = RadioSearcher()
    w.show()
    sys.exit(app.exec_())