from PyQt5.QtGui import QPixmap, QColor

# Импорт классов - участников игры
from source_py.game_participants.enemy import Enemy
from source_py.game_participants.player import Player
from source_py.game_participants.enemy_builder import EnemyBuilder

EASY = 1
MEDIUM = 2
HARD = 3


# Класс для хранения данных текущей игровой партии
# Хранит данные игрока, противников, настроек игры
# Также предоставляет интерфейс для работы с этими данными
class GameManager:
    def __init__(self):
        self.difficulty = EASY

        # Участники игры
        self.enemy1 = None
        self.enemy2 = None
        self.player = None

        # Множество использованных в текущей игре тем
        # Для предупреждения их повторения
        self.used_themes = set()

        # Словарь для удобства конвертирования сложности в имя файла
        # Содержащего изображение противника
        self.dif_convert = {EASY: "easy", MEDIUM: "medium", HARD: "hard"}

    # Создаём объекты класса Игрок и 2 Противника
    def setup_game(self):
        self.enemy1 = EnemyBuilder.get_enemy(self.difficulty, 0)
        self.enemy2 = EnemyBuilder.get_enemy(self.difficulty, 1)

        player_image = QPixmap("../images/game_members_images/player_images/player0.png")
        player_base_color = "rgb(238, 214, 115)"

        self.player = Player("Игрок", player_image, player_base_color)

    # Изменение сложности игры
    # Вызывается из меню настройки сложности
    # В качестве параметра всегда строка - наименование сложности
    def set_difficulty(self, difficulty):
        for dif in self.dif_convert.keys():
            if difficulty == self.dif_convert[dif]:
                self.difficulty = dif
                return
        self.difficulty = EASY

    def get_difficulty(self):
        return self.difficulty

    def get_player_mistakes_count(self):
        # Словарь для хранения количества жизней
        # Ключ - выбранная сложность игры
        # Значение - количество допустимых ошибок в вопросе (ответ - слово, ответ - число)
        mistakes_cnt = {EASY: (5, 3), MEDIUM: (3, 1), HARD: (1, 0)}
        return mistakes_cnt[self.difficulty]

    # Возвращает изображение 2-х противников в формате QPixmap
    def get_enemies_images(self):
        enemy1_pixmap = QPixmap(
            f"../images/game_members_images/"
            f"enemy_images/{self.dif_convert[self.difficulty]}_enemy1.png")
        enemy2_pixmap = QPixmap(
            f"../images/game_members_images/"
            f"enemy_images/{self.dif_convert[self.difficulty]}_enemy2.png")

        return enemy1_pixmap, enemy2_pixmap

    def get_player_image(self):
        return self.player.image

    def get_player_background_color(self):
        return self.player.background_color

    def set_player_image(self, image):
        self.player.image = image

    def set_player_background_color(self, color):
        self.player.background_color = color
