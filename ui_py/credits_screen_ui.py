from PyQt5 import QtCore, QtGui, QtWidgets


# UI-состовляющаяя экрана благодарностей


class CreditsScreenUI(object):
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
        self.main_credit = QtWidgets.QLabel(self.main_frame)
        self.main_credit.setGeometry(QtCore.QRect(0, 0, 981, 141))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.main_credit.setFont(font)
        self.main_credit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.main_credit.setStyleSheet("color:rgb(238, 214, 115);")
        self.main_credit.setAlignment(QtCore.Qt.AlignCenter)
        self.main_credit.setObjectName("main_credit")
        self.textEdit = QtWidgets.QTextEdit(self.main_frame)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(15, 200, 951, 471))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-radius: 10;\n"
                                    "border: 4px solid rgb(238, 217, 94);\n"
                                    "color: rgb(255, 255, 0);\n"
                                    "background-color:rgb(0, 0, 127); ")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setReadOnly(True)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.exit_btn = QtWidgets.QPushButton(self.main_frame)
        self.exit_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_btn.setGeometry(QtCore.QRect(370, 685, 240, 81))
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
        self.mid_credit = QtWidgets.QLabel(self.main_frame)
        self.mid_credit.setGeometry(QtCore.QRect(0, 130, 971, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.mid_credit.setFont(font)
        self.mid_credit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.mid_credit.setStyleSheet("color:rgb(238, 214, 115);")
        self.mid_credit.setAlignment(QtCore.Qt.AlignCenter)
        self.mid_credit.setObjectName("mid_credit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_credit.setText(_translate("MainWindow", "БЛАГОДАРНОСТИ"))
        self.exit_btn.setText(_translate("MainWindow", "Выйти"))
        self.mid_credit.setText(_translate("MainWindow", "Глава Команды - Егоров Максим"))
