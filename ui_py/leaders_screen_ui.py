from PyQt5 import QtCore, QtGui, QtWidgets


# UI составляющая экрана-списка лидеров


class LeadersScreenUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(11, 11, 1051, 778))
        self.main_frame.setStyleSheet("QFrame \n"
                                      "{\n"
                                      "    background-color: rgb(49, 52, 117); \n"
                                      "    color: rbg(220, 220, 220); \n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.main_label = QtWidgets.QLabel(self.main_frame)
        self.main_label.setGeometry(QtCore.QRect(10, 10, 1021, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.main_label.setFont(font)
        self.main_label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.main_label.setStyleSheet("color:rgb(238, 214, 115);")
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.exit_btn = QtWidgets.QPushButton(self.main_frame)
        self.exit_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_btn.setGeometry(QtCore.QRect(379, 680, 321, 81))
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
                                    "      border-radius: 10;\n"
                                    "      border: 4px solid rgb(238, 217, 94);\n"
                                    "      color: rgb(238, 214, 115);\n"
                                    "      background-color: rgb(41, 35, 117)\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::pressed\n"
                                    "{\n"
                                    "    color: black;\n"
                                    "    background-color: rgb(238, 214, 115)\n"
                                    "}")
        self.exit_btn.setObjectName("exit_btn")
        self.tableWidget = QtWidgets.QTableWidget(self.main_frame)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(20, 130, 1021, 531))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(" QWidget {\n"
                                       "    background-color: rgb(40, 35, 117);\n"
                                       "    color: #fffff8;\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "    background-color: rgb(58, 53, 117);\n"
                                       "    padding: 4px;\n"
                                       "    border: 1px solid #fffff8;\n"
                                       "    font-size: 14pt;\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget {\n"
                                       "    gridline-color: #fffff8;\n"
                                       "    border: 3px solid rgb(34, 31, 104);\n"
                                       "    border-radius: 0px;\n"
                                       "    font-size: 12pt;\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget QTableCornerButton::section {\n"
                                       "    background-color: rgb(58, 53, 117);\n"
                                       "    border: 1px solid #fffff8;\n"
                                       "} \n"
                                       "\n"
                                       " QScrollBar::add-page:vertical, "
                                       "QScrollBar::sub-page:vertical {\n"
                                       "     background: rgb(66, 75, 141);\n"
                                       " } \n"
                                       "\n"
                                       "QScrollBar::add-page:horizontal, "
                                       "QScrollBar::sub-page:horizontal {\n"
                                       "     background: rgb(66, 75, 141);\n"
                                       " }\n"
                                       " ")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(46)
        self.tableWidget.verticalHeader().setDefaultSectionSize(39)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label.setText(_translate("MainWindow", "Список Лидеров"))
        self.exit_btn.setText(_translate("MainWindow", "Выйти"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Игрок"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Рекорд"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Опыт"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Верных ответов"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ошибок сделано"))
