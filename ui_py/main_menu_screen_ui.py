from PyQt5 import QtCore, QtGui, QtWidgets


# UI составляющая игрового меню

class MainMenuUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setStyleSheet("QFrame \n"
                                      "{\n"
                                      "    background-color: rgb(49, 52, 117); \n"
                                      "    color: rbg(220, 220, 220); \n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.game_icon = QtWidgets.QLabel(self.main_frame)
        self.game_icon.setGeometry(QtCore.QRect(0, 0, 979, 221))
        self.game_icon.setText("")
        self.game_icon.setPixmap(QtGui.QPixmap("../images/background_images/main_menu_icon.png"))
        self.game_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.game_icon.setObjectName("game_icon")
        self.new_game_btn = QtWidgets.QPushButton(self.main_frame)
        self.new_game_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.new_game_btn.setGeometry(QtCore.QRect(220, 250, 541, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.new_game_btn.setFont(font)
        self.new_game_btn.setStyleSheet("QPushButton{ \n"
                                        "    border-radius: 10;\n"
                                        "    border: 4px solid rgb(238, 217, 94);\n"
                                        "    color: rgb(238, 214, 115);\n"
                                        "    background-color: rgb(41, 35, 117)\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{\n"
                                        "    color: black;\n"
                                        "    background-color: rgb(238, 214, 115)\n"
                                        "}")
        self.new_game_btn.setObjectName("new_game_btn")
        self.leaders_btn = QtWidgets.QPushButton(self.main_frame)
        self.leaders_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leaders_btn.setGeometry(QtCore.QRect(220, 370, 541, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.leaders_btn.setFont(font)
        self.leaders_btn.setStyleSheet("QPushButton{ \n"
                                       "    border-radius: 10;\n"
                                       "    border: 4px solid rgb(238, 217, 94);\n"
                                       "    color: rgb(238, 214, 115);\n"
                                       "    background-color: rgb(41, 35, 117)\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::pressed\n"
                                       "{\n"
                                       "    color: black;\n"
                                       "    background-color: rgb(238, 214, 115)\n"
                                       "}")
        self.leaders_btn.setObjectName("leaders_btn")
        self.credits_btn = QtWidgets.QPushButton(self.main_frame)
        self.credits_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.credits_btn.setGeometry(QtCore.QRect(220, 490, 541, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.credits_btn.setFont(font)
        self.credits_btn.setStyleSheet("QPushButton{ \n"
                                       "    border-radius: 10;\n"
                                       "    border: 4px solid rgb(238, 217, 94);\n"
                                       "    color: rgb(238, 214, 115);\n"
                                       "    background-color: rgb(41, 35, 117)\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::pressed\n"
                                       "{\n"
                                       "    color: black;\n"
                                       "    background-color: rgb(238, 214, 115)\n"
                                       "}")
        self.credits_btn.setObjectName("authors_btn")
        self.exit_btn = QtWidgets.QPushButton(self.main_frame)
        self.exit_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_btn.setGeometry(QtCore.QRect(220, 610, 541, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("QPushButton{ \n"
                                    "    border-radius: 10;\n"
                                    "    border: 4px solid rgb(238, 217, 94);\n"
                                    "    color: rgb(238, 214, 115);\n"
                                    "    background-color: rgb(41, 35, 117)\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::pressed\n"
                                    "{\n"
                                    "    color: black;\n"
                                    "    background-color: rgb(238, 214, 115)\n"
                                    "}")
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.new_game_btn.setText(_translate("MainWindow", "Начать Игру"))
        self.leaders_btn.setText(_translate("MainWindow", "Список Лидеров"))
        self.credits_btn.setText(_translate("MainWindow", "Благодарности"))
        self.exit_btn.setText(_translate("MainWindow", "Выйти"))
