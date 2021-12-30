from PyQt5 import QtCore, QtGui, QtWidgets


class GuessingScreenUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(11, 11, 1000, 640))
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
        self.main_heading.setGeometry(QtCore.QRect(0, 10, 981, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.main_heading.setFont(font)
        self.main_heading.setStyleSheet("color:rgb(238, 214, 115)")
        self.main_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.main_heading.setObjectName("main_heading")
        self.cur_lives_heading = QtWidgets.QLabel(self.main_frame)
        self.cur_lives_heading.setGeometry(QtCore.QRect(70, 80, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.cur_lives_heading.setFont(font)
        self.cur_lives_heading.setStyleSheet("color:rgb(238, 214, 115)")
        self.cur_lives_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.cur_lives_heading.setObjectName("cur_lives_heading")
        self.time_left_heading = QtWidgets.QLabel(self.main_frame)
        self.time_left_heading.setGeometry(QtCore.QRect(520, 80, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.time_left_heading.setFont(font)
        self.time_left_heading.setStyleSheet("color:rgb(238, 214, 115)")
        self.time_left_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.time_left_heading.setObjectName("time_left_heading")
        self.guessable_word = QtWidgets.QLabel(self.main_frame)
        self.guessable_word.setGeometry(QtCore.QRect(20, 150, 941, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.guessable_word.setFont(font)
        self.guessable_word.setStyleSheet("color:rgb(238, 214, 115)")
        self.guessable_word.setAlignment(QtCore.Qt.AlignCenter)
        self.guessable_word.setObjectName("guessable_word")
        self.buttons_frame = QtWidgets.QFrame(self.main_frame)
        self.buttons_frame.setGeometry(QtCore.QRect(160, 330, 691, 291))
        self.buttons_frame.setStyleSheet("QFrame \n"
                                         "{\n"
                                         "    background-color: rgb(52, 56, 138);\n"
                                         "    color: rbg(220, 220, 220); \n"
                                         "    border-radius: 20px;\n"
                                         "}")
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_frame.setObjectName("buttons_frame")
        self.pushButton = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    background-color: rgb(170, 170, 255);\n"
                                      "    color: black;\n"
                                      "    border: 1px solid black; \n"
                                      "    border-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed\n"
                                      "{ \n"
                                      "    background-color: white; \n"
                                      "    color: rgb(162, 162, 162);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::disabled\n"
                                      "{\n"
                                      "    background-color: white;\n"
                                      "    color: rgb(162, 162, 162)\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgb(170, 170, 255);\n"
                                        "    color: black;\n"
                                        "    border: 1px solid black; \n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{ \n"
                                        "    background-color: white; \n"
                                        "    color: rgb(162, 162, 162);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::disabled\n"
                                        "{\n"
                                        "    background-color: white;\n"
                                        "    color: rgb(162, 162, 162)\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttonGroup.addButton(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgb(170, 170, 255);\n"
                                        "    color: black;\n"
                                        "    border: 1px solid black; \n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{ \n"
                                        "    background-color: white; \n"
                                        "    color: rgb(162, 162, 162);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::disabled\n"
                                        "{\n"
                                        "    background-color: white;\n"
                                        "    color: rgb(162, 162, 162)\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.buttonGroup.addButton(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgb(170, 170, 255);\n"
                                        "    color: black;\n"
                                        "    border: 1px solid black; \n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{ \n"
                                        "    background-color: white; \n"
                                        "    color: rgb(162, 162, 162);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::disabled\n"
                                        "{\n"
                                        "    background-color: white;\n"
                                        "    color: rgb(162, 162, 162)\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.buttonGroup.addButton(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgb(170, 170, 255);\n"
                                        "    color: black;\n"
                                        "    border: 1px solid black; \n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{ \n"
                                        "    background-color: white; \n"
                                        "    color: rgb(162, 162, 162);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::disabled\n"
                                        "{\n"
                                        "    background-color: white;\n"
                                        "    color: rgb(162, 162, 162)\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.buttonGroup.addButton(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgb(170, 170, 255);\n"
                                        "    color: black;\n"
                                        "    border: 1px solid black; \n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{ \n"
                                        "    background-color: white; \n"
                                        "    color: rgb(162, 162, 162);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::disabled\n"
                                        "{\n"
                                        "    background-color: white;\n"
                                        "    color: rgb(162, 162, 162)\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.buttonGroup.addButton(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgb(170, 170, 255);\n"
                                        "    color: black;\n"
                                        "    border: 1px solid black; \n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{ \n"
                                        "    background-color: white; \n"
                                        "    color: rgb(162, 162, 162);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::disabled\n"
                                        "{\n"
                                        "    background-color: white;\n"
                                        "    color: rgb(162, 162, 162)\n"
                                        "}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.buttonGroup.addButton(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgb(170, 170, 255);\n"
                                        "    color: black;\n"
                                        "    border: 1px solid black; \n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{ \n"
                                        "    background-color: white; \n"
                                        "    color: rgb(162, 162, 162);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::disabled\n"
                                        "{\n"
                                        "    background-color: white;\n"
                                        "    color: rgb(162, 162, 162)\n"
                                        "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.buttonGroup.addButton(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "    background-color: rgb(170, 170, 255);\n"
                                        "    color: black;\n"
                                        "    border: 1px solid black; \n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed\n"
                                        "{ \n"
                                        "    background-color: white; \n"
                                        "    color: rgb(162, 162, 162);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::disabled\n"
                                        "{\n"
                                        "    background-color: white;\n"
                                        "    color: rgb(162, 162, 162)\n"
                                        "}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.buttonGroup.addButton(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setGeometry(QtCore.QRect(560, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.buttonGroup.addButton(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setGeometry(QtCore.QRect(620, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.buttonGroup.addButton(self.pushButton_11)
        self.pushButton_19 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_19.setEnabled(True)
        self.pushButton_19.setGeometry(QtCore.QRect(260, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.buttonGroup.addButton(self.pushButton_19)
        self.pushButton_16 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_16.setEnabled(True)
        self.pushButton_16.setGeometry(QtCore.QRect(320, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.buttonGroup.addButton(self.pushButton_16)
        self.pushButton_12 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setGeometry(QtCore.QRect(500, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.buttonGroup.addButton(self.pushButton_12)
        self.pushButton_14 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_14.setEnabled(True)
        self.pushButton_14.setGeometry(QtCore.QRect(200, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.buttonGroup.addButton(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.setGeometry(QtCore.QRect(140, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.buttonGroup.addButton(self.pushButton_13)
        self.pushButton_20 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_20.setEnabled(True)
        self.pushButton_20.setGeometry(QtCore.QRect(440, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.buttonGroup.addButton(self.pushButton_20)
        self.pushButton_22 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_22.setEnabled(True)
        self.pushButton_22.setGeometry(QtCore.QRect(80, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.buttonGroup.addButton(self.pushButton_22)
        self.pushButton_17 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_17.setEnabled(True)
        self.pushButton_17.setGeometry(QtCore.QRect(380, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.buttonGroup.addButton(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_18.setEnabled(True)
        self.pushButton_18.setGeometry(QtCore.QRect(20, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.buttonGroup.addButton(self.pushButton_18)
        self.pushButton_15 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_15.setEnabled(True)
        self.pushButton_15.setGeometry(QtCore.QRect(560, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.buttonGroup.addButton(self.pushButton_15)
        self.pushButton_31 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_31.setEnabled(True)
        self.pushButton_31.setGeometry(QtCore.QRect(290, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_31.setObjectName("pushButton_31")
        self.buttonGroup.addButton(self.pushButton_31)
        self.pushButton_26 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_26.setEnabled(True)
        self.pushButton_26.setGeometry(QtCore.QRect(410, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.buttonGroup.addButton(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_27.setEnabled(True)
        self.pushButton_27.setGeometry(QtCore.QRect(590, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.buttonGroup.addButton(self.pushButton_27)
        self.pushButton_21 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_21.setEnabled(True)
        self.pushButton_21.setGeometry(QtCore.QRect(170, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.buttonGroup.addButton(self.pushButton_21)
        self.pushButton_23 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_23.setEnabled(True)
        self.pushButton_23.setGeometry(QtCore.QRect(110, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.buttonGroup.addButton(self.pushButton_23)
        self.pushButton_28 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_28.setEnabled(True)
        self.pushButton_28.setGeometry(QtCore.QRect(470, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.buttonGroup.addButton(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_29.setEnabled(True)
        self.pushButton_29.setGeometry(QtCore.QRect(350, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_29.setObjectName("pushButton_29")
        self.buttonGroup.addButton(self.pushButton_29)
        self.pushButton_24 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_24.setEnabled(True)
        self.pushButton_24.setGeometry(QtCore.QRect(50, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.buttonGroup.addButton(self.pushButton_24)
        self.pushButton_30 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_30.setEnabled(True)
        self.pushButton_30.setGeometry(QtCore.QRect(530, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_30.setObjectName("pushButton_30")
        self.buttonGroup.addButton(self.pushButton_30)
        self.pushButton_25 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_25.setEnabled(True)
        self.pushButton_25.setGeometry(QtCore.QRect(230, 140, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.buttonGroup.addButton(self.pushButton_25)
        self.pushButton_32 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_32.setEnabled(True)
        self.pushButton_32.setGeometry(QtCore.QRect(620, 80, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_32.setObjectName("pushButton_32")
        self.buttonGroup.addButton(self.pushButton_32)
        self.pushButton_33 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_33.setEnabled(True)
        self.pushButton_33.setGeometry(QtCore.QRect(50, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_33.setObjectName("pushButton_33")
        self.buttonGroup.addButton(self.pushButton_33)
        self.pushButton_34 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_34.setEnabled(True)
        self.pushButton_34.setGeometry(QtCore.QRect(170, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_34.setObjectName("pushButton_34")
        self.buttonGroup.addButton(self.pushButton_34)
        self.pushButton_35 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_35.setEnabled(True)
        self.pushButton_35.setGeometry(QtCore.QRect(350, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_35.setObjectName("pushButton_35")
        self.buttonGroup.addButton(self.pushButton_35)
        self.pushButton_36 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_36.setEnabled(True)
        self.pushButton_36.setGeometry(QtCore.QRect(470, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_36.setObjectName("pushButton_36")
        self.buttonGroup.addButton(self.pushButton_36)
        self.pushButton_37 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_37.setEnabled(True)
        self.pushButton_37.setGeometry(QtCore.QRect(290, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_37.setObjectName("pushButton_37")
        self.buttonGroup.addButton(self.pushButton_37)
        self.pushButton_38 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_38.setEnabled(True)
        self.pushButton_38.setGeometry(QtCore.QRect(110, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_38.setObjectName("pushButton_38")
        self.buttonGroup.addButton(self.pushButton_38)
        self.pushButton_39 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_39.setEnabled(True)
        self.pushButton_39.setGeometry(QtCore.QRect(230, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_39.setObjectName("pushButton_39")
        self.buttonGroup.addButton(self.pushButton_39)
        self.pushButton_40 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_40.setEnabled(True)
        self.pushButton_40.setGeometry(QtCore.QRect(410, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_40.setObjectName("pushButton_40")
        self.buttonGroup.addButton(self.pushButton_40)
        self.pushButton_41 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_41.setEnabled(True)
        self.pushButton_41.setGeometry(QtCore.QRect(590, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_41.setObjectName("pushButton_41")
        self.buttonGroup.addButton(self.pushButton_41)
        self.pushButton_42 = QtWidgets.QPushButton(self.buttons_frame)
        self.pushButton_42.setEnabled(True)
        self.pushButton_42.setGeometry(QtCore.QRect(530, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: black;\n"
                                         "    border: 1px solid black; \n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed\n"
                                         "{ \n"
                                         "    background-color: white; \n"
                                         "    color: rgb(162, 162, 162);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::disabled\n"
                                         "{\n"
                                         "    background-color: white;\n"
                                         "    color: rgb(162, 162, 162)\n"
                                         "}")
        self.pushButton_42.setObjectName("pushButton_42")
        self.buttonGroup.addButton(self.pushButton_42)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_heading.setText(_translate("MainWindow", "Угадывайте Слово"))
        self.cur_lives_heading.setText(_translate("MainWindow", "Ошибок Позволено - 0"))
        self.time_left_heading.setText(_translate("MainWindow", "Времени Осталось - 60.00"))
        self.guessable_word.setText(_translate("MainWindow", "Р А З Г О В О Р \n"
                                                             "С Е Р Г Е Я   Д О В Л А Т О В А   С\n"
                                                             "Б Е Р Т Р А Н О М   Р А С С Е Л О М"))
        self.pushButton.setText(_translate("MainWindow", "Й"))
        self.pushButton_2.setText(_translate("MainWindow", "Ц"))
        self.pushButton_3.setText(_translate("MainWindow", "У"))
        self.pushButton_4.setText(_translate("MainWindow", "К"))
        self.pushButton_5.setText(_translate("MainWindow", "Е"))
        self.pushButton_6.setText(_translate("MainWindow", "Н"))
        self.pushButton_7.setText(_translate("MainWindow", "Г"))
        self.pushButton_8.setText(_translate("MainWindow", "Ш"))
        self.pushButton_9.setText(_translate("MainWindow", "Щ"))
        self.pushButton_10.setText(_translate("MainWindow", "З"))
        self.pushButton_11.setText(_translate("MainWindow", "Х"))
        self.pushButton_19.setText(_translate("MainWindow", "П"))
        self.pushButton_16.setText(_translate("MainWindow", "Р"))
        self.pushButton_12.setText(_translate("MainWindow", "Д"))
        self.pushButton_14.setText(_translate("MainWindow", "А"))
        self.pushButton_13.setText(_translate("MainWindow", "В"))
        self.pushButton_20.setText(_translate("MainWindow", "Л"))
        self.pushButton_22.setText(_translate("MainWindow", "Ы"))
        self.pushButton_17.setText(_translate("MainWindow", "О"))
        self.pushButton_18.setText(_translate("MainWindow", "Ф"))
        self.pushButton_15.setText(_translate("MainWindow", "Ж"))
        self.pushButton_31.setText(_translate("MainWindow", "И"))
        self.pushButton_26.setText(_translate("MainWindow", "Ь"))
        self.pushButton_27.setText(_translate("MainWindow", "Ъ"))
        self.pushButton_21.setText(_translate("MainWindow", "С"))
        self.pushButton_23.setText(_translate("MainWindow", "Ч"))
        self.pushButton_28.setText(_translate("MainWindow", "Б"))
        self.pushButton_29.setText(_translate("MainWindow", "Т"))
        self.pushButton_24.setText(_translate("MainWindow", "Я"))
        self.pushButton_30.setText(_translate("MainWindow", "Ю"))
        self.pushButton_25.setText(_translate("MainWindow", "М"))
        self.pushButton_32.setText(_translate("MainWindow", "Э"))
        self.pushButton_33.setText(_translate("MainWindow", "0"))
        self.pushButton_34.setText(_translate("MainWindow", "2"))
        self.pushButton_35.setText(_translate("MainWindow", "5"))
        self.pushButton_36.setText(_translate("MainWindow", "7"))
        self.pushButton_37.setText(_translate("MainWindow", "4"))
        self.pushButton_38.setText(_translate("MainWindow", "1"))
        self.pushButton_39.setText(_translate("MainWindow", "3"))
        self.pushButton_40.setText(_translate("MainWindow", "6"))
        self.pushButton_41.setText(_translate("MainWindow", "9"))
        self.pushButton_42.setText(_translate("MainWindow", "8"))
