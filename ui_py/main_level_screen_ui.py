from PyQt5 import QtCore, QtGui, QtWidgets


class MainLevelUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(11, 11, 1191, 778))
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
        self.enemy2_frame.setGeometry(QtCore.QRect(980, 500, 191, 201))
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
        self.player_frame.setGeometry(QtCore.QRect(770, 500, 191, 201))
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
        self.enemy1_frame.setGeometry(QtCore.QRect(560, 500, 191, 201))
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
        self.enemy1_name.setGeometry(QtCore.QRect(560, 450, 191, 41))
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
        self.enemy2_name.setGeometry(QtCore.QRect(980, 450, 191, 41))
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
        self.player_name.setGeometry(QtCore.QRect(770, 450, 191, 41))
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
        self.question_panel = QtWidgets.QWidget(self.main_frame)
        self.question_panel.setGeometry(QtCore.QRect(540, 39, 620, 390))
        self.question_panel.setStyleSheet("QWidget\n"
                                          "{\n"
                                          "    background-color: rgb(0, 0, 127);\n"
                                          "    color: rbg(220, 220, 220);\n"
                                          "    border: 1px solid black;\n"
                                          "}")
        self.question_panel.setObjectName("question_panel")
        self.theme1 = QtWidgets.QLabel(self.question_panel)
        self.theme1.setGeometry(QtCore.QRect(0, 0, 170, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.theme1.setFont(font)
        self.theme1.setStyleSheet("border-radius: 0px;\n"
                                  "color: rgb(238, 214, 115)")
        self.theme1.setAlignment(QtCore.Qt.AlignCenter)
        self.theme1.setObjectName("theme1")
        self.theme2 = QtWidgets.QLabel(self.question_panel)
        self.theme2.setGeometry(QtCore.QRect(0, 78, 170, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.theme2.setFont(font)
        self.theme2.setStyleSheet("border-radius: 0px;\n"
                                  "color: rgb(238, 214, 115)")
        self.theme2.setAlignment(QtCore.Qt.AlignCenter)
        self.theme2.setObjectName("theme2")
        self.theme3 = QtWidgets.QLabel(self.question_panel)
        self.theme3.setGeometry(QtCore.QRect(0, 156, 170, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.theme3.setFont(font)
        self.theme3.setStyleSheet("border-radius: 0px;\n"
                                  "color: rgb(238, 214, 115)")
        self.theme3.setAlignment(QtCore.Qt.AlignCenter)
        self.theme3.setObjectName("theme3")
        self.theme4 = QtWidgets.QLabel(self.question_panel)
        self.theme4.setGeometry(QtCore.QRect(0, 234, 170, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.theme4.setFont(font)
        self.theme4.setStyleSheet("border-radius: 0px;\n"
                                  "color: rgb(238, 214, 115)")
        self.theme4.setAlignment(QtCore.Qt.AlignCenter)
        self.theme4.setObjectName("theme4")
        self.theme5 = QtWidgets.QLabel(self.question_panel)
        self.theme5.setGeometry(QtCore.QRect(0, 312, 170, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.theme5.setFont(font)
        self.theme5.setStyleSheet("border-radius: 0px;\n"
                                  "color: rgb(238, 214, 115)")
        self.theme5.setAlignment(QtCore.Qt.AlignCenter)
        self.theme5.setObjectName("theme5")
        self.btn_00 = QtWidgets.QPushButton(self.question_panel)
        self.btn_00.setGeometry(QtCore.QRect(170, 0, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_00.setFont(font)
        self.btn_00.setMouseTracking(True)
        self.btn_00.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_00.setObjectName("btn_00")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_00)
        self.btn_01 = QtWidgets.QPushButton(self.question_panel)
        self.btn_01.setGeometry(QtCore.QRect(260, 0, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_01.setFont(font)
        self.btn_01.setMouseTracking(True)
        self.btn_01.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_01.setObjectName("btn_01")
        self.buttonGroup.addButton(self.btn_01)
        self.btn_02 = QtWidgets.QPushButton(self.question_panel)
        self.btn_02.setEnabled(True)
        self.btn_02.setGeometry(QtCore.QRect(350, 0, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_02.setFont(font)
        self.btn_02.setMouseTracking(True)
        self.btn_02.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_02.setObjectName("btn_02")
        self.buttonGroup.addButton(self.btn_02)
        self.btn_03 = QtWidgets.QPushButton(self.question_panel)
        self.btn_03.setGeometry(QtCore.QRect(440, 0, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_03.setFont(font)
        self.btn_03.setMouseTracking(True)
        self.btn_03.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_03.setObjectName("btn_03")
        self.buttonGroup.addButton(self.btn_03)
        self.btn_04 = QtWidgets.QPushButton(self.question_panel)
        self.btn_04.setGeometry(QtCore.QRect(530, 0, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_04.setFont(font)
        self.btn_04.setMouseTracking(True)
        self.btn_04.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_04.setObjectName("btn_04")
        self.buttonGroup.addButton(self.btn_04)
        self.btn_11 = QtWidgets.QPushButton(self.question_panel)
        self.btn_11.setGeometry(QtCore.QRect(260, 78, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_11.setFont(font)
        self.btn_11.setMouseTracking(True)
        self.btn_11.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_11.setObjectName("btn_11")
        self.buttonGroup.addButton(self.btn_11)
        self.btn_13 = QtWidgets.QPushButton(self.question_panel)
        self.btn_13.setGeometry(QtCore.QRect(440, 78, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_13.setFont(font)
        self.btn_13.setMouseTracking(True)
        self.btn_13.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_13.setObjectName("btn_13")
        self.buttonGroup.addButton(self.btn_13)
        self.btn_14 = QtWidgets.QPushButton(self.question_panel)
        self.btn_14.setGeometry(QtCore.QRect(530, 78, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_14.setFont(font)
        self.btn_14.setMouseTracking(True)
        self.btn_14.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_14.setObjectName("btn_14")
        self.buttonGroup.addButton(self.btn_14)
        self.btn_12 = QtWidgets.QPushButton(self.question_panel)
        self.btn_12.setGeometry(QtCore.QRect(350, 78, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_12.setFont(font)
        self.btn_12.setMouseTracking(True)
        self.btn_12.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_12.setObjectName("btn_12")
        self.buttonGroup.addButton(self.btn_12)
        self.btn_10 = QtWidgets.QPushButton(self.question_panel)
        self.btn_10.setGeometry(QtCore.QRect(170, 78, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_10.setFont(font)
        self.btn_10.setMouseTracking(True)
        self.btn_10.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_10.setObjectName("btn_10")
        self.buttonGroup.addButton(self.btn_10)
        self.btn_21 = QtWidgets.QPushButton(self.question_panel)
        self.btn_21.setGeometry(QtCore.QRect(260, 156, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_21.setFont(font)
        self.btn_21.setMouseTracking(True)
        self.btn_21.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_21.setObjectName("btn_21")
        self.buttonGroup.addButton(self.btn_21)
        self.btn_24 = QtWidgets.QPushButton(self.question_panel)
        self.btn_24.setGeometry(QtCore.QRect(530, 156, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_24.setFont(font)
        self.btn_24.setMouseTracking(True)
        self.btn_24.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_24.setObjectName("btn_24")
        self.buttonGroup.addButton(self.btn_24)
        self.btn_20 = QtWidgets.QPushButton(self.question_panel)
        self.btn_20.setGeometry(QtCore.QRect(170, 156, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_20.setFont(font)
        self.btn_20.setMouseTracking(True)
        self.btn_20.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_20.setObjectName("btn_20")
        self.buttonGroup.addButton(self.btn_20)
        self.btn_22 = QtWidgets.QPushButton(self.question_panel)
        self.btn_22.setGeometry(QtCore.QRect(350, 156, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_22.setFont(font)
        self.btn_22.setMouseTracking(True)
        self.btn_22.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_22.setObjectName("btn_22")
        self.buttonGroup.addButton(self.btn_22)
        self.btn_23 = QtWidgets.QPushButton(self.question_panel)
        self.btn_23.setGeometry(QtCore.QRect(440, 156, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_23.setFont(font)
        self.btn_23.setMouseTracking(True)
        self.btn_23.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_23.setObjectName("btn_23")
        self.buttonGroup.addButton(self.btn_23)
        self.btn_31 = QtWidgets.QPushButton(self.question_panel)
        self.btn_31.setGeometry(QtCore.QRect(260, 234, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_31.setFont(font)
        self.btn_31.setMouseTracking(True)
        self.btn_31.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_31.setObjectName("btn_31")
        self.buttonGroup.addButton(self.btn_31)
        self.btn_33 = QtWidgets.QPushButton(self.question_panel)
        self.btn_33.setGeometry(QtCore.QRect(440, 234, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_33.setFont(font)
        self.btn_33.setMouseTracking(True)
        self.btn_33.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_33.setObjectName("btn_33")
        self.buttonGroup.addButton(self.btn_33)
        self.btn_34 = QtWidgets.QPushButton(self.question_panel)
        self.btn_34.setGeometry(QtCore.QRect(530, 234, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_34.setFont(font)
        self.btn_34.setMouseTracking(True)
        self.btn_34.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_34.setObjectName("btn_34")
        self.buttonGroup.addButton(self.btn_34)
        self.btn_32 = QtWidgets.QPushButton(self.question_panel)
        self.btn_32.setGeometry(QtCore.QRect(350, 234, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_32.setFont(font)
        self.btn_32.setMouseTracking(True)
        self.btn_32.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_32.setObjectName("btn_32")
        self.buttonGroup.addButton(self.btn_32)
        self.btn_30 = QtWidgets.QPushButton(self.question_panel)
        self.btn_30.setGeometry(QtCore.QRect(170, 234, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_30.setFont(font)
        self.btn_30.setMouseTracking(True)
        self.btn_30.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_30.setObjectName("btn_30")
        self.buttonGroup.addButton(self.btn_30)
        self.btn_41 = QtWidgets.QPushButton(self.question_panel)
        self.btn_41.setGeometry(QtCore.QRect(260, 312, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_41.setFont(font)
        self.btn_41.setMouseTracking(True)
        self.btn_41.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_41.setObjectName("btn_41")
        self.buttonGroup.addButton(self.btn_41)
        self.btn_43 = QtWidgets.QPushButton(self.question_panel)
        self.btn_43.setGeometry(QtCore.QRect(440, 312, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_43.setFont(font)
        self.btn_43.setMouseTracking(True)
        self.btn_43.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_43.setObjectName("btn_43")
        self.buttonGroup.addButton(self.btn_43)
        self.btn_44 = QtWidgets.QPushButton(self.question_panel)
        self.btn_44.setGeometry(QtCore.QRect(530, 312, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_44.setFont(font)
        self.btn_44.setMouseTracking(True)
        self.btn_44.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_44.setObjectName("btn_44")
        self.buttonGroup.addButton(self.btn_44)
        self.btn_42 = QtWidgets.QPushButton(self.question_panel)
        self.btn_42.setGeometry(QtCore.QRect(350, 312, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_42.setFont(font)
        self.btn_42.setMouseTracking(True)
        self.btn_42.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_42.setObjectName("btn_42")
        self.buttonGroup.addButton(self.btn_42)
        self.btn_40 = QtWidgets.QPushButton(self.question_panel)
        self.btn_40.setGeometry(QtCore.QRect(170, 312, 90, 78))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_40.setFont(font)
        self.btn_40.setMouseTracking(True)
        self.btn_40.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "\n"
                                  "    border-radius: 0px; \n"
                                  "    color: rgb(238, 214, 115);\n"
                                  "    background-color: rgb(0, 0, 127)\n"
                                  "}\n"
                                  "                                        \n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "    color: black;\n"
                                  "    background-color: rgb(238, 214, 115);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "    border: 2px solid rgb(238, 214, 115);\n"
                                  "}")
        self.btn_40.setObjectName("btn_40")
        self.buttonGroup.addButton(self.btn_40)
        self.question_frame = QtWidgets.QFrame(self.main_frame)
        self.question_frame.setGeometry(QtCore.QRect(20, 20, 501, 511))
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
        font.setPointSize(20)
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
        self.question_ans_btn = QtWidgets.QPushButton(self.question_frame)
        self.question_ans_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.question_ans_btn.setGeometry(QtCore.QRect(170, 450, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.question_ans_btn.setFont(font)
        self.question_ans_btn.setStyleSheet("QPushButton\n"
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
        self.question_ans_btn.setObjectName("question_ans_btn")
        self.answer_frame = QtWidgets.QFrame(self.main_frame)
        self.answer_frame.setGeometry(QtCore.QRect(20, 560, 501, 201))
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
        self.answer_label.setGeometry(QtCore.QRect(20, 10, 461, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.answer_label.setFont(font)
        self.answer_label.setStyleSheet("border: 0px;\n"
                                        "color: rgb(238, 214, 115)")
        self.answer_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.answer_label.setObjectName("answer_label")
        self.game_status = QtWidgets.QLabel(self.answer_frame)
        self.game_status.setGeometry(QtCore.QRect(20, 150, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.game_status.setFont(font)
        self.game_status.setStyleSheet("border: 0px;\n"
                                       "color: rgb(238, 214, 115)")
        self.game_status.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.game_status.setObjectName("game_status")
        self.enemy1_points = QtWidgets.QLCDNumber(self.main_frame)
        self.enemy1_points.setGeometry(QtCore.QRect(560, 710, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.enemy1_points.setFont(font)
        self.enemy1_points.setDigitCount(1)
        self.enemy1_points.setObjectName("enemy1_points")
        self.player_points = QtWidgets.QLCDNumber(self.main_frame)
        self.player_points.setGeometry(QtCore.QRect(770, 710, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.player_points.setFont(font)
        self.player_points.setDigitCount(1)
        self.player_points.setObjectName("player_points")
        self.enemy2_points = QtWidgets.QLCDNumber(self.main_frame)
        self.enemy2_points.setGeometry(QtCore.QRect(980, 710, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.enemy2_points.setFont(font)
        self.enemy2_points.setDigitCount(1)
        self.enemy2_points.setObjectName("enemy2_points")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit_btn.setText(_translate("MainWindow", "X"))
        self.enemy1_name.setText(_translate("MainWindow", "Противник № 1"))
        self.enemy2_name.setText(_translate("MainWindow", "Противник № 2"))
        self.player_name.setText(_translate("MainWindow", "Игрок № 1"))
        self.theme1.setText(_translate("MainWindow", "Философская"))
        self.theme2.setText(_translate("MainWindow", "Колян Рефн"))
        self.theme3.setText(_translate("MainWindow", "Историческая"))
        self.theme4.setText(_translate("MainWindow", "Животнолюбивая"))
        self.theme5.setText(_translate("MainWindow", "Музыкальная"))
        self.btn_00.setText(_translate("MainWindow", "100"))
        self.btn_01.setText(_translate("MainWindow", "200"))
        self.btn_02.setText(_translate("MainWindow", "300"))
        self.btn_03.setText(_translate("MainWindow", "400"))
        self.btn_04.setText(_translate("MainWindow", "500"))
        self.btn_11.setText(_translate("MainWindow", "200"))
        self.btn_13.setText(_translate("MainWindow", "400"))
        self.btn_14.setText(_translate("MainWindow", "500"))
        self.btn_12.setText(_translate("MainWindow", "300"))
        self.btn_10.setText(_translate("MainWindow", "100"))
        self.btn_21.setText(_translate("MainWindow", "200"))
        self.btn_24.setText(_translate("MainWindow", "500"))
        self.btn_20.setText(_translate("MainWindow", "100"))
        self.btn_22.setText(_translate("MainWindow", "300"))
        self.btn_23.setText(_translate("MainWindow", "400"))
        self.btn_31.setText(_translate("MainWindow", "200"))
        self.btn_33.setText(_translate("MainWindow", "400"))
        self.btn_34.setText(_translate("MainWindow", "500"))
        self.btn_32.setText(_translate("MainWindow", "300"))
        self.btn_30.setText(_translate("MainWindow", "100"))
        self.btn_41.setText(_translate("MainWindow", "200"))
        self.btn_43.setText(_translate("MainWindow", "400"))
        self.btn_44.setText(_translate("MainWindow", "500"))
        self.btn_42.setText(_translate("MainWindow", "300"))
