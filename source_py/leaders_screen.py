import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from PyQt5 import QtCore
from PyQt5.QtGui import QColor

from PyQt5 import QtMultimedia

from ui_py.leaders_screen_ui import LeadersScreenUI

from source_py.frame_setup import setup_frame


# Меню лидеров
class LeadersScreen(QMainWindow, LeadersScreenUI):
    def __init__(self, prev_window):
        super().__init__()
        self.prev_window = prev_window
        self.setupUi(self)
        self.initUI()
        self.load_table()

    def initUI(self):
        # Настройка параметров окна
        setup_frame(self, self.main_frame)

        # Настраиваем функционал кнопок
        self.exit_btn.clicked.connect(self.close_window)

        # Сохраняем stylesheet нашей таблицы для того, чтобы
        # После загрузки таблицы применить его вновь -
        # Сохранив изменения стиля на все добавленные ячейки таблицы
        self.tableWidget_stylesheet = self.tableWidget.styleSheet()
        self.system_timer = QtCore.QTimer(self)
        self.system_timer.setSingleShot(True)
        self.system_timer.timeout.connect(self.change_table_stylesheet)
        self.system_timer.start(1)

    def load_table(self):
        con = sqlite3.connect("../Jeopardy.db")
        cur = con.cursor()

        # Загружаем данные об игроках из БД в таблицу
        player_stats = cur.execute(
            """SELECT * FROM Leaders ORDER BY experience, record""").fetchall()[::-1]
        self.tableWidget.setRowCount(len(player_stats))
        for i, row in enumerate(player_stats):
            for j in range(5):
                item = QTableWidgetItem(str(row[j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)

        con.close()

    def change_table_stylesheet(self):
        self.tableWidget.setStyleSheet(self.tableWidget_stylesheet)

    def close_window(self):
        self.prev_window.show()
        self.close()
