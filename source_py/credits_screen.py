import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore
from PyQt5.QtGui import QColor

from PyQt5 import QtMultimedia

from ui_py.credits_screen_ui import CreditsScreenUI

from source_py.frame_setup import setup_frame


# Меню благодарностей
class CreditsScreen(QMainWindow, CreditsScreenUI):
    def __init__(self, prev_window):
        super().__init__()
        self.prev_window = prev_window
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Настройка параметров окна
        setup_frame(self, self.main_frame)

        # Настраиваем функционал кнопок
        self.exit_btn.clicked.connect(self.close_window)

        # Загружаем список благодарностей в виджет QTextEdit
        try:
            file = open("../texts/credits.txt", 'r', encoding='utf-8')
            cur_credits = file.readlines()
            for credit in cur_credits:
                self.textEdit.append('\t\t' + credit.rstrip('\n'))
            file.close()
        except FileNotFoundError:
            self.textEdit.setText("Благодарность всем живым существам\n"
                                  "В особенности ответственным за этот раздел игры")

    def close_window(self):
        self.prev_window.show()
        self.close()
