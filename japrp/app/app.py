import sys
import requests
import logging
from io import StringIO, BytesIO
from japrp.app.main_window import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSlot, QTimer
from PyQt5.QtGui import QPixmap
from japrp.app_parts.qt_search import ClickableSearchResult
from japrp.parser import RadioBrowserSimple
from japrp.audio_backends.audio_backend_vlc import VlcBackend
from japrp.audio_backends.audio_backend_pyqt5 import QtMediaPlayerWrapper
from functools import partial

_BACKEND = "vlc"
_SEARCH_LIMIT = 20
_SONG_UPDATE_TIMER = 50 * 1000
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#https://github.com/baoboa/pyqt5/blob/master/examples/multimediawidgets/player.py how to make pyqt5 media playr work with playlist
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

        self.ui.volumeSlider.setValue(self.player.get_volume())
        self.ui.volumeSlider.valueChanged.connect(self.set_volume)

        self.player_is_active = False

        self.ui.song_title.setWordWrap(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_song_name)
        self.timer.start(_SONG_UPDATE_TIMER)


    def get_song_name(self):
        print("Updating Song Title")
        if self.player_is_active:
            title = self.player.get_meta_data_icy(self.player.get_url())
            self.ui.song_title.setText(title)
        self.timer.start(_SONG_UPDATE_TIMER)

    @pyqtSlot()
    def search_radio(self):
        # To dynamically create and add to scroll area we need a container. We create the container inside the function, s.t. it is reseted between searchs
        self.containerWidget = QWidget()
        self.containerLayout = QVBoxLayout()
        if not self.search_results:
            self.search_results = []
        if len(self.search_results) > 0:
            self.search_results = []
        if _BACKEND == "vlc":
            temp_search = self.searcher.search_limited(name=self.ui.searchbar.text(), limit=_SEARCH_LIMIT)
        else:
            _CODECS = ("mp3", "aac")
            temp_search = self.searcher.search_filter_by_codec(self.ui.searchbar.text(), codecs=_CODECS, limit=_SEARCH_LIMIT)
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
        self.ui.searchedContent.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

    @pyqtSlot(int)
    def openPlayer(self, idx_widget):
        self.player.stop()
        self.player.set_media(self.search_results[idx_widget].value["url"])
        self.player.play()
        self.ui.song_title.setText("")
        temp_icon_value = self.search_results[idx_widget].value.get("favicon")
        if temp_icon_value is not None:
            if len(temp_icon_value) > 0:
                url_ok = False
                try:
                    icon_decoded = requests.get(temp_icon_value, timeout=5)
                    url_ok = icon_decoded.ok
                except requests.RequestException as e:
                    logger.exception("Icon Url was not ok because of exception %s" %e)
                if url_ok:
                    qp = QPixmap()
                    qp.loadFromData(icon_decoded.content)
                    qp.scaled(2, 2, Qt.KeepAspectRatioByExpanding)
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
        self.player_is_active = True

    #@pyqtSlot()
    def start_playing(self):

        # self.stream = subprocess.Popen(["python", "-m", "streamer_script.py"], stdout=sys.stdout)
        try:
            if self.player.get_is_playing():
                self.player.pause()
                logger.debug("Pause player")
            else:
                self.player.play()
                logger.debug("Start playing")
        except ValueError as ex:
            logger.exception("Play was hit before a media was selected: %s" %ex)

    @pyqtSlot()
    def stop_playing(self):
        print("Stopping")
        if self.player.media is not None or self.player is not None:
            self.player.stop()
            logger.debug("Stop playing")
        self.player_is_active = False

    @pyqtSlot()
    def set_volume(self):
        self.player.set_volume(self.ui.volumeSlider.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = Japrp()
    w.show()
    sys.exit(app.exec())
