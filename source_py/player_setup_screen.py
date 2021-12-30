# Импорт системных библиотек
import sys

# Импорт PyQt5 компонент
from PyQt5.QtWidgets import QColorDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QColor

# Импорт классов
from source_py.main_level_screen import MainLevelScreen

# Импорт UI компонент
from ui_py.player_setup_screen_ui import PlayerSetupUI

# Импорт сторонних функций
from source_py.frame_setup import setup_frame

# Список запрещеннх для выбора имён персонажа
FORBIDDEN_NAMES = ['Хозяин', 'Приспешник', 'Подданый']
IMAGE_COUNT = 30


# Меню настройки персонажа
class PlayerSetupScreen(QMainWindow, PlayerSetupUI):
    def __init__(self, main_menu, audio_player, game_manager):
        super().__init__()

        self.audio_player = audio_player
        self.game_manager = game_manager
        self.main_menu = main_menu

        # Текущие выбранные изображение и цвет иконки
        self.cur_color = "rgb(238, 214, 115)"
        self.cur_pixmap = QPixmap("../images/game_members_images/player_images/player0.png")
        self.i_image = 0
        self.n_images = IMAGE_COUNT

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Настройки параметров окна
        setup_frame(self, self.main_frame)

        # Настройка кнопок переключения изображения игрока
        self.change_image_left_btn.clicked.connect(lambda: self.change_image(-1))
        self.change_image_right_btn.clicked.connect(lambda: self.change_image(1))
        self.change_image(0)

        # Настройка кнопки изменения цвета иконки игрока
        self.change_background_color_btn.clicked.connect(self.change_background_color)

        # Настройка перехода к игре
        self.next_stage_btn.clicked.connect(self.start_game)

    def change_image(self, shift):
        # Округление с учётом переполнения в любую из сторон
        self.i_image = ((self.i_image + shift) % self.n_images + self.n_images) % self.n_images
        self.cur_pixmap = QPixmap(f"../images/"
                                  f"game_members_images/player_images/player{self.i_image}.png")
        self.player_image.setPixmap(self.cur_pixmap)

    # Выбор и смена цвета иконки персонажа
    def change_background_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.cur_color = color.name()
            self.player_background.setStyleSheet(f"background-color: {self.cur_color}")

    # Функция окончания настройки параметров игрока и запуска основного уровня игры
    def start_game(self):
        # Получаем имя игрока из LineEdit - если не введено ничего
        # Используем стандартное имя "Игрок"
        player_name = self.player_name_line_edit.text()
        if not player_name:
            player_name = "Игрок"

        if player_name in FORBIDDEN_NAMES:
            self.player_name_line_edit.setText("Недостоин")
            return

        self.game_manager.player.set_name(player_name)
        self.game_manager.set_player_image(self.cur_pixmap)
        self.game_manager.set_player_background_color(self.cur_color)

        self.main_level = MainLevelScreen(self.main_menu, self.audio_player, self.game_manager)
        self.main_level.show()

        self.close()
