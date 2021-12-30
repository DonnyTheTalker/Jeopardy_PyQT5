from PyQt5 import QtCore, QtGui, QtWidgets


class PlayerSetupUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(11, 11, 978, 748))
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
        self.player_background = QtWidgets.QFrame(self.main_frame)
        self.player_background.setGeometry(QtCore.QRect(720, 300, 191, 201))
        self.player_background.setStyleSheet("background-color: rgb(238, 214, 115);  ")
        self.player_background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.player_background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_background.setObjectName("player_background")
        self.player_image = QtWidgets.QLabel(self.player_background)
        self.player_image.setGeometry(QtCore.QRect(9, 9, 171, 181))
        self.player_image.setText("")
        self.player_image.setPixmap(
            QtGui.QPixmap("../game_members_images/player_images/player0.PNG"))
        self.player_image.setAlignment(QtCore.Qt.AlignCenter)
        self.player_image.setObjectName("player_image")
        self.next_stage_btn = QtWidgets.QPushButton(self.main_frame)
        self.next_stage_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.next_stage_btn.setGeometry(QtCore.QRect(250, 575, 481, 141))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(53)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.next_stage_btn.setFont(font)
        self.next_stage_btn.setStyleSheet("QPushButton\n"
                                          "{\n"
                                          "    border-radius: 10;\n"
                                          "    border: 4px solid rgb(238, 217, 94);\n"
                                          "    color: rgb(238, 214, 115);\n"
                                          "    background-color: rgb(41, 35, 117);\n"
                                          "}\n"
                                          "                                        \n"
                                          "QPushButton::pressed\n"
                                          "{\n"
                                          "    color: black;\n"
                                          "    background-color: rgb(238, 214, 115);\n"
                                          "}")
        self.next_stage_btn.setObjectName("next_stage_btn")
        self.player_name_label = QtWidgets.QLabel(self.main_frame)
        self.player_name_label.setGeometry(QtCore.QRect(40, 100, 331, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.player_name_label.setFont(font)
        self.player_name_label.setStyleSheet("color:rgb(238, 214, 115)")
        self.player_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_name_label.setObjectName("player_name_label")
        self.player_name_line_edit = QtWidgets.QLineEdit(self.main_frame)
        self.player_name_line_edit.setGeometry(QtCore.QRect(390, 110, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(27)
        self.player_name_line_edit.setFont(font)
        self.player_name_line_edit.setStyleSheet("border-radius: 10;\n"
                                                 "border: 4px solid rgb(238, 217, 94);\n"
                                                 "color: rgb(238, 214, 115)"
                                                 ";background-color: rgb(41, 35, 117);")
        self.player_name_line_edit.setMaxLength(10)
        self.player_name_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.player_name_line_edit.setObjectName("player_name_line_edit")
        self.change_background_color_btn = QtWidgets.QPushButton(self.main_frame)
        self.change_background_color_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.change_background_color_btn.setGeometry(QtCore.QRect(100, 430, 531, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.change_background_color_btn.setFont(font)
        self.change_background_color_btn.setStyleSheet("QPushButton\n"
                                                       "{\n"
                                                       "    border-radius: 10;\n"
                                                       "    border: 4px solid rgb(238, 217, 94);\n"
                                                       "    color: rgb(238, 214, 115);\n"
                                                       "    background-color: rgb(41, 35, 117);\n"
                                                       "}\n"
                                                       "                                        \n"
                                                       "QPushButton::pressed\n"
                                                       "{\n"
                                                       "    color: black;\n"
                                                       "    background-color: rgb(238, 214, 115);\n"
                                                       "}")
        self.change_background_color_btn.setObjectName("change_background_color_btn")
        self.player_image_hint = QtWidgets.QLabel(self.main_frame)
        self.player_image_hint.setGeometry(QtCore.QRect(50, 220, 641, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.player_image_hint.setFont(font)
        self.player_image_hint.setStyleSheet("color:rgb(238, 214, 115)")
        self.player_image_hint.setAlignment(QtCore.Qt.AlignCenter)
        self.player_image_hint.setObjectName("player_image_hint")
        self.change_image_right_btn = QtWidgets.QPushButton(self.main_frame)
        self.change_image_right_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.change_image_right_btn.setGeometry(QtCore.QRect(369, 320, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(55)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.change_image_right_btn.setFont(font)
        self.change_image_right_btn.setStyleSheet("QPushButton\n"
                                                  "{\n"
                                                  "    border-radius: 10;\n"
                                                  "    border: 4px solid rgb(238, 217, 94);\n"
                                                  "    color: rgb(238, 214, 115);\n"
                                                  "    background-color: rgb(41, 35, 117);\n"
                                                  "}\n"
                                                  "                                        \n"
                                                  "QPushButton::pressed\n"
                                                  "{\n"
                                                  "    color: black;\n"
                                                  "    background-color: rgb(238, 214, 115);\n"
                                                  "}")
        self.change_image_right_btn.setIconSize(QtCore.QSize(20, 20))
        self.change_image_right_btn.setObjectName("change_image_right_btn")
        self.change_image_left_btn = QtWidgets.QPushButton(self.main_frame)
        self.change_image_left_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.change_image_left_btn.setGeometry(QtCore.QRect(100, 320, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(55)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.change_image_left_btn.setFont(font)
        self.change_image_left_btn.setStyleSheet("QPushButton\n"
                                                 "{\n"
                                                 "    border-radius: 10;\n"
                                                 "    border: 4px solid rgb(238, 217, 94);\n"
                                                 "    color: rgb(238, 214, 115);\n"
                                                 "    background-color: rgb(41, 35, 117);\n"
                                                 "}\n"
                                                 "                                        \n"
                                                 "QPushButton::pressed\n"
                                                 "{\n"
                                                 "    color: black;\n"
                                                 "    background-color: rgb(238, 214, 115);\n"
                                                 "}")
        self.change_image_left_btn.setObjectName("change_image_left_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_heading.setText(_translate("MainWindow", "Последние Шаги"))
        self.next_stage_btn.setText(_translate("MainWindow", "К Игре"))
        self.player_name_label.setText(_translate("MainWindow", "Имя игрока"))
        self.player_name_line_edit.setText(_translate("MainWindow", "Игрок"))
        self.change_background_color_btn.setText(
            _translate("MainWindow", "Изменить цвет иконки игрока"))
        self.player_image_hint.setText(_translate("MainWindow", "Изменить изображение игрока"))
        self.change_image_right_btn.setText(_translate("MainWindow", "☛"))
        self.change_image_left_btn.setText(_translate("MainWindow", "☚"))
