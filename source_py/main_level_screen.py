# Импорт системных библиотек
import sys
import random
import sqlite3

# Импорт PyQt5 компонент
from PyQt5.QtWidgets import QColorDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import QTimer, Qt

# Импорт классов
from source_py.guessing_screen import GuessingScreen
from source_py.final_level_screen import FinalLevelScreen
from source_py.questions.question_builder import QuestionBuilder

import source_py.questions.question_builder as question_builder
import source_py.game_states as GameStates

# Импорт UI компонент
from ui_py.main_level_screen_ui import MainLevelUI

# Импорт сторонних функций
from source_py.frame_setup import setup_frame, setup_players

# Длительность вопросов
QUESTION_DURATION = 15.0
AUDIO_QUESTION_DURATION = 10.0
QUESTION_CHANGE_DURATION = 2
QUESTION_CHANGE_OFFSET = 2

# Разновидности вопросов
QUESTION_REGULAR = 0
QUESTION_TRANSITION = 1
QUESTION_NO_RISK = 2
QUESTION_TRICK = 3

# Длительности времени перехода к вопросу в зависимости от его вида
QUESTION_REGULAR_DURATION = 0
QUESTION_TRANSITION_DURATION = 6
QUESTION_NO_RISK_DURATION = 4
QUESTION_TRICK_DURATION = 4


# Основной игровой уровень
class MainLevelScreen(QMainWindow, MainLevelUI):
    def __init__(self, main_menu, audio_player, game_manager):
        super().__init__()
        self.setupUi(self)

        self.audio_player = audio_player
        self.game_manager = game_manager
        self.main_menu = main_menu

        # Текущее состояние игры
        self.cur_state = GameStates.PLAYER_QUESTION_CHOICE

        # Все участники игры
        self.player = self.game_manager.player
        self.enemy1 = self.game_manager.enemy1
        self.enemy2 = self.game_manager.enemy2
        self.cur_guesser = self.player

        # Все таймеры
        self.enemy1_timer = QTimer(self)
        self.enemy2_timer = QTimer(self)
        self.system_timer = QTimer(self)
        self.game_timer = QTimer(self)

        # Игровые переменные
        self.questions_left = 25
        self.questions = list()

        self.initUI()
        self.reset_round()

    def initUI(self):
        # Настройки параметров окна
        setup_frame(self, self.main_frame)
        setup_players(self)

        # Привязка кнопки выхода из игры (в главное меню)
        self.exit_btn.clicked.connect(self.close_window)

        # Привязка кнопки ответа на вопрос
        self.question_ans_btn.clicked.connect(self.player_answer)

        # Привязка кнопок-вопросов
        # Отключение возможности активации кнопок через нажатие пробела
        for btn in self.buttonGroup.buttons():
            btn.clicked.connect(self.player_choose_question)
            btn.setFocusPolicy(Qt.NoFocus)

        # Привязка названия темы к её номеру
        self.themes = {0: self.theme1, 1: self.theme2,
                       2: self.theme3, 3: self.theme4, 4: self.theme5}

        # Привязка участников игры к виджету, отображающему их баллы
        self.member_points = {self.player: self.player_points,
                              self.enemy1: self.enemy1_points,
                              self.enemy2: self.enemy2_points}

    # При закрытии окна завершаем игры (останавливаем все таймеры)
    # Иначе игра может продолжиться в закрытом окне
    def close_window(self):
        self.stop_game()
        self.main_menu.show()
        self.close()

    # Загрузка и настройка интерфейса для очередного раунда
    def reset_round(self):
        # Обновление интерфейса для нового раунда
        self.question_clarification.setText("Приятной игры")
        self.main_question_label.setText(f"")

        # Первое право выбора вопроса в каждом раунде предоставляется игроку
        self.cur_guesser = self.game_manager.player

        # Начальное состояние каждого раунда - выбор игроком первого вопроса
        self.cur_state = GameStates.PLAYER_QUESTION_CHOICE

        # Выбор двух случайных неповторяющихся вопросов по их номеру
        # Для каждой уникальной категории
        questions = [i for i in range(1, 25)]
        random.shuffle(questions)
        self.questions_transitions = questions[0:2]
        self.questions_no_risk = questions[2:4]
        self.questions_trick = questions[4:6]

        # Настройка виджетов
        self.question_timer.show()
        self.question_timer.setText("")

        self.question_ans_btn.setText("Ответить")
        self.question_ans_btn.hide()
        self.question_ans_btn.setEnabled(False)

        self.answer_label.setText("Выбирайте первый вопрос")
        self.game_status.setText("")

        # Установка ценности вопросов
        # "Включение" кнопок
        for btn in self.buttonGroup.buttons():
            btn.setText(f"{(int(btn.objectName()[-1]) + 1) * 100}")
            btn.setEnabled(True)

        # Загрузка вопросов
        self.questions_left = 25
        self.questions = [[None for i in range(5)] for j in range(5)]
        self.load_questions()

    # Функция загрузки вопросов
    def load_questions(self):
        con = sqlite3.connect("../Jeopardy.db")
        cur = con.cursor()

        last_themes = [theme[0] for theme in cur.execute("""SELECT * From LastThemes""").fetchall()]
        cur.execute("""DELETE FROM LastThemes""")
        con.commit()

        total_themes = cur.execute("""SELECT * FROM Themes""").fetchall()
        random.shuffle(total_themes)
        themes = list()

        # Сохраняем пять уникальных тем для текущей игры
        for theme in total_themes:
            if theme[0] not in self.game_manager.used_themes and theme[1] not in last_themes:
                self.game_manager.used_themes.add(theme[0])

                cur.execute("""INSERT INTO LastThemes VALUES(?)""", (theme[1],))
                con.commit()

                themes.append(theme)

                if len(themes) == 5:
                    break

        for i in range(5):
            self.themes[i].setText(themes[i][0])
            for j in range(5):
                question = cur.execute("""SELECT * FROM Questions
                                          WHERE id = ?""", (themes[i][1] * 5 + j,)).fetchall()[0]
                self.questions[i][j] = QuestionBuilder.get_question(
                    question[1], question[2], question[3], question[4], question[5]
                )

        con.close()

    # Выбор вопроса игроком - происходит через нажатие соответствующей кнопки
    # Выполняется в случае, если текущее игровое состояние - выбор вопроса игроком
    def player_choose_question(self):
        if self.cur_state != GameStates.PLAYER_QUESTION_CHOICE:
            return
        self.quest_btn = self.sender()
        self.prepare_question()

    # Выбор вопроса противником-ботом
    # Выбирает случайный из ещё не заданных
    def ai_choose_question(self):
        i_question = random.randint(1, self.questions_left)
        for btn in self.buttonGroup.buttons():
            if btn.isEnabled():
                i_question -= 1
                if i_question == 0:
                    btn.animateClick(200)
                    self.quest_btn = btn
                    self.game_timer = QTimer()
                    self.set_timer(self.game_timer, True, self.prepare_question, 200)
                    return

    # Подготовка вопроса к выводу на экран
    # Выбор разновидности вопроса (обычный, кот в мешке, без риска, с подвохом)
    def prepare_question(self):
        quest_btn = self.quest_btn

        self.question_value = int(quest_btn.text())
        quest_btn.setText("")
        quest_btn.setEnabled(False)

        self.question_kind = self.get_question_kind()
        self.cur_state = GameStates.LOADING_QUESTION

        self.game_status.setText("")
        self.answer_label.setText("")

        if self.question_kind != QUESTION_REGULAR:
            if self.question_kind == QUESTION_TRANSITION:
                self.prepare_transition_question()
                timer_duration = QUESTION_TRANSITION_DURATION

            elif self.question_kind == QUESTION_NO_RISK:
                self.prepare_no_risk_question()
                timer_duration = QUESTION_NO_RISK_DURATION

            elif self.question_kind == QUESTION_TRICK:
                self.prepare_trick_question()
                timer_duration = QUESTION_TRICK_DURATION

            self.game_timer = QTimer(self)
            self.set_timer(self.game_timer, True, self.show_question, timer_duration * 1000)

        else:
            self.show_question()

    # Подготовка вопроса - кота в мешке
    # Вопрос случайно меняет обладателя
    # На меню вопроса выводится иконка вопроса, проигрывается специальная мелодия
    def prepare_transition_question(self):
        self.members = [self.enemy1, self.enemy2, self.player]
        self.members.remove(self.cur_guesser)
        self.cur_guesser = random.choice(self.members)

        self.main_question_label.setPixmap(
            QPixmap("../images/background_images/question_transition.png"))
        self.question_clarification.setText("Кот в мешке!")
        self.game_status.setText(f"Кота получает {self.cur_guesser.get_name()}")

        self.audio_player.load("../music/question_transition.mp3")
        self.audio_player.set_volume(40)
        self.audio_player.play()

    # Подготовка вопроса без риска
    def prepare_no_risk_question(self):
        self.question_clarification.setText("Вопрос без риска!")
        self.main_question_label.setText("Даже ответив неправильно,\nвы не потеряете баллы")
        self.game_status.setText(f"На вопрос отвечает {self.cur_guesser.get_name()}")

    # Подготовка вопроса с подвохом
    # Стоимость вопроса увеличивается в 1-3 раза
    def prepare_trick_question(self):
        self.question_value = random.randint(self.question_value // 100 + 1,
                                             self.question_value // 100 * 3) * 100
        self.question_clarification.setText("Вопрос с подвохом!")
        self.main_question_label.setText(f"Новая цена вопроса - {self.question_value}")
        self.game_status.setText(f"На вопрос отвечает {self.cur_guesser.get_name()}")

    # Вывод вопроса и пояснение на экран
    def show_question(self):
        quest_btn = self.quest_btn
        self.answer_label.setText("")
        self.game_status.setText("")

        quest_row = int(quest_btn.objectName()[-2])
        quest_col = int(quest_btn.objectName()[-1])

        self.cur_question = self.questions[quest_row][quest_col]

        # Аудио-вопросы требуют дополнительное время на прослушивание композиции
        if type(self.cur_question).__name__ == 'AudioQuestion':
            self.cur_question.ask_question(self.question_clarification, self.main_question_label,
                                           self.audio_player)
            self.game_status.setText("Наслаждаемся композицией")
            self.game_timer = QTimer(self)
            self.set_timer(self.game_timer, True, self.ask_question, AUDIO_QUESTION_DURATION * 1000)
        else:
            self.cur_question.ask_question(self.question_clarification, self.main_question_label)
            self.ask_question()

    # Функция задавания вопроса
    # Смена текущего игрового состояния на ожидание ответа
    # Настройка таймера, отсчитывающего время на ответ
    # Настройка ходов противников
    def ask_question(self):
        # Смена игрового состояния и отслеживание действий игрока
        self.cur_state = GameStates.WAITING_FOR_ANSWER
        self.player_chose = False

        # Включение кнопки ответа и текстового отображения таймера ответа на вопрос
        self.question_ans_btn.show()
        self.question_ans_btn.setEnabled(True)

        self.answer_label.setText("Ждём отвечающих")
        self.game_status.setText("")

        self.question_timer.setText("{:.2f}".format(QUESTION_DURATION))
        self.question_timer.show()
        self.time_offset = 10

        # Создание и запуск таймера - времени на ответ
        self.game_timer = QTimer(self)
        self.set_timer(self.game_timer, False, self.elapse_question_time, self.time_offset)

        # Вложенная функция настройки противника - запускает таймер
        # Вызывающий функцию ответа на вопрос противником
        def setup_enemy(enemy, enemy_timer):
            enemy.move()
            self.set_timer(enemy_timer, True, lambda: self.ai_answer(enemy),
                           enemy.get_thinking_time())

        # Для обычных вопросов отвечающим может стать каждый из участников игры
        if self.question_kind == QUESTION_REGULAR:
            self.cur_participants = [self.player, self.enemy1, self.enemy2]

            if self.enemy1.is_answering():
                self.enemy1_timer = QTimer(self)
                setup_enemy(self.enemy1, self.enemy1_timer)

            if self.enemy2.is_answering():
                self.enemy2_timer = QTimer(self)
                setup_enemy(self.enemy2, self.enemy2_timer)
        # Для специальных вопросов - только один
        else:
            self.cur_participants = [self.cur_guesser]
            if self.cur_guesser != self.player:
                self.question_ans_btn.hide()
                self.question_ans_btn.setEnabled(False)
                self.cur_guesser_timer = QTimer(self)
                setup_enemy(self.cur_guesser, self.cur_guesser_timer)

    # Отсчёт времени вопроса
    def elapse_question_time(self):
        # Высчитывание прошедшего промежутка времени по оптимальной формуле
        # Вывод с двумя знаками после запятой
        remaining_time = float(self.question_timer.text()) - self.time_offset / 400
        self.question_timer.setText("{:.2f}".format(max(0.0, remaining_time)))
        if remaining_time <= 0:
            self.game_timer.stop()
            self.change_question()

    # При закрытии игры во избежание всевозможных проблем
    # Прерываем работу всех потенциально работающих таймеров
    def stop_game(self):
        self.audio_player.stop()
        self.enemy1_timer.stop()
        self.game_timer.stop()
        self.enemy2_timer.stop()
        self.system_timer.stop()

    # Постановка игры на паузу - остановка таймера отсчёта времени на вопрос
    # Остановка таймеров противников с сохранением оставшегося времени
    def pause_game(self):
        self.cur_state = GameStates.PAUSE
        self.game_timer.stop()

        if self.enemy1.is_moving():
            self.enemy1_time_left = self.enemy1_timer.remainingTime()
            self.enemy1_timer.stop()
        if self.enemy2.is_moving():
            self.enemy2_time_left = self.enemy2_timer.remainingTime()
            self.enemy2_timer.stop()

    # Продолжение игры после паузы
    # Происходит в случае - если после паузы
    # Текущий вопрос не получил правильного ответа и не закончились участники
    # Которые могли бы на него ответить (массив cur_participants)
    def resume_game(self):
        if not self.check_for_participants_end():
            self.cur_state = GameStates.WAITING_FOR_ANSWER
            self.answer_label.setText("Ждём отвечающих")
            self.game_timer.start(self.time_offset)
            if self.enemy1.is_moving():
                self.enemy1_timer.start(self.enemy1_time_left)
            if self.enemy2.is_moving():
                self.enemy2_timer.start(self.enemy2_time_left)

    def start_next_level(self):
        self.final_level = FinalLevelScreen(self.main_menu, self.audio_player,
                                            self.game_manager)
        self.final_level.show()
        self.close()

    # Ответ на вопрос со стороны противников
    # cur_enemy - отвечающий противник
    def ai_answer(self, cur_enemy):
        if self.cur_state != GameStates.WAITING_FOR_ANSWER:
            return

        self.cur_state = GameStates.AI_ANSWER
        cur_enemy.stop()
        self.pause_game()

        ai_ans = cur_enemy.get_answer(self.cur_question.get_right_answer())

        # В случае, если не был дан правильный ответ
        # Возвращаемся к состоянию ожидания ответа
        # Иначе - переходим к следующему вопросу
        if not self.check_answer(cur_enemy, ai_ans == self.cur_question.get_right_answer(), ai_ans):
            self.system_timer = QTimer(self)
            self.set_timer(self.system_timer, True, self.resume_game,
                           QUESTION_CHANGE_DURATION * 1000)

    # Ответ на вопрос со стороны игрока
    def player_answer(self):
        # Проверка на то, отвечал ли игрок ранее
        # И является ли текущее состояние игры - ожиданием ответа
        if self.player_chose or self.cur_state != GameStates.WAITING_FOR_ANSWER:
            return

        # Приостанавливаем игру - и переходим к миниигре "Поле Чудес"
        self.pause_game()
        self.player_chose = True
        self.guessing_screen = GuessingScreen(self, self.audio_player, self.game_manager,
                                              self.cur_question.get_right_answer(),
                                              self.cur_question.get_question_id())
        self.guessing_screen.show()
        self.hide()

    # Проверка ответа игрока
    def check_player_answer(self, is_correct):
        # В случае, если ответ не правильный - отключаем
        # Кнопку ответа, продолжаем игру
        if not self.check_answer(self.player, is_correct, self.player.get_mistake()):
            self.question_ans_btn.setEnabled(False)
            self.question_ans_btn.hide()
            self.system_timer = QTimer(self)
            self.set_timer(self.system_timer, True, self.resume_game,
                           QUESTION_CHANGE_DURATION * 1000)

    # Универсальная проверка ответа
    # Возвращаемое значение - правильность ответа (bool)
    def check_answer(self, answer_owner, is_correct, given_ans=''):
        self.answer_label.setText(f"Отвечает {answer_owner.get_name()}")
        self.cur_participants.remove(answer_owner)

        # В случае правильности ответа - начисляем очки
        # Переходим к следующему вопросу и сменяем задающего вопрос на отвечающего
        if is_correct:
            answer_owner.add_right_answer()

            self.answer_label.setText(
                self.answer_label.text() + '\n\n' + f"Верно +{self.question_value}")
            self.change_member_points(answer_owner, True)
            self.cur_guesser = answer_owner
            self.change_question(True)

            return True
        # В случае если ответ неправильный и вопрос не относится к виду "Без Риска"
        # Уменьшаем количество очков отвечающего
        else:
            answer_owner.add_mistake()

            if not self.question_kind == QUESTION_NO_RISK:
                self.answer_label.setText(
                    self.answer_label.text() + '\n' + given_ans +
                    '\n' + f"Неверно -{self.question_value}")

                self.change_member_points(answer_owner, False)
                return False
            else:
                self.answer_label.setText(
                    self.answer_label.text() + '\n' + given_ans + '\n' + "Неверно")
                return False

    # Функция смены вопроса
    # Поведение зависит от того, был ли дан правильный ответ на вопрос
    # Если не был - требовал ли вопрос ответа (имел вид "Кот в мешке", "С подвохом")
    def change_question(self, is_answered=False, players_run_out=False):
        self.game_timer.stop()
        self.question_timer.setText("")
        self.question_ans_btn.hide()
        self.question_ans_btn.setEnabled(False)

        self.main_question_label.setText(self.cur_question.get_right_answer())
        self.game_status.setText(f"{self.cur_guesser.get_name()} выбирает вопрос")

        self.stop_enemies()

        # В случае если не был дан ответ на вопрос
        # Но ответ обязательно требовался из-за вида вопроса
        # Снимаем с выбирающего вопрос баллы
        if not is_answered:
            self.answer_label.setText("Никто не ответил на вопрос")
            if self.question_kind in [QUESTION_TRICK, QUESTION_TRANSITION] and not players_run_out:
                self.answer_label.setText(
                    self.answer_label.text() + '\n\n' + f'-{self.question_value}')
                self.change_member_points(self.cur_guesser, False)

        # Уменьшаем количество неразыгранных вопросов
        # Если их не осталось - завершаем игру
        self.questions_left -= 1
        if self.questions_left == 0:
            self.system_timer = QTimer(self)
            self.set_timer(self.system_timer, True, self.start_next_level,
                           (QUESTION_CHANGE_DURATION + 1) * 1000)
            self.game_status.setText("Конец раунда!")
            return

        # На очередном ходу выбираем текущее игровое состояние
        # В зависимости от отвечающего
        if self.cur_guesser == self.game_manager.player:
            self.cur_state = GameStates.PLAYER_QUESTION_CHOICE
        else:
            self.cur_state = GameStates.AI_QUESTION_CHOICE
            self.game_timer = QTimer(self)
            self.set_timer(self.game_timer, True, self.ai_choose_question,
                           random.randint(QUESTION_CHANGE_DURATION * 1000, (
                                   QUESTION_CHANGE_DURATION + QUESTION_CHANGE_OFFSET) * 1000))

    # Проверка на то, остались ли ещё отвечающие на текущем ходу
    # Если закончились - переходим к следующему вопросу
    def check_for_participants_end(self):
        if not self.cur_participants:
            self.change_question(False, True)
            return True
        return False

    # Останавливаем противников - отключая их таймеры
    # И вызывая соответствующие функции их классов
    def stop_enemies(self):
        if self.enemy1.is_moving():
            self.enemy1.stop()
            self.enemy1_timer.stop()
        if self.enemy2.is_moving():
            self.enemy2.stop()
            self.enemy2_timer.stop()

    # Изменение очков участника игры на QLCDNum
    # Происходит с учетом количества знаков в числе
    # Для выравнивания по центру
    def change_member_points(self, answer_owner, is_correct):
        if is_correct:
            answer_owner.increase_points(self.question_value)
        else:
            answer_owner.decrease_points(self.question_value)

        new_points = answer_owner.get_points()
        points_widget = self.member_points[answer_owner]

        points_widget.setDigitCount(len(str(int(new_points))))
        points_widget.display(new_points)

    # Установка таймера на вызов определенной функции
    def set_timer(self, timer, is_single_shot, connected_func, start_time):
        timer.setSingleShot(is_single_shot)
        timer.timeout.connect(connected_func)
        timer.start(start_time)

    # Выбор вида вопроса
    # Вопрос может быть только одного вида
    def get_question_kind(self):
        if self.questions_left in self.questions_transitions:
            return QUESTION_TRANSITION
        if self.questions_left in self.questions_no_risk:
            return QUESTION_NO_RISK
        if self.questions_left in self.questions_trick:
            return QUESTION_TRICK
        return QUESTION_REGULAR
