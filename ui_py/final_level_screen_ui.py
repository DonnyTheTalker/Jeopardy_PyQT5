from PyQt5 import QtCore, QtGui, QtWidgets


class FinalLevelUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(11, 11, 1191, 801))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.main_frame.setFont(font)
        self.main_frame.setStyleSheet("QFrame \n"
                                      "{\n"
                                      "    background-color: rgb(49, 52, 117); \n"
                                      "    color: rbg(220, 220, 220); \n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.exit_btn = QtWidgets.QPushButton(self.main_frame)
        self.exit_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_btn.setGeometry(QtCore.QRect(1160, 10, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "    color: black;\n"
                                    "    background-color: red;\n"
                                    "    border-color: black;\n"
                                    "    border-radius: 10px;\n"
                                    "}")
        self.exit_btn.setObjectName("exit_btn")
        self.enemy2_frame = QtWidgets.QFrame(self.main_frame)
        self.enemy2_frame.setGeometry(QtCore.QRect(980, 530, 191, 201))
        self.enemy2_frame.setStyleSheet("background-color: rgb(238, 214, 115);  ")
        self.enemy2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.enemy2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.enemy2_frame.setObjectName("enemy2_frame")
        self.enemy2_image = QtWidgets.QLabel(self.enemy2_frame)
        self.enemy2_image.setGeometry(QtCore.QRect(9, 9, 171, 181))
        self.enemy2_image.setText("")
        self.enemy2_image.setPixmap(QtGui.QPixmap("game_members_images/default_player.PNG"))
        self.enemy2_image.setAlignment(QtCore.Qt.AlignCenter)
        self.enemy2_image.setObjectName("enemy2_image")
        self.player_frame = QtWidgets.QFrame(self.main_frame)
        self.player_frame.setGeometry(QtCore.QRect(770, 530, 191, 201))
        self.player_frame.setStyleSheet("background-color: rgb(238, 214, 115);  ")
        self.player_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.player_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_frame.setObjectName("player_frame")
        self.player_image = QtWidgets.QLabel(self.player_frame)
        self.player_image.setGeometry(QtCore.QRect(9, 9, 171, 181))
        self.player_image.setText("")
        self.player_image.setPixmap(QtGui.QPixmap("game_members_images/default_player.PNG"))
        self.player_image.setAlignment(QtCore.Qt.AlignCenter)
        self.player_image.setObjectName("player_image")
        self.enemy1_frame = QtWidgets.QFrame(self.main_frame)
        self.enemy1_frame.setGeometry(QtCore.QRect(560, 530, 191, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enemy1_frame.setFont(font)
        self.enemy1_frame.setStyleSheet("background-color: rgb(238, 214, 115);  ")
        self.enemy1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.enemy1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.enemy1_frame.setObjectName("enemy1_frame")
        self.enemy1_image = QtWidgets.QLabel(self.enemy1_frame)
        self.enemy1_image.setGeometry(QtCore.QRect(9, 9, 171, 181))
        self.enemy1_image.setText("")
        self.enemy1_image.setPixmap(QtGui.QPixmap("game_members_images/default_player.PNG"))
        self.enemy1_image.setAlignment(QtCore.Qt.AlignCenter)
        self.enemy1_image.setObjectName("enemy1_image")
        self.enemy1_name = QtWidgets.QLabel(self.main_frame)
        self.enemy1_name.setGeometry(QtCore.QRect(560, 480, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.enemy1_name.setFont(font)
        self.enemy1_name.setStyleSheet("color: rgb(238, 214, 115)")
        self.enemy1_name.setLineWidth(1)
        self.enemy1_name.setAlignment(QtCore.Qt.AlignCenter)
        self.enemy1_name.setObjectName("enemy1_name")
        self.enemy2_name = QtWidgets.QLabel(self.main_frame)
        self.enemy2_name.setGeometry(QtCore.QRect(980, 480, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.enemy2_name.setFont(font)
        self.enemy2_name.setStyleSheet("color: rgb(238, 214, 115)")
        self.enemy2_name.setLineWidth(1)
        self.enemy2_name.setAlignment(QtCore.Qt.AlignCenter)
        self.enemy2_name.setObjectName("enemy2_name")
        self.player_name = QtWidgets.QLabel(self.main_frame)
        self.player_name.setGeometry(QtCore.QRect(770, 480, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.player_name.setFont(font)
        self.player_name.setStyleSheet("color: rgb(238, 214, 115)")
        self.player_name.setLineWidth(1)
        self.player_name.setAlignment(QtCore.Qt.AlignCenter)
        self.player_name.setObjectName("player_name")
        self.bet_panel = QtWidgets.QWidget(self.main_frame)
        self.bet_panel.setGeometry(QtCore.QRect(20, 520, 501, 261))
        self.bet_panel.setStyleSheet("QWidget\n"
                                     "{\n"
                                     "    background-color: rgb(0, 0, 127);\n"
                                     "    color: rbg(220, 220, 220);\n"
                                     "    border: 1px solid rgb(238, 214, 115);\n"
                                     "    border-radius: 10px;\n"
                                     "}")
        self.bet_panel.setObjectName("bet_panel")
        self.bet_clarification = QtWidgets.QLabel(self.bet_panel)
        self.bet_clarification.setGeometry(QtCore.QRect(10, 10, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bet_clarification.setFont(font)
        self.bet_clarification.setStyleSheet("border: 0px;\n"
                                             "color: rgb(238, 214, 115)")
        self.bet_clarification.setTextFormat(QtCore.Qt.AutoText)
        self.bet_clarification.setAlignment(QtCore.Qt.AlignCenter)
        self.bet_clarification.setObjectName("bet_clarification")
        self.game_start_btn = QtWidgets.QPushButton(self.bet_panel)
        self.game_start_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.game_start_btn.setGeometry(QtCore.QRect(170, 210, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.game_start_btn.setFont(font)
        self.game_start_btn.setStyleSheet("QPushButton\n"
                                          "{\n"
                                          "    border-radius: 10;\n"
                                          "    border: 2px solid rgb(238, 217, 94);\n"
                                          "    color: rgb(238, 214, 115);\n"
                                          "    background-color: rgb(41, 35, 117);\n"
                                          "}\n"
                                          "                                        \n"
                                          "QPushButton::pressed\n"
                                          "{\n"
                                          "    color: black;\n"
                                          "    background-color: rgb(238, 214, 115);\n"
                                          "}")
        self.game_start_btn.setObjectName("game_start_btn")
        self.bet_slider = QtWidgets.QSlider(self.bet_panel)
        self.bet_slider.setGeometry(QtCore.QRect(10, 150, 481, 31))
        self.bet_slider.setStyleSheet("QSlider\n"
                                      "{\n"
                                      "    border: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::groove:horizontal {\n"
                                      "    border: 1px solid rgb(238, 214, 115);\n"
                                      "    border-radius: 7px;\n"
                                      "    height: 16px;\n"
                                      "    color: rgb(238, 214, 115);\n"
                                      "    background: rgb(20, 24, 109);\n"
                                      "    margin: 2px 0;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::handle:horizontal {\n"
                                      "    background:  rgb(238, 214, 115);\n"
                                      "    border: 1px solid #5c5c5c;\n"
                                      "    width: 25px;\n"
                                      "    margin: -2px 0; \n"
                                      "    border-radius: 3px;\n"
                                      "}\n"
                                      "")
        self.bet_slider.setMinimum(0)
        self.bet_slider.setSingleStep(10)
        self.bet_slider.setProperty("value", 99)
        self.bet_slider.setSliderPosition(99)
        self.bet_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bet_slider.setObjectName("bet_slider")
        self.bet_label = QtWidgets.QLabel(self.bet_panel)
        self.bet_label.setGeometry(QtCore.QRect(10, 70, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.bet_label.setFont(font)
        self.bet_label.setStyleSheet("border: 0px;\n"
                                     "color: rgb(238, 214, 115)")
        self.bet_label.setTextFormat(QtCore.Qt.AutoText)
        self.bet_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bet_label.setObjectName("bet_label")
        self.question_frame = QtWidgets.QFrame(self.main_frame)
        self.question_frame.setGeometry(QtCore.QRect(20, 20, 501, 471))
        self.question_frame.setStyleSheet("QFrame \n"
                                          "{\n"
                                          "    background-color: rgb(0, 0, 127);\n"
                                          "    color: rbg(220, 220, 220); \n"
                                          "    border-radius: 20px;\n"
                                          "    border: 2px solid rgb(238, 214, 115);\n"
                                          "}")
        self.question_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.question_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.question_frame.setObjectName("question_frame")
        self.question_clarification = QtWidgets.QLabel(self.question_frame)
        self.question_clarification.setGeometry(QtCore.QRect(20, 10, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_clarification.setFont(font)
        self.question_clarification.setStyleSheet("border: 0px;\n"
                                                  "color: rgb(238, 214, 115)")
        self.question_clarification.setTextFormat(QtCore.Qt.AutoText)
        self.question_clarification.setAlignment(QtCore.Qt.AlignCenter)
        self.question_clarification.setObjectName("question_clarification")
        self.main_question_label = QtWidgets.QLabel(self.question_frame)
        self.main_question_label.setGeometry(QtCore.QRect(20, 80, 461, 291))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.main_question_label.setFont(font)
        self.main_question_label.setStyleSheet("border: 0px;\n"
                                               "color: rgb(238, 214, 115)")
        self.main_question_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_question_label.setObjectName("main_question_label")
        self.question_timer = QtWidgets.QLabel(self.question_frame)
        self.question_timer.setEnabled(True)
        self.question_timer.setGeometry(QtCore.QRect(20, 390, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.question_timer.setFont(font)
        self.question_timer.setStyleSheet("border: 0px;\n"
                                          "color: rgb(238, 214, 115)")
        self.question_timer.setText("")
        self.question_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.question_timer.setObjectName("question_timer")
        self.enemy1_points = QtWidgets.QLCDNumber(self.main_frame)
        self.enemy1_points.setGeometry(QtCore.QRect(560, 740, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.enemy1_points.setFont(font)
        self.enemy1_points.setDigitCount(1)
        self.enemy1_points.setObjectName("enemy1_points")
        self.player_points = QtWidgets.QLCDNumber(self.main_frame)
        self.player_points.setGeometry(QtCore.QRect(770, 740, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.player_points.setFont(font)
        self.player_points.setDigitCount(1)
        self.player_points.setObjectName("player_points")
        self.enemy2_points = QtWidgets.QLCDNumber(self.main_frame)
        self.enemy2_points.setGeometry(QtCore.QRect(980, 740, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.enemy2_points.setFont(font)
        self.enemy2_points.setDigitCount(1)
        self.enemy2_points.setObjectName("enemy2_points")
        self.theme_label = QtWidgets.QLabel(self.main_frame)
        self.theme_label.setGeometry(QtCore.QRect(540, 30, 621, 251))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.theme_label.setFont(font)
        self.theme_label.setStyleSheet("border: 0px;\n"
                                       "color: rgb(238, 214, 115)")
        self.theme_label.setTextFormat(QtCore.Qt.AutoText)
        self.theme_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.theme_label.setObjectName("theme_label")
        self.answer_frame = QtWidgets.QFrame(self.main_frame)
        self.answer_frame.setGeometry(QtCore.QRect(540, 290, 631, 161))
        self.answer_frame.setStyleSheet("QFrame \n"
                                        "{\n"
                                        "    background-color: rgb(0, 0, 127);\n"
                                        "    color: rbg(220, 220, 220); \n"
                                        "    border-radius: 20px;\n"
                                        "    border: 2px solid rgb(238, 214, 115);\n"
                                        "}")
        self.answer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.answer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.answer_frame.setObjectName("answer_frame")
        self.answer_label = QtWidgets.QLabel(self.answer_frame)
        self.answer_label.setGeometry(QtCore.QRect(10, 10, 611, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.answer_label.setFont(font)
        self.answer_label.setStyleSheet("border: 0px;\n"
                                        "color: rgb(238, 214, 115)")
        self.answer_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.answer_label.setObjectName("answer_label")
        self.game_status = QtWidgets.QLabel(self.answer_frame)
        self.game_status.setGeometry(QtCore.QRect(10, 110, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.game_status.setFont(font)
        self.game_status.setStyleSheet("border: 0px;\n"
                                       "color: rgb(238, 214, 115)")
        self.game_status.setText("")
        self.game_status.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.game_status.setObjectName("game_status")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit_btn.setText(_translate("MainWindow", "X"))
        self.enemy1_name.setText(_translate("MainWindow", "Противник № 1"))
        self.enemy2_name.setText(_translate("MainWindow", "Противник № 2"))
        self.player_name.setText(_translate("MainWindow", "ФФФФФФФФФФ"))
        self.bet_clarification.setText(_translate("MainWindow", "Делайте ставку"))
        self.game_start_btn.setText(_translate("MainWindow", "Играть"))
        self.bet_label.setText(_translate("MainWindow", "100"))
        self.question_clarification.setText(_translate("MainWindow", "Приятной игры"))
        self.main_question_label.setText(_translate("MainWindow", "Финальный Раунд"))
        self.theme_label.setText(_translate("MainWindow", "Тема финального раунда:\n"
                                                          "Киберспорт\n"
                                                          "Киберспорт\n"
                                                          "Киберспорт"))
        self.answer_label.setText(_translate("MainWindow", "Делайте ставку"))
