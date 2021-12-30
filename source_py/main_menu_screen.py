# Импорт системных библиотек
import sys

# Импорт PyQt5 компонент
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from PyQt5 import QtCore
from PyQt5 import QtMultimedia
from PyQt5.QtGui import QColor

# Импорт UI компонент
from ui_py.main_menu_screen_ui import MainMenuUI

# Импорт классов
from source_py.credits_screen import CreditsScreen
from source_py.leaders_screen import LeadersScreen
from source_py.game_manager import GameManager
from source_py.game_setup_screen import GameSetupScreen

# Импорт сторонних функций
from source_py.frame_setup import setup_frame


# Главное меню игры
class MainMenuScreen(QMainWindow, MainMenuUI):
    def __init__(self, audio_player):
        super().__init__()

        self.audio_player = audio_player
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Настройка параметров окна
        setup_frame(self, self.main_frame)

        # Настраиваем функционал кнопок
        self.exit_btn.clicked.connect(self.close_window)
        self.credits_btn.clicked.connect(self.show_credits)
        self.new_game_btn.clicked.connect(self.start_game)
        self.leaders_btn.clicked.connect(self.show_leaders)

    def close_window(self):
        self.close()

    # Переход к онку благодарностей
    def show_credits(self):
        self.credits = CreditsScreen(self)
        self.credits.show()
        self.hide()

    # Переход к окну со списком лидеров
    # Осуществляется с задержкой для того
    # Чтобы гарантировать успешную загрузку базы данных
    # До доступа игрока к окну
    def show_leaders(self):
        self.leaders_screen = LeadersScreen(self)

        def open_leaders():
            self.leaders_screen.show()
            self.hide()

        # Создание таймера для открытия окна
        system_timer = QtCore.QTimer(self)
        system_timer.setSingleShot(True)
        system_timer.timeout.connect(open_leaders)
        system_timer.start(1)

    # Переход к окну настройки параметров новой игры
    def start_game(self):
        self.game_manager = GameManager()
        self.game_setup = GameSetupScreen(self, self.audio_player, self.game_manager)
        self.game_setup.show()
        self.hide()
