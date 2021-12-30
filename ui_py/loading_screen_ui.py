from PyQt5 import QtCore, QtGui, QtWidgets


# UI составляющая экрана загрузки


class LoadingScreenUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(10, 0, 788, 580))
        self.main_frame.setStyleSheet("QFrame \n"
                                      "{\n"
                                      "    background-color: rgb(49, 52, 117); \n"
                                      "    color: rbg(220, 220, 220); \n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.game_icon_label = QtWidgets.QLabel(self.main_frame)
        self.game_icon_label.setGeometry(QtCore.QRect(155, 80, 471, 261))
        self.game_icon_label.setText("")
        self.game_icon_label.setPixmap(
            QtGui.QPixmap("../images/background_images/game_icon.PNG"))
        self.game_icon_label.setObjectName("game_icon_label")
        self.loading_status = QtWidgets.QLabel(self.main_frame)
        self.loading_status.setGeometry(QtCore.QRect(0, 340, 791, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.loading_status.setFont(font)
        self.loading_status.setStyleSheet("color: rgb(238, 214, 115)")
        self.loading_status.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_status.setObjectName("loading_status")
        self.progressBar = QtWidgets.QProgressBar(self.main_frame)
        self.progressBar.setGeometry(QtCore.QRect(9, 420, 771, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar \n"
                                       "{\n"
                                       "    background-color: rgba(69, 74, 166, 240);\n"
                                       "    color:rgb(238, 214, 116);\n"
                                       "    border-style: none;\n"
                                       "    border-radius: 10px;\n"
                                       "    text-align: center;\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk\n"
                                       "{\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: qlineargradient(spread:pad, "
                                       "x1:0, y1:0.511, x2:0.995025, y2:0.54, stop:0.0547264 "
                                       "rgba(255, 94, 234, 255), stop:1 rgba(170, 0, 255, 255));\n"
                                       "}")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.loading_label = QtWidgets.QLabel(self.main_frame)
        self.loading_label.setGeometry(QtCore.QRect(0, 450, 791, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.loading_label.setFont(font)
        self.loading_label.setStyleSheet("color: rgb(238, 214, 115)")
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_label.setObjectName("loading_label")
        self.copyright_label = QtWidgets.QLabel(self.main_frame)
        self.copyright_label.setGeometry(QtCore.QRect(470, 530, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.copyright_label.setFont(font)
        self.copyright_label.setStyleSheet("color: rgb(238, 214, 115)")
        self.copyright_label.setAlignment(QtCore.Qt.AlignCenter)
        self.copyright_label.setObjectName("copyright_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loading_status.setText(_translate("MainWindow",
                                               "<html><head/><body><p><span style=\" "
                                               "font-weight:600;\">Загрузка</span> Баз Данных"
                                               "</p></body></html>"))
        self.loading_label.setText(_translate("MainWindow", "Загрузка..."))
        self.copyright_label.setText(
            _translate("MainWindow", "© Посвящаю созданную этим проектом заслугу\n"
                                     "благу всех живых существ"))
