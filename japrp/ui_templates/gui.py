# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 40, 371, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.searcherLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.searcherLayout.setContentsMargins(0, 0, 0, 0)
        self.searcherLayout.setObjectName("searcherLayout")
        self.searchbar = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.searchbar.setObjectName("searchbar")
        self.searcherLayout.addWidget(self.searchbar)
        self.searchedContent = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.searchedContent.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.searchedContent.setWidgetResizable(True)
        self.searchedContent.setObjectName("searchedContent")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 367, 414))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.searchedContent.setWidget(self.scrollAreaWidgetContents)
        self.searcherLayout.addWidget(self.searchedContent)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(510, 40, 201, 451))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.playerLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.playerLayout.setContentsMargins(0, 0, 0, 0)
        self.playerLayout.setObjectName("playerLayout")
        self.sender_icon = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sender_icon.sizePolicy().hasHeightForWidth())
        self.sender_icon.setSizePolicy(sizePolicy)
        self.sender_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.sender_icon.setObjectName("sender_icon")
        self.playerLayout.addWidget(self.sender_icon)
        self.sender_name = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.sender_name.setAlignment(QtCore.Qt.AlignCenter)
        self.sender_name.setObjectName("sender_name")
        self.playerLayout.addWidget(self.sender_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.playerLayout.addItem(spacerItem)
        self.song_title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.song_title.setAlignment(QtCore.Qt.AlignCenter)
        self.song_title.setObjectName("song_title")
        self.playerLayout.addWidget(self.song_title)
        self.volumeSlider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.playerLayout.addWidget(self.volumeSlider)
        self.playerButtons = QtWidgets.QHBoxLayout()
        self.playerButtons.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.playerButtons.setObjectName("playerButtons")
        self.play = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.play.setObjectName("play")
        self.playerButtons.addWidget(self.play)
        self.stop = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.stop.setObjectName("stop")
        self.playerButtons.addWidget(self.stop)
        self.playerLayout.addLayout(self.playerButtons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sender_icon.setText(_translate("MainWindow", "TextLabel"))
        self.sender_name.setText(_translate("MainWindow", "TextLabel"))
        self.song_title.setText(_translate("MainWindow", "TextLabel"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.menufile.setTitle(_translate("MainWindow", "Settings"))
