# Импорт системных библиотек
import sys
import random
import sqlite3

# Импорт PyQt5 компонент
from PyQt5.QtWidgets import QColorDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import QTimer

# Импорт классов
from source_py.guessing_screen import GuessingScreen
from source_py.game_results_screen import GameResultsScreen
from source_py.questions.question_builder import QuestionBuilder

import source_py.questions.question_builder as question_builder
import source_py.game_states as GameStates

# Импорт UI компонент
from ui_py.final_level_screen_ui import FinalLevelUI

# Импорт сторонних функций
from source_py.frame_setup import setup_frame, setup_players

# Длительность вопросов
QUESTION_DURATION = 15.0
QUESTION_SKIP_DURATION = 5.0
AUDIO_QUESTION_DURATION = 10.0
QUESTION_CHANGE_DURATION = 2
QUESTION_CHANGE_OFFSET = 2


# Финальный игровой уровень
class FinalLevelScreen(QMainWindow, FinalLevelUI):
    def __init__(self, main_menu, audio_player, game_manager):
        super().__init__()
        self.setupUi(self)

        self.audio_player = audio_player
        self.game_manager = game_manager
        self.main_menu = main_menu

        # Все участники игры
        self.player = self.game_manager.player
        self.enemy1 = self.game_manager.enemy1
        self.enemy2 = self.game_manager.enemy2

        # Все таймеры
        self.game_timer = QTimer(self)

        self.initUI()
        self.load_question()
        self.reset_round()

    def initUI(self):
        # Настройки параметров окна
        setup_frame(self, self.main_frame)

        # Привязка участников игры к виджету, отображающему их баллы
        # Установка балло участников игры на соответствующих виджетах
        self.member_points = {self.player: self.player_points,
                              self.enemy1: self.enemy1_points,
                              self.enemy2: self.enemy2_points}
        self.change_member_points(self.player)
        self.change_member_points(self.enemy1)
        self.change_member_points(self.enemy2)

        setup_players(self)

        # Привязка кнопки выхода из игры (в главное меню)
        self.exit_btn.clicked.connect(self.close_window)
        self.game_start_btn.clicked.connect(self.show_question)

    # Загрузка темы и случайного вопроса из БД
    def load_question(self):
        con = sqlite3.connect("../Jeopardy.db")
        cur = con.cursor()

        total_themes = cur.execute("""SELECT * FROM Themes""").fetchall()
        random.shuffle(total_themes)
        themes = list()

        # Сохраняем уникальную тему для последнего раунда
        for theme in total_themes:
            if theme[0] not in self.game_manager.used_themes and '\n' not in theme[0]:
                self.game_manager.used_themes.add(theme[0])
                themes.append(theme)
                break

        # Получаем случайный вопрос из выбранной темы
        question = cur.execute("""SELECT * FROM Questions
                                                  WHERE id = ?""",
                               (themes[0][1] * 5 + random.randint(0, 4),)).fetchall()[0]

        self.main_question = QuestionBuilder.get_question(
            question[1], question[2], question[3], question[4], question[5])
        self.question_answer = self.main_question.get_right_answer()
        self.theme_label.setText('Тема финального раунда:\n' + themes[0][0])

        con.close()

    # Функция создания раунда
    def reset_round(self):
        self.game_status.setText("")

        # Если количество баллов игрока - не натуральное число
        # То сделать ставку он не сможет - убираем из интерфейса
        # Frame с виджетами для выбора ставки
        if self.player.get_points() <= 0:
            self.answer_label.setText("Вы не набрали достаточного количества баллов\n"
                                      "Для участия в финальном раунде")

            self.player_is_moving = False
            self.bet_panel.hide()
            self.game_timer = QTimer(self)
            self.set_timer(self.game_timer, True, self.show_question, 3000)
        # Иначе - получаем ставку в диапозоне от 1 до количества баллов игрока
        else:
            self.answer_label.setText("Делайте ставку")

            # Настраиваем слайдер - минимимальное и максимальное значения
            # Связываем слайдер с функцией изменения ставки
            self.bet_slider.setMinimum(1)
            self.bet_slider.setMaximum(self.player.get_points() // 10)
            self.bet_slider.setValue(self.player.get_points())
            self.bet_slider.valueChanged.connect(self.change_bet)
            self.bet_label.setText(str(self.player.get_points()))

            self.player_is_moving = True

    def change_bet(self):
        self.bet_label.setText(str(self.bet_slider.value() * 10))

    # Вывод вопроса на экран
    # Начало основного игрового цикла
    def show_question(self):
        if self.player_is_moving:
            self.player_bet = self.bet_slider.value() * 10
        self.bet_panel.hide()
        self.answer_label.setText("")
        self.game_status.setText("")

        # Аудио-вопросы требуют дополнительное время на прослушивание композиции
        if type(self.main_question).__name__ == 'AudioQuestion':
            self.main_question.ask_question(self.question_clarification, self.main_question_label,
                                            self.audio_player)
            self.game_status.setText("Наслаждаемся композицией")
            self.game_timer = QTimer(self)
            self.set_timer(self.game_timer, True, self.ask_question, AUDIO_QUESTION_DURATION * 1000)
        else:
            self.main_question.ask_question(self.question_clarification, self.main_question_label)
            self.ask_question()

    # Запуск таймера, отсчитывающего оставшееся на размышления время
    def ask_question(self):
        self.answer_label.setText("Время на размышления")
        self.game_status.setText("")

        # Время на размышления формируем в зависимости от того
        # Будет ли отвечать игрок (количество баллов игрока > 0)
        if self.player_is_moving:
            self.question_timer.setText("{:.2f}".format(QUESTION_DURATION))
        else:
            self.question_timer.setText("{:.2f}".format(QUESTION_SKIP_DURATION))
        self.question_timer.show()
        self.time_offset = 10

        # Создание и запуск таймера - времени на размышления
        self.game_timer = QTimer(self)
        self.set_timer(self.game_timer, False, self.elapse_question_time, self.time_offset)

    # Функция отсчёта времени на размышления
    def elapse_question_time(self):
        # Высчитывание прошедшего промежутка времени по оптимальной формуле
        # Вывод с двумя знаками после запятой
        remaining_time = float(self.question_timer.text()) - self.time_offset / 400
        self.question_timer.setText("{:.2f}".format(max(0.0, remaining_time)))
        if remaining_time <= 0:
            self.game_timer.stop()
            self.question_timer.hide()
            self.get_answer()

    # В зависимости от того, отвечает ли игрок
    # Либо запускаем миниигру "Поле Чудес" - либо сразу переходим
    # К проверке ответов всех участников
    def get_answer(self):
        if self.player_is_moving:
            self.guessing_screen = GuessingScreen(self, self.audio_player, self.game_manager,
                                                  self.main_question.get_right_answer(),
                                                  self.main_question.get_question_id())
            self.guessing_screen.show()
            self.hide()
        else:
            self.check_answers()

    # Проверка на правильность пользовательского ответа
    # И запуск функции проверки ответа всех участников игры
    def check_player_answer(self, is_correct):
        self.player_ans_correct = is_correct

        # Добавляем ошибку или правильный ответ в статистику игрока
        if is_correct:
            self.player.add_right_answer()
        else:
            self.player.add_mistake()

        self.check_answers()

    # Функция проверки ответов всех игроков
    def check_answers(self):
        self.answer_label.setText("")
        self.game_status.setText("")

        self.answer_label.setText(f"Правильный ответ - {self.main_question.get_right_answer()}")
        self.main_question_label.setText(self.main_question.get_right_answer())

        # Сохраняем всех участников игры в массив и храним индекс
        # Текущего участника
        self.cur_participants = [self.enemy1, self.player, self.enemy2]
        self.i_answer_owner = 0

        # Запускаем функцию проверки ответа конкретного игрока с задержкой
        # Нужной для отображения на экране правильного ответа
        self.game_timer = QTimer(self)
        self.set_timer(self.game_timer, True, self.check_participant_answer, 2000)

    # Проверка правильности ответа конкретного участника
    def check_participant_answer(self):
        self.question_clarification.setText("Сверяем ответы участников")
        self.game_status.setText("")

        cur_answer_owner = self.cur_participants[self.i_answer_owner]
        self.i_answer_owner += 1

        self.main_question_label.setText(f"Отвечает {cur_answer_owner.get_name()}\n")

        # В случае - если участник имеет баланс <= 0
        # Для него раунд пропущен - уведомляем об этом через главный label
        if cur_answer_owner.get_points() <= 0:
            self.main_question_label.setText(f"{cur_answer_owner.get_name()} не имеет\n"
                                             f"Нужного количества очков\n"
                                             f"И пропускает раунд")
        # В случае - если участник - игрок
        # Проверяем правильность ответа по полученной из окна угадывания
        # Логической переменной
        elif cur_answer_owner == self.player:
            if self.player_ans_correct:
                ans_status = f"\nВерно\nРазмер ставки {self.player_bet}"
                p_bet = self.player_bet
                p_bet_str = f'+{p_bet}'
            else:
                ans_status = f"{self.player.get_mistake()}\nНеверно\nРазмер ставки {self.player_bet}"
                p_bet = -self.player_bet
                p_bet_str = p_bet

            self.main_question_label.setText(self.main_question_label.text() + ans_status)
            self.change_member_points(self.player, p_bet)
            self.game_status.setText(f"{self.player.get_name()} {p_bet_str}")
        # В случае - если участник - противник
        # Сравниваем правильный ответ с полученным от противника
        # Меняем ставку в зависимости от правильности ответа
        else:
            ai_ans = cur_answer_owner.get_answer(self.main_question.get_right_answer())

            if ai_ans == self.main_question.get_right_answer():
                ai_bet = random.randint(cur_answer_owner.get_points() // 2 // 10,
                                        cur_answer_owner.get_points() // 10) * 10
                ans_status = f"\nВерно\nРазмер ставки {ai_bet}"
                ai_bet_str = f'+{ai_bet}'
            else:
                ai_bet = random.randint(cur_answer_owner.get_points() // 4 // 10,
                                        cur_answer_owner.get_points() // 4 * 3 // 10) * 10
                ans_status = f"{cur_answer_owner.get_mistake()}\nНеверно\nРазмер ставки {ai_bet}"
                ai_bet = -ai_bet
                ai_bet_str = ai_bet

            self.main_question_label.setText(self.main_question_label.text() + ans_status)
            self.change_member_points(cur_answer_owner, ai_bet)
            self.game_status.setText(f"{cur_answer_owner.get_name()} {ai_bet_str}")

        # Если текущий участник - последний - запускаем функцию анонса результатов
        # Иначе - проверяем ответ следующего игрока
        self.game_timer = QTimer(self)
        if self.i_answer_owner == len(self.cur_participants):
            self.set_timer(self.game_timer, True, self.announce_results, 4000)
        else:
            self.set_timer(self.game_timer, True, self.check_participant_answer, 4000)

    # При закрытии игры останавливаем все таймеры
    # Иначе игра может продолжиться в закрытом окне
    def close_window(self):
        self.game_timer.stop()
        self.audio_player.stop()
        self.main_menu.show()
        self.close()

    # Переход к окну результатов игры
    def announce_results(self):
        self.results_screen = GameResultsScreen(self.main_menu, self.audio_player,
                                                self.game_manager)
        self.results_screen.show()
        self.close()

    # Изменение очков участника игры на QLCDNum
    # Происходит с учетом количества знаков в числе
    # Для выравнивания по центру
    def change_member_points(self, answer_owner, question_value=0):
        answer_owner.increase_points(question_value)

        new_points = answer_owner.get_points()
        points_widget = self.member_points[answer_owner]

        points_widget.setDigitCount(len(str(int(new_points))))
        points_widget.display(new_points)

    # Установка таймера на вызов определенной функции
    def set_timer(self, timer, is_single_shot, connected_func, start_time):
        timer.setSingleShot(is_single_shot)
        timer.timeout.connect(connected_func)
        timer.start(start_time)
