# Импорт системных библиотек
import sys

# Импорт PyQt5 компонент
from PyQt5.QtWidgets import QApplication, QMainWindow

# Импорт классов
from source_py.player_setup_screen import PlayerSetupScreen

# Импорт UI компонент
from ui_py.game_setup_screen_ui import GameSetupUI

# Импорт сторонних функций
from source_py.frame_setup import setup_frame


# Меню выбора сложности
class GameSetupScreen(QMainWindow, GameSetupUI):
    def __init__(self, main_menu, audio_player, game_manager):
        super().__init__()

        self.audio_player = audio_player
        self.game_manager = game_manager
        self.main_menu = main_menu

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Настройки параметров окна
        setup_frame(self, self.main_frame)

        # Привязка кнопки перехода к следующему этапу подготовки к игре
        self.next_stage_btn.clicked.connect(self.next_stage)

        # Привязка кнопок выбора сложности
        self.buttonGroup.buttonToggled.connect(self.change_difficulty)

    # Смену отображаемых подсказок
    # И иконок компьютерных противников
    def change_difficulty(self):
        dif = self.buttonGroup.checkedButton().objectName().split('_')[0]

        # Изменяем состояние сложности в хранителе информации
        self.game_manager.set_difficulty(dif)

        enemies_icons = self.game_manager.get_enemies_images()
        self.enemy1_label.setPixmap(enemies_icons[0])
        self.enemy2_label.setPixmap(enemies_icons[1])

        self.difficulty_hint_main.setText(
            self.get_text_from_file(f"../texts/difficulty_hints/{dif}_difficulty"
                                    f"_hint_main.txt", "Сегодня без подсказки")
        )
        self.difficulty_hint_extra.setText(
            self.get_text_from_file(f"../texts/difficulty_hints/{dif}_difficulty"
                                    f"_hint_extra.txt", "Сегодня без подсказки")
        )
        self.enemy_hint_main.setText(
            self.get_text_from_file(f"../texts/enemy_hints/{dif}_enemy"
                                    f"_hint.txt", "Сегодня без подсказки")
        )

    def next_stage(self):
        self.game_manager.setup_game()
        self.player_setup = PlayerSetupScreen(self.main_menu, self.audio_player, self.game_manager)
        self.player_setup.show()
        self.close()

    # Загрузка текста из файла - в случае ошибки
    # Возвращаем заранее заготовленный текст
    def get_text_from_file(self, filename, exc):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return exc
