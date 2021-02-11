import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter
from japrp.parser import RadioBrowserSimple
from pprint import pprint
import json

class ClickableSearchResult(QWidget):

    def __init__(self, name, value):
        super().__init__()
        self.name_ref = name
        #self.setText(self.name_ref)
        self.value = value

        self.media_button = QPushButton(self.name_ref)
        self.details = QPushButton("Details")

        self.details.clicked.connect(self.onClick)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.media_button)
        self.hbox.addWidget(self.details)
        self.setLayout(self.hbox)

        self.msg = QMessageBox()
        self.details.clicked.connect(self.onClick)

    def onClick(self):
        self.msg.setText(json.dumps(self.value))

    def showdialog():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect()

        retval = msg.exec_()
        print
        "value of pressed message box button:", retval

    def msgbtn(i):
        print
        "Button pressed is:", i.text()

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.controls = QWidget()
        self.controlsLayout = QVBoxLayout()

        self.search_results = []
        self.controls.setLayout(self.controlsLayout)

        # Scroll area, i.e. space where results are displayed
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        self.searchbar = QLineEdit()
        #self.searchbar.setGeometry(QtCore.QRect(140, 70, 104, 78))

        # Add the items to VBoxLayout (applied to container widget)
        # which encompasses the whole window.
        container = QWidget()
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(self.searchbar)
        containerLayout.addWidget(self.scroll)
        container.setLayout(containerLayout)

        self.setCentralWidget(container)
        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle("Control Panel")

        self.searchbar.returnPressed.connect(self.search_radio)
        self.searcher = RadioBrowserSimple()




    def search_radio(self):
        if not self.search_results:
            self.search_results = []
        temp_search = self.searcher.search_limited(name=self.searchbar.text(), limit=10)
        res = self.searcher.process_result(temp_search)
        for key, val in res.items():
            widget = ClickableSearchResult(key, val)
            widget.media_button.clicked.connect(widget.onClick)
            self.search_results.append(widget)
            self.controlsLayout.addWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())