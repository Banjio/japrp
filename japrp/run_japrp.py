from PyQt5.QtWidgets import QDialog, QApplication
import subprocess
from japrb_gui import *
from japrp.streamer import UrlStreamer
import sys


class MyApp(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_playing)
        self.stream = None

    def start_playing(self):
        self.stream = subprocess.Popen(["python", "-m", "streamer_script.py"], stdout=sys.stdout)



    def closeEvent(self, event):
        #quit_msg = "Are you sure you want to exit the program?"
        self.stream.terminate()
        del self.stream
        #reply = QtGui.QMessageBox.question(self, 'Message',
        #                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        #if reply == QtGui.QMessageBox.Yes:
        #    event.accept()
        #else:
        #    event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())


