import sys
from japrp.app.main_window import Ui_MainWindow
from PyQt5.QtWidgets import *
from japrp.app_parts.qt_search import ClickableSearchResult
from japrp.parser import RadioBrowserSimple
from japrp.audio_backends.audio_backend_vlc import VlcBackend
from japrp.audio_backends.audio_backend_pyqt5 import QtMediaPlayerWrapper

_BACKEND = "vlc"

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

    def search_radio(self):
        if not self.search_results:
            self.search_results = []
        if len(self.search_results) > 0:
            self.search_results = []
            self.ui.searcherLayout.removeWidget()
        temp_search = self.searcher.search_limited(name=self.ui.searchbar.text(), limit=10)
        res = self.searcher.process_result(temp_search)
        for key, val in res.items():
            widget = ClickableSearchResult(key, val)
            widget.play_btn.clicked.connect(lambda: self.openPlayer(widget))
            self.search_results.append(widget)
            self.ui.searcherLayout.addWidget(widget)

    def openPlayer(self, widget):
        self.player.set_media(widget.value["url"])
        self.player.play()

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
