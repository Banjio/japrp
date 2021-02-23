import sys
import requests
from io import StringIO, BytesIO
from japrp.app.main_window import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPixmap
from japrp.app_parts.qt_search import ClickableSearchResult
from japrp.parser import RadioBrowserSimple
from japrp.audio_backends.audio_backend_vlc import VlcBackend
from japrp.audio_backends.audio_backend_pyqt5 import QtMediaPlayerWrapper
from functools import partial

_BACKEND = "vlc"
_SEARCH_LIMIT = 20

class Japrp(QMainWindow):

    def __init__(self):
        super(Japrp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.search_results = []
        self.searcher = RadioBrowserSimple()
        if _BACKEND == "vlc":
            self.player = VlcBackend()
        else:
            self.player = QtMediaPlayerWrapper()
        self.ui.searchbar.returnPressed.connect(self.search_radio)

        self.ui.play.clicked.connect(self.start_playing)
        self.ui.stop.clicked.connect(self.stop_playing)

        self.ui.searchedContent.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.searchedContent.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.searchedContent.setWidgetResizable(True)

        self._station_icon_default = QPixmap("../../img/empty_icon.png")
        self._station_name_default = ""
        self.ui.sender_icon.setPixmap(self._station_icon_default)

        self.ui.sender_name.setText(self._station_name_default)

        self.ui.volumeSlider.setValue(100)
        self.ui.volumeSlider.valueChanged.connect(self.set_volume)

    @pyqtSlot()
    def search_radio(self):
        # To dynamically create and add to scroll area we need a container. We create the container inside the function, s.t. it is reseted between searchs
        self.containerWidget = QWidget()
        self.containerLayout = QVBoxLayout()
        if not self.search_results:
            self.search_results = []
        if len(self.search_results) > 0:
            self.search_results = []
        temp_search = self.searcher.search_limited(name=self.ui.searchbar.text(), limit=_SEARCH_LIMIT)
        res = self.searcher.process_result(temp_search)
        for key, val in res.items():
            widget = ClickableSearchResult(key, val)
            #print(widget)
            self.search_results.append(widget)
            # Use partial instead of lambda functions here, because with lambda the value passed to the function will
            # be set to len(list) after it is created -> see for details: https://stackoverflow.com/questions/45090982/passing-extra-arguments-through-connect
            widget.play_btn.clicked.connect(partial(self.openPlayer, len(self.search_results) - 1))
            self.containerLayout.addWidget(widget)

        self.containerWidget.setLayout(self.containerLayout)
        self.ui.searchedContent.setWidget(self.containerWidget)

    @pyqtSlot(int)
    def openPlayer(self, idx_widget):
        self.player.stop()
        self.player.set_media(self.search_results[idx_widget].value["url"])
        self.player.play()
        temp_icon_value = self.search_results[idx_widget].value.get("favicon")
        if temp_icon_value is not None:
            if len(temp_icon_value) > 0:
                icon_decoded = requests.get(temp_icon_value)
                if icon_decoded.ok:
                    qp = QPixmap()
                    qp.loadFromData(icon_decoded.content)
                    qp.scaled(1, 1, Qt.IgnoreAspectRatio)
                    self.ui.sender_icon.setPixmap(qp)
                    self.ui.sender_icon.setScaledContents(True)
                else:
                    self.ui.sender_icon.setPixmap(self._station_icon_default)

        else:
            self.ui.sender_icon.setPixmap(self._station_icon_default)

        temp_station_name = self.search_results[idx_widget].value.get("name")
        if temp_station_name is not None:
            if len(temp_station_name) > 0:
                self.ui.sender_name.setText(temp_station_name)
            else:
                self.ui.sender_name.setText(self._station_name_default)

    @pyqtSlot()
    def start_playing(self):
        # self.stream = subprocess.Popen(["python", "-m", "streamer_script.py"], stdout=sys.stdout)
        if _BACKEND == "vlc":
            if self.player.media_player.is_playing():
                self.player.pause()
            else:
                self.player.play()
        else:
            self.player.play()

    @pyqtSlot()
    def stop_playing(self):
        if self.player is not None:
            self.player.stop()

    @pyqtSlot()
    def set_volume(self):
        self.player.set_volume(self.ui.volumeSlider.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Japrp()
    w.show()
    sys.exit(app.exec())
