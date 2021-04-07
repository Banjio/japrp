from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QHBoxLayout, QWidget
from japrb_gui import *
import sys
#sys.path.append("../")
from japrp.audio_backends.audio_backend_vlc import VlcBackend
from japrp.audio_backends.audio_backend_pyqt5 import QtMediaPlayerWrapper
from japrp.app_parts.qt_search import RadioSearcher
from japrp.app_parts.player_qt import Player

_BACKEND = "vlc"

class MyApp(QDialog):

    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        if _BACKEND == "vlc":
            self.player = VlcBackend()
        else:
            self.player = QtMediaPlayerWrapper()
        self.ui.playBtn.clicked.connect(self.start_playing)
        self._url = ""
        self.ui.setBtn.clicked.connect(self.set_url)


    def start_playing(self):
        #self.stream = subprocess.Popen(["python", "-m", "streamer_script.py"], stdout=sys.stdout)
        if self._url == "":
            pass
        if _BACKEND == "vlc":
            if self.player.media_player.is_playing():
                self.player.pause()
            else:
                self.player.play()
        else:
            self.player.play()

    def set_url(self):
        #URL = "http://bob.hoerradar.de/radiobob-hartesaite-mp3-hq?sABC=6020sp0s%230%23r731s0685son37qn82q119rrn30n0ss5%23zrqvncynlre&=&amsparams=playerid:mediaplayer;skey:1612774415"  # BBC
        #URL = "http://mp3-live.swr3.de/swr3_m.m3u"
        self._url = self.ui.enterUrl.show()
        if self._url == "" or self._url is None:
            pass
        else:
            self.player.set_media(self._url, media_type='infer')


    def closeEvent(self, event):
       #quit_msg = "Are you sure you want to exit the program?"
       if self.player is not None:
           self.player.stop()

class MyApp2(QMainWindow):

    def __init__(self):
        super(MyApp2, self).__init__()

        self.player = Player(parent=self)
        self.searcher = RadioSearcher()
        self.container = QWidget()
        self.containerLayout = QHBoxLayout()
       #self.layout.addWidget(self.searcher)
        self.containerLayout.addWidget(self.searcher)
        self.containerLayout.addWidget(self.player)
        self.container.setLayout(self.containerLayout)
        self.setCentralWidget(self.container)
        #self.setLayout(self.layout)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp2()
    w.show()
    sys.exit(app.exec())


