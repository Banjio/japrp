import sys
import requests
from io import StringIO
from japrp.app.main_window import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from japrp.app_parts.qt_search import ClickableSearchResult
from japrp.parser import RadioBrowserSimple
from japrp.audio_backends.audio_backend_vlc import VlcBackend
from japrp.audio_backends.audio_backend_pyqt5 import QtMediaPlayerWrapper

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
        self.ui.searchedContent.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.searchedContent.setWidgetResizable(True)

        self._station_icon_default = QPixmap("../../img/empty_icon.png")
        self._station_name_default = ""
        self.ui.sender_icon.setPixmap(self._station_icon_default)

        self.ui.sender_name.setText(self._station_name_default)


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
            widget.play_btn.clicked.connect(lambda: self.openPlayer(widget))
            self.search_results.append(widget)
            self.containerLayout.addWidget(widget)

        self.containerWidget.setLayout(self.containerLayout)
        self.ui.searchedContent.setWidget(self.containerWidget)

    def openPlayer(self, widget):
        # TODO: There is a bug where we always acess the same widget, Downloading image not working
        self.player.stop()
        print(widget.value["url"])
        self.player.set_media(widget.value["url"])
        self.player.play()
        temp_icon_value = widget.value.get("favicon")
        if temp_icon_value is not None or len(temp_icon_value):
            icon_decoded = requests.get(temp_icon_value)
            if icon_decoded.ok:
                #temp = StringIO()
                #with open(temp, "wb") as f:
                #    f.write(icon_decoded.content)
                #    self.ui.sender_icon.setPixmap(QPixmap(temp))
                pass
            else:
                self.ui.sender_icon.setPixmap(self._station_icon_default)

        else:
            self.ui.sender_icon.setPixmap(self._station_icon_default)

        temp_station_name = widget.value.get("name")
        if temp_station_name is not None or len(temp_station_name):
            self.ui.sender_name.setText(temp_station_name)
        else:
            self.ui.sender_name.setText(self._station_name_default)


    def start_playing(self):
        # self.stream = subprocess.Popen(["python", "-m", "streamer_script.py"], stdout=sys.stdout)
        if _BACKEND == "vlc":
            if self.player.media_player.is_playing():
                self.player.pause()
            else:
                self.player.play()
        else:
            self.player.play()

    def stop_playing(self):
        if self.player is not None:
            self.player.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Japrp()
    w.show()
    sys.exit(app.exec())
