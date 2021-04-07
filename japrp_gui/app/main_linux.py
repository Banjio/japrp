#!/usr/bin/env python
import sys
import os
import pathlib
sys.path.append("../")
print(os.path.abspath(os.curdir))
from japrp.app.app import Japrp
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
app.setStyle("Fusion")
w = Japrp()
w.show()
sys.exit(app.exec())
