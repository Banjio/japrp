import sys
#sys.path.append("../")
from PyQt5.QtWidgets import *
from japrp.audio_backends.audio_backend_vlc import VlcBackend
from japrp.audio_backends.audio_backend_pyqt5 import QtMediaPlayerWrapper

_BACKEND = "vlc"

class Player(QWidget):

    def __init__(self, value_dict=None, parent=None):
        super().__init__(parent=parent)
        self.layout = QGridLayout()
        if value_dict is None:
            value_dict = {}
        self._station_name = value_dict.get("name", "NO NamE")
        self._icon = value_dict.get("icon", "NO ICON")
        self.url = value_dict.get("url")
        self.station_name = QLabel(self._station_name)
        self.icon = QLabel(self._icon)
        self.playBtn = QPushButton("Play")
        self.stopBtn = QPushButton("Stop")
        self.playBtn.clicked.connect(self.start_playing)
        self.stopBtn.clicked.connect(self.stop_playing)
        if _BACKEND == "vlc":
            self.player = VlcBackend()
        else:
            self.player = QtMediaPlayerWrapper()

        self.layout.addWidget(self.station_name, 0, 0, 1, 3)
        self.layout.addWidget(self.icon, 1, 0, 1, 3)
        self.layout.addWidget(self.playBtn, 2, 0, 1, 1)
        self.layout.addWidget(self.stopBtn, 2, 1, 1, 1)
        self.setLayout(self.layout)

    def start_playing(self):
        #self.stream = subprocess.Popen(["python", "-m", "streamer_script.py"], stdout=sys.stdout)
        if self.url == "" or self.url is None:
            pass
        else:
            self.player.set_media(self.url, media_type='infer')
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


    def set_url(self, url):
        #URL = "http://bob.hoerradar.de/radiobob-hartesaite-mp3-hq?sABC=6020sp0s%230%23r731s0685son37qn82q119rrn30n0ss5%23zrqvncynlre&=&amsparams=playerid:mediaplayer;skey:1612774415"  # BBC
        #URL = "http://mp3-live.swr3.de/swr3_m.m3u"
        self.url = url





    def closeEvent(self, event):
       #quit_msg = "Are you sure you want to exit the program?"
       if self.player is not None:
           self.player.stop()



if __name__ == "__main__":
    URL = "http://bob.hoerradar.de/radiobob-hartesaite-mp3-hq?sABC=6020sp0s%230%23r731s0685son37qn82q119rrn30n0ss5%23zrqvncynlre&=&amsparams=playerid:mediaplayer;skey:1612774415"  # BBC
    app = QApplication(sys.argv)
    player = Player()
    player.set_url(URL)
    player.show()
    sys.exit(app.exec())