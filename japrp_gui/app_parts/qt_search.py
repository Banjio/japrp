import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPainter
from japrp_core.parser import RadioBrowserSimple
from japrp_gui.app_parts.dict_viewer_pyqt5 import DictViewTree, DictTreeViewAsDialog
from pprint import pprint
import json

class ClickableSearchResult(QWidget):

    def __init__(self, name: str, value: dict):
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

    @pyqtSlot()
    def show_details(self):
        view = DictTreeViewAsDialog(dict_=self.value)
        view.exec()

class RadioSeacherView(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # self = container
        #self.container = QWidget(self)
        self.model = RadioSeacherModel()
        #self.search_results = []
        self.searchbar = QLineEdit()
        self.search_result = []
        # Scroll area, i.e. space where results are displayed
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.containerLayout = QVBoxLayout()
        self.containerLayout.addWidget(self.searchbar)
        self.containerLayout.addWidget(self.scroll)
        self.setLayout(self.containerLayout)
        #Use self as container instead of creating an extra container widget
        #self.container.setLayout(self.containerLayout)
        #self.setGeometry(800, 100, 800, 600)
        self.setWindowTitle("Control Panel")
        self.searcher = RadioBrowserSimple()
        self.searchbar.returnPressed.connect(self.search_radio)

    def search_radio(self):
        self.model.search(self.searchbar.text())
        scrollWidget = QWidget(self.scroll)
        scrollWidgetLayout = QVBoxLayout(scrollWidget)
        self.scroll.setWidget(scrollWidget)
        self.search_result = [ClickableSearchResult(key, val) for key, val in self.model.search_result.items()]
        for wi in self.search_result:
            scrollWidgetLayout.addWidget(wi)


class RadioSeacherModel(object):

    def __init__(self):
        self.search_result: dict = {}
        self.rb = RadioBrowserSimple()

    def search(self, name):
        temp_search = self.rb.search_limited(name, limit=15)
        self.search_result = self.rb.process_result(temp_search)



class RadioSeacherAsMain(QMainWindow):

    def __init__(self):
        super().__init__()
        self.search_model = RadioSeacherModel()
        self.search_view = RadioSeacherView(self.search_model)
        self.setCentralWidget(self.search_view)
        self.resize(1000,1000)

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
        self.container = QWidget()
        self.containerLayout = QVBoxLayout()
        self.containerLayout.addWidget(self.searchbar)
        self.containerLayout.addWidget(self.scroll)
        self.container.setLayout(self.containerLayout)
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
    w = RadioSeacherAsMain()
    w.show()
    sys.exit(app.exec_())