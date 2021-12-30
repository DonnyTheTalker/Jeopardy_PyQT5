# Импорт системных библиотек
import sys
import sqlite3

# Импорт PyQt5 компонент
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore

# Импорт UI компонент
from ui_py.loading_screen_ui import LoadingScreenUI

# Импорт классов
from source_py.main_menu_screen import MainMenuScreen
from source_py.audio_player import AudioPlayer

# Импорт сторонних функций
from source_py.frame_setup import setup_frame

MAIN_TIMER_DURATION = 125
STATUS_TIMER_DURATION = 2500


# Загрузочный экран - после работы открывает главное меню игры
# Является стартовым для работы приложения
class LoadingScreen(QMainWindow, LoadingScreenUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.audio_player = AudioPlayer()
        self.main_menu = MainMenuScreen(self.audio_player)

        # Переменные для QProgressBar
        self.cur_counter = 0

        self.initUI()

    def initUI(self):
        # Настройка параметров окна
        setup_frame(self, self.main_frame)

        # Проигрыватель для вступительной композиции
        filename = "../music/loading_screen.mp3"
        self.audio_player.load(filename)
        self.audio_player.set_volume(30)
        self.audio_player.play()

        # Таймер заполнения progress-bar'а загрузки
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(MAIN_TIMER_DURATION)
        self.update_progress()

        # Изменения 'текущего состояния' загрузочного статуса
        try:
            file = open("../texts/loading_statuses.txt", 'r', encoding='utf-8')
            self.statuses = file.readlines()
            self.cur_status = 0
            self.status_timer = QtCore.QTimer()
            self.status_timer.timeout.connect(self.update_loading_status)
            self.status_timer.start(STATUS_TIMER_DURATION)
            self.update_loading_status()
            file.close()

        except FileNotFoundError:
            self.loading_status.setText("<strong>Пытаемся</strong> найти файл со своими "
                                        "обязанностями")

    # Изменение текущего статуса загрузочного экрана
    def update_loading_status(self):
        if self.cur_status == len(self.statuses):
            self.status_timer.stop()
            return

        self.loading_status.setText(self.statuses[self.cur_status])
        self.cur_status += 1

    # Изменение шкалы в QProgressBar
    def update_progress(self):
        self.progressBar.setValue(self.cur_counter)

        if self.cur_counter > 100:
            self.timer.stop()
            self.main_menu.show()
            self.close()

        self.cur_counter += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoadingScreen()
    ex.show()
    sys.exit(app.exec_())
