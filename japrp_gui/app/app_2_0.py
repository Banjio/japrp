import sys
import requests
import logging
from io import StringIO, BytesIO
from japrp_gui.app.main_window import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSlot, QTimer, QThreadPool, QRect
from PyQt5.QtGui import QPixmap
from japrp_gui.app_parts.qt_search import ClickableSearchResult
from japrp_core.parser import RadioBrowserSimple
from japrp_core.audio_backends.audio_backend_vlc import VlcBackend
from japrp_core.audio_backends.audio_backend_pyqt5 import QtMediaPlayerWrapper
from functools import partial
from japrp_gui.app.qt_worker import Worker

import qdarkstyle

_BACKEND = "vlc"
_SEARCH_LIMIT = 20
_SONG_UPDATE_TIMER = 25 * 1000
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
#https://github.com/baoboa/pyqt5/blob/master/examples/multimediawidgets/player.py how to make pyqt5 media playr work with playlist


class JaprpUi(object):

    def __init__(self, main_window):
        self.central_widget = QWidget(main_window)

class Japrp(QMainWindow):

    def __init__(self):
        super(Japrp, self).__init__()
        #self.setupUi(self)
        self.centralwidget = QWidget(self)
        self.initialize_ui(self.centralwidget)
        self.setCentralWidget(self.centralwidget)
        self.resize(1200, 900)
        print(self.size())
        #self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        # self.search_results = []
        # self.searcher = RadioBrowserSimple()
        # if _BACKEND == "vlc":
        #     self.player = VlcBackend()
        # else:
        #     self.player = QtMediaPlayerWrapper()
        # self.ui.searchbar.returnPressed.connect(self.search_radio)
        #
        # self.ui.play.clicked.connect(self.start_playing)
        # self.ui.stop.clicked.connect(self.stop_playing)
        #
        # self.ui.searchedContent.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.ui.searchedContent.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.ui.searchedContent.setWidgetResizable(True)
        #
        # self._station_icon_default = QPixmap("../../img/empty_icon.png")
        # self._station_name_default = ""
        # self.ui.sender_icon.setPixmap(self._station_icon_default)
        #
        # self.ui.sender_name.setText(self._station_name_default)
        #
        # self.ui.volumeSlider.setValue(self.player.get_volume())
        # self.ui.volumeSlider.valueChanged.connect(self.set_volume)
        #
        # self.player_is_active = False
        #
        # self.ui.song_title.setWordWrap(True)
        # self.timer = QTimer(self)
        # self.timer.setInterval(_SONG_UPDATE_TIMER)
        # self.timer.timeout.connect(self.get_song_name)
        # #self.timer.timeout.connect(self.set_song_name)
        # self.timer.start()
        #
        # self.threadpool = QThreadPool()

    
    # def setupUi(self, MainWindow):
    #     MainWindow.setObjectName("MainWindow")
    #     MainWindow.resize(800, 600)
    #     self.centralwidget = QWidget(MainWindow)
    #     sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(0)
    #     sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
    #     self.centralwidget.setSizePolicy(sizePolicy)
    #     self.centralwidget.setObjectName("centralwidget")
    #     self.verticalLayoutWidget = QWidget(self.centralwidget)
    #     self.verticalLayoutWidget.setGeometry(QRect(110, 40, 371, 451))
    #     self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
    #     self.searcherLayout = QVBoxLayout(self.verticalLayoutWidget)
    #     self.searcherLayout.setSizeConstraint(QLayout.SetNoConstraint)
    #     self.searcherLayout.setContentsMargins(0, 0, 0, 0)
    #     self.searcherLayout.setObjectName("searcherLayout")
    #     self.searchbar = QLineEdit(self.verticalLayoutWidget)
    #     sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(0)
    #     sizePolicy.setHeightForWidth(self.searchbar.sizePolicy().hasHeightForWidth())
    #     self.searchbar.setSizePolicy(sizePolicy)
    #     self.searchbar.setObjectName("searchbar")
    #     self.searcherLayout.addWidget(self.searchbar)
    #     self.searchedContent = QScrollArea(self.verticalLayoutWidget)
    #     self.searchedContent.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
    #     self.searchedContent.setWidgetResizable(True)
    #     self.searchedContent.setObjectName("searchedContent")
    #     self.scrollAreaWidgetContents = QWidget()
    #     self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 367, 414))
    #     sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    #     sizePolicy.setHorizontalStretch(2)
    #     sizePolicy.setVerticalStretch(2)
    #     sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
    #     self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
    #     self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
    #     self.searchedContent.setWidget(self.scrollAreaWidgetContents)
    #     self.searcherLayout.addWidget(self.searchedContent)
        # self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        # self.verticalLayoutWidget_3.setGeometry(QRect(510, 40, 201, 451))
        # self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        # self.playerLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        # self.playerLayout.setSizeConstraint(QLayout.SetNoConstraint)
        # self.playerLayout.setContentsMargins(0, 0, 0, 0)
        # self.playerLayout.setObjectName("playerLayout")
        # self.sender_icon = QLabel(self.verticalLayoutWidget_3)
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.sender_icon.sizePolicy().hasHeightForWidth())
        # self.sender_icon.setSizePolicy(sizePolicy)
        # self.sender_icon.setAlignment(Qt.AlignCenter)
        # self.sender_icon.setObjectName("sender_icon")
        # self.playerLayout.addWidget(self.sender_icon)
        # self.sender_name = QLabel(self.verticalLayoutWidget_3)
        # self.sender_name.setAlignment(Qt.AlignCenter)
        # self.sender_name.setObjectName("sender_name")
        # self.playerLayout.addWidget(self.sender_name)
        # spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.playerLayout.addItem(spacerItem)
        # self.song_title = QLabel(self.verticalLayoutWidget_3)
        # self.song_title.setAlignment(Qt.AlignCenter)
        # self.song_title.setObjectName("song_title")
        # self.playerLayout.addWidget(self.song_title)
        # self.volumeSlider = QSlider(self.verticalLayoutWidget_3)
        # self.volumeSlider.setOrientation(Qt.Horizontal)
        # self.volumeSlider.setObjectName("volumeSlider")
        # self.playerLayout.addWidget(self.volumeSlider)
        # self.playerButtons = QHBoxLayout()
        # self.playerButtons.setSizeConstraint(QLayout.SetNoConstraint)
        # self.playerButtons.setObjectName("playerButtons")
        # self.play = QPushButton(self.verticalLayoutWidget_3)
        # sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        # self.play.setSizePolicy(sizePolicy)
        # self.play.setObjectName("play")
        # self.playerButtons.addWidget(self.play)
        # self.stop = QPushButton(self.verticalLayoutWidget_3)
        # self.stop.setObjectName("stop")
        # self.playerButtons.addWidget(self.stop)
        # self.playerLayout.addLayout(self.playerButtons)
        # MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QMenuBar(MainWindow)
        # self.menubar.setGeometry(QRect(0, 0, 800, 25))
        # self.menubar.setObjectName("menubar")
        # self.menufile = QMenu(self.menubar)
        # self.menufile.setObjectName("menufile")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        # self.menubar.addAction(self.menufile.menuAction())

        #self.retranslateUi(MainWindow)
        #QMetaObject.connectSlotsByName(MainWindow)
    
    def initialize_ui(self, central_widget):
        self.global_layout = QHBoxLayout()
        self.searchbar_widget = self.initialize_searchbar(central_widget)
        self.global_layout.addWidget(self.searchbar_widget)
        self.player_widget = self.initialize_player_ui(central_widget)
        self.global_layout.addWidget(self.player_widget)

    @staticmethod
    def initialize_searchbar(central_widget):
        verticalLayoutWidget = QWidget(central_widget)
        verticalLayoutWidget.setGeometry(QRect(110, 40, 371, 451))
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        searcherLayout = QVBoxLayout()
        searcherLayout.setSizeConstraint(QLayout.SetNoConstraint)
        searcherLayout.setContentsMargins(0, 0, 0, 0)
        searcherLayout.setObjectName("searcherLayout")
        searchbar = QLineEdit(verticalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(searchbar.sizePolicy().hasHeightForWidth())
        searchbar.setSizePolicy(sizePolicy)
        searchbar.setObjectName("searchbar")
        searcherLayout.addWidget(searchbar)
        searchedContent = QScrollArea(verticalLayoutWidget)
        searchedContent.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        searchedContent.setWidgetResizable(True)
        searchedContent.setObjectName("searchedContent")
        scrollAreaWidgetContents = QWidget()
        scrollAreaWidgetContents.setGeometry(QRect(0, 0, 367, 414))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        searchedContent.setWidget(scrollAreaWidgetContents)
        searcherLayout.addWidget(searchedContent)
        return verticalLayoutWidget

    @staticmethod
    def initialize_player_ui(central_widget):
        verticalLayoutWidget_3 = QWidget(central_widget)
        verticalLayoutWidget_3.setGeometry(QRect(510, 40, 201, 451))
        verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        playerLayout = QVBoxLayout(verticalLayoutWidget_3)
        playerLayout.setSizeConstraint(QLayout.SetNoConstraint)
        playerLayout.setContentsMargins(0, 0, 0, 0)
        playerLayout.setObjectName("playerLayout")
        sender_icon = QLabel(verticalLayoutWidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sender_icon.sizePolicy().hasHeightForWidth())
        sender_icon.setSizePolicy(sizePolicy)
        sender_icon.setAlignment(Qt.AlignCenter)
        sender_icon.setObjectName("sender_icon")
        playerLayout.addWidget(sender_icon)
        sender_name = QLabel(verticalLayoutWidget_3)
        sender_name.setAlignment(Qt.AlignCenter)
        sender_name.setObjectName("sender_name")
        playerLayout.addWidget(sender_name)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        playerLayout.addItem(spacerItem)
        song_title = QLabel(verticalLayoutWidget_3)
        song_title.setAlignment(Qt.AlignCenter)
        song_title.setObjectName("song_title")
        playerLayout.addWidget(song_title)
        volumeSlider = QSlider(verticalLayoutWidget_3)
        volumeSlider.setOrientation(Qt.Horizontal)
        volumeSlider.setObjectName("volumeSlider")
        playerLayout.addWidget(volumeSlider)
        playerButtons = QHBoxLayout()
        playerButtons.setSizeConstraint(QLayout.SetNoConstraint)
        playerButtons.setObjectName("playerButtons")
        play = QPushButton(verticalLayoutWidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(play.sizePolicy().hasHeightForWidth())
        play.setSizePolicy(sizePolicy)
        play.setObjectName("play")
        playerButtons.addWidget(play)
        stop = QPushButton(verticalLayoutWidget_3)
        stop.setObjectName("stop")
        playerButtons.addWidget(stop)
        playerLayout.addLayout(playerButtons)
        return verticalLayoutWidget_3

    def initialize_player(self):
        pass



    def get_song_name(self):
        logger.debug("Workers active %s" %self.threadpool.activeThreadCount())
        if self.threadpool.maxThreadCount() == self.threadpool.activeThreadCount():
            self.threadpool.waitForDone(5 * 1000)
        if self.player_is_active:
            player_url = self.player.get_url()
            worker = Worker(self.player.get_meta_data_icy, player_url)
            worker.signals.result.connect(self.set_song_name)
            self.threadpool.start(worker)

    def set_song_name(self, s):
        logger.debug("Update song title!")
        if self.player_is_active:
            self.ui.song_title.setText(s)


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
   #app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    w = Japrp()
    w.show()
    sys.exit(app.exec())
