# Импорт системных библиотек
import sys
import sqlite3

# Импорт PyQt5 компонент
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

# Импорт UI компонент
from ui_py.game_results_screen_ui import GameResultsScreenUI

# Импорт сторонних функций
from source_py.frame_setup import setup_frame

# Длительность различных аудио-сегментов в секундах
GAME_WIN_MUSIC_DURATION = 5.75
GAME_LOSS_MUSIC_DURATION = 11.75


# Меню отображения результата игры
class GameResultsScreen(QMainWindow, GameResultsScreenUI):
    def __init__(self, main_menu, audio_player, game_manager):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.audio_player = audio_player
        self.game_manager = game_manager
        self.main_menu = main_menu

        # Сохраняем учасников игры для дальнейшего доступа к их результатам
        self.player = self.game_manager.player
        self.enemy1 = self.game_manager.enemy1
        self.enemy2 = self.game_manager.enemy2

        self.show_results()

    def initUI(self):
        # Настройки параметров окна
        setup_frame(self, self.main_frame)

    # Вывод на экран участников, отсортированный по количеству набранных очков
    # Также вывод текста с опытом, начисленным игроку за то или иное занятое место
    def show_results(self):
        # Массив участников текущей игры с каждой их характеристикой
        participants = [(self.player, self.game_manager.get_player_image(),
                         self.game_manager.get_player_background_color(), self.player.get_points()),
                        (self.enemy1, self.game_manager.get_enemies_images()[0],
                         "rgb(238, 214, 115)",
                         self.enemy1.get_points()),
                        (self.enemy2, self.game_manager.get_enemies_images()[1],
                         "rgb(238, 214, 115)",
                         self.enemy2.get_points())]

        # Словари для доступа к UI-элементам по номеру места, занятого участником игры
        # UI (иконка участника, количество его очков, панель с именем и его изображение)
        frames = {0: self.place1_frame, 1: self.place2_frame, 2: self.place3_frame}
        points = {0: self.place1_points, 1: self.place2_points, 2: self.place3_points}
        names = {0: self.place1_name, 1: self.place2_name, 2: self.place3_name}
        images = {0: self.place1_image, 1: self.place2_image, 2: self.place3_image}

        # Сортируем участников в соответствии с количеством набранных очков
        # Выводим их характеристики на UI элементы
        participants.sort(key=lambda member: -member[-1])
        for i in range(len(participants)):
            frames[i].setStyleSheet(f"background-color: {participants[i][-2]}")
            names[i].setText(participants[i][0].get_name())
            images[i].setPixmap(participants[i][1])
            points[i].setDigitCount(len(str(participants[i][-1])))
            points[i].display(participants[i][-1])

        # Начисление очков игроку - и запись его результатов в БД
        for i in range(len(participants)):
            if participants[i][0] == self.player:
                self.add_experience(i)

        # Таймер для проигрывания мелодии-окончания перед выходом в главное меню
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.end_game)

        if participants[0][0] == self.player:
            self.game_results.setText("Поздравляем с победой!")
            self.audio_player.load("../music/game_win.mp3")
            self.timer.start(GAME_WIN_MUSIC_DURATION * 1000)
        else:
            self.game_results.setText("К сожалению, вы проиграли!")
            self.audio_player.load("../music/game_loss.mp3")
            self.timer.start(GAME_LOSS_MUSIC_DURATION * 1000)

        self.audio_player.set_volume(30)
        self.audio_player.play()

    def end_game(self):
        self.main_menu.show()
        self.close()

    # Сохранение прогресса игрока в БД
    def add_experience(self, player_place):
        con = sqlite3.connect("../Jeopardy.db")
        cur = con.cursor()

        player_name = self.player.get_name()
        players = list(x[0] for x in cur.execute("SELECT Name FROM Leaders").fetchall())

        # Добавление нового игрока в БД
        if player_name not in players:
            cur.execute("INSERT INTO Leaders VALUES(?, ?, 0, 0, 0)",
                        (player_name, self.player.get_points()))
            con.commit()

        player_record = cur.execute("""SELECT record from Leaders
                                        WHERE name = ?""", (player_name,)).fetchall()[0][0]
        player_record = max(player_record, self.player.get_points())
        experience_bonus = {0: 100, 1: 50, 2: 25}

        # Обновление статистики игрока
        cur.execute("""UPDATE Leaders
                        SET record = ?, experience = experience + ?, 
                            n_mistakes = n_mistakes + ?, n_answers = n_answers + ?
                        WHERE name = ?""",
                    (player_record,
                     experience_bonus[player_place] * self.game_manager.get_difficulty(),
                     self.player.get_mistakes_count(), self.player.get_right_answers_count(),
                     player_name))
        con.commit()

        self.expreience_label.setText(
            f"+{experience_bonus[player_place] * self.game_manager.get_difficulty()} очков опыта")

        con.close()
