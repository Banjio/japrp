from PyQt5.QtWidgets import QApplication, QLabel
import time
app = QApplication([])

label = QLabel("Hello World")
label.show()
time.sleep(5)
app.exit(1)