from PyQt5 import QtCore, QtGui, QtWidgets


# UI составляющая экрана выбора сложности


class GameSetupUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(11, 11, 978, 778))
        self.main_frame.setStyleSheet("QFrame \n"
                                      "{\n"
                                      "    background-color: rgb(49, 52, 117); \n"
                                      "    color: rbg(220, 220, 220); \n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.main_heading = QtWidgets.QLabel(self.main_frame)
        self.main_heading.setGeometry(QtCore.QRect(210, 5, 571, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.main_heading.setFont(font)
        self.main_heading.setStyleSheet("color:rgb(238, 214, 115)")
        self.main_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.main_heading.setObjectName("main_heading")
        self.easy_btn = QtWidgets.QRadioButton(self.main_frame)
        self.easy_btn.setGeometry(QtCore.QRect(180, 175, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.easy_btn.setFont(font)
        self.easy_btn.setStyleSheet("QRadioButton \n"
                                    "{\n"
                                    "    color:rgb(238, 214, 115);    \n"
                                    "}\n"
                                    "\n"
                                    "QRadioButton::indicator {\n"
                                    "    width:                  10px;\n"
                                    "    height:                 10px;\n"
                                    "    border-radius:          7px;\n"
                                    "}\n"
                                    "\n"
                                    "QRadioButton::indicator:checked {\n"
                                    "    background-color:   rgb(238, 214, 115); \n"
                                    "    border:                 2px solid white;\n"
                                    "}\n"
                                    "\n"
                                    "QRadioButton::indicator:unchecked {\n"
                                    "    background-color:       black;\n"
                                    "    border:                 2px solid white;\n"
                                    "}")
        self.easy_btn.setChecked(True)
        self.easy_btn.setObjectName("easy_btn")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.easy_btn)
        self.difficulty_heading = QtWidgets.QLabel(self.main_frame)
        self.difficulty_heading.setGeometry(QtCore.QRect(200, 110, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.difficulty_heading.setFont(font)
        self.difficulty_heading.setStyleSheet("color:rgb(238, 214, 115)")
        self.difficulty_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.difficulty_heading.setObjectName("difficulty_heading")
        self.medium_btn = QtWidgets.QRadioButton(self.main_frame)
        self.medium_btn.setGeometry(QtCore.QRect(410, 175, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.medium_btn.setFont(font)
        self.medium_btn.setStyleSheet("QRadioButton \n"
                                      "{\n"
                                      "    color:rgb(238, 214, 115);    \n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::indicator {\n"
                                      "    width:                  10px;\n"
                                      "    height:                 10px;\n"
                                      "    border-radius:          7px;\n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::indicator:checked {\n"
                                      "    background-color:   rgb(238, 214, 115); \n"
                                      "    border:                 2px solid white;\n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::indicator:unchecked {\n"
                                      "    background-color:       black;\n"
                                      "    border:                 2px solid white;\n"
                                      "}")
        self.medium_btn.setChecked(False)
        self.medium_btn.setObjectName("medium_btn")
        self.buttonGroup.addButton(self.medium_btn)
        self.hard_btn = QtWidgets.QRadioButton(self.main_frame)
        self.hard_btn.setGeometry(QtCore.QRect(670, 175, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.hard_btn.setFont(font)
        self.hard_btn.setStyleSheet("QRadioButton \n"
                                    "{\n"
                                    "    color:rgb(238, 214, 115);    \n"
                                    "}\n"
                                    "\n"
                                    "QRadioButton::indicator {\n"
                                    "    width:                  10px;\n"
                                    "    height:                 10px;\n"
                                    "    border-radius:          7px;\n"
                                    "}\n"
                                    "\n"
                                    "QRadioButton::indicator:checked {\n"
                                    "    background-color:   rgb(238, 214, 115); \n"
                                    "    border:                 2px solid white;\n"
                                    "}\n"
                                    "\n"
                                    "QRadioButton::indicator:unchecked {\n"
                                    "    background-color:       black;\n"
                                    "    border:                 2px solid white;\n"
                                    "}")
        self.hard_btn.setChecked(False)
        self.hard_btn.setObjectName("hard_btn")
        self.buttonGroup.addButton(self.hard_btn)
        self.difficulty_hint_main = QtWidgets.QLabel(self.main_frame)
        self.difficulty_hint_main.setGeometry(QtCore.QRect(0, 235, 981, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.difficulty_hint_main.setFont(font)
        self.difficulty_hint_main.setStyleSheet("color:rgb(238, 214, 115)")
        self.difficulty_hint_main.setAlignment(QtCore.Qt.AlignCenter)
        self.difficulty_hint_main.setObjectName("difficulty_hint_main")
        self.enemy1_frame = QtWidgets.QFrame(self.main_frame)
        self.enemy1_frame.setGeometry(QtCore.QRect(200, 380, 191, 201))
        self.enemy1_frame.setStyleSheet("QFrame \n"
                                        "{\n"
                                        "    background-color: rgb(238, 214, 115); \n"
                                        "    color: rbg(220, 220, 220); \n"
                                        "}")
        self.enemy1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.enemy1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.enemy1_frame.setObjectName("enemy1_frame")
        self.enemy1_label = QtWidgets.QLabel(self.enemy1_frame)
        self.enemy1_label.setGeometry(QtCore.QRect(10, 10, 171, 181))
        self.enemy1_label.setText("")
        self.enemy1_label.setPixmap(
            QtGui.QPixmap("../images/game_members_images/enemy_images/easy_enemy1.PNG"))
        self.enemy1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enemy1_label.setObjectName("enemy1_label")
        self.enemy2_frame = QtWidgets.QFrame(self.main_frame)
        self.enemy2_frame.setGeometry(QtCore.QRect(580, 380, 191, 201))
        self.enemy2_frame.setStyleSheet("QFrame \n"
                                        "{\n"
                                        "    background-color: rgb(238, 214, 115); \n"
                                        "    color: rbg(220, 220, 220); \n"
                                        "}")
        self.enemy2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.enemy2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.enemy2_frame.setObjectName("enemy2_frame")
        self.enemy2_label = QtWidgets.QLabel(self.enemy2_frame)
        self.enemy2_label.setGeometry(QtCore.QRect(10, 10, 171, 181))
        self.enemy2_label.setText("")
        self.enemy2_label.setPixmap(
            QtGui.QPixmap("../images/game_members_images/enemy_images/easy_enemy2.PNG"))
        self.enemy2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enemy2_label.setObjectName("enemy2_label")
        self.enemy_hint_main = QtWidgets.QLabel(self.main_frame)
        self.enemy_hint_main.setGeometry(QtCore.QRect(0, 310, 981, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enemy_hint_main.setFont(font)
        self.enemy_hint_main.setStyleSheet("color:rgb(238, 214, 115)")
        self.enemy_hint_main.setAlignment(QtCore.Qt.AlignCenter)
        self.enemy_hint_main.setObjectName("enemy_hint_main")
        self.difficulty_hint_extra = QtWidgets.QLabel(self.main_frame)
        self.difficulty_hint_extra.setGeometry(QtCore.QRect(0, 580, 981, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.difficulty_hint_extra.setFont(font)
        self.difficulty_hint_extra.setStyleSheet("color:rgb(238, 214, 115)")
        self.difficulty_hint_extra.setAlignment(QtCore.Qt.AlignCenter)
        self.difficulty_hint_extra.setObjectName("difficulty_hint_extra")
        self.next_stage_btn = QtWidgets.QPushButton(self.main_frame)
        self.next_stage_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.next_stage_btn.setGeometry(QtCore.QRect(340, 690, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.next_stage_btn.setFont(font)
        self.next_stage_btn.setStyleSheet("QPushButton{ \n"
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
        self.next_stage_btn.setObjectName("next_stage_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_heading.setText(_translate("MainWindow", "Начинаем Игру"))
        self.easy_btn.setText(_translate("MainWindow", "Низкий"))
        self.difficulty_heading.setText(_translate("MainWindow", "Выберите уровень сложности"))
        self.medium_btn.setText(_translate("MainWindow", "Средний"))
        self.hard_btn.setText(_translate("MainWindow", "Высокий"))
        self.difficulty_hint_main.setText(
            _translate("MainWindow", "Уровень сложности для новичков"))
        self.enemy_hint_main.setText(_translate("MainWindow", "С вами играют непризнанные мудрецы"))
        self.difficulty_hint_extra.setText(
            _translate("MainWindow", "Вы можете ошибиться до 5-и раз при вводе ответа\n"
                                     "И до 3-х, если ответ - число"))
        self.next_stage_btn.setText(_translate("MainWindow", "Далее"))
