# Импорт системных библиотек
import sys

# Импорт PyQt5 компонент
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

# Импорт класса-перечисления игровых состояний
import source_py.game_states as GameStates

# Импорт UI компонент
from ui_py.guessing_screen_ui import GuessingScreenUI

# Импорт сторонних функций
from source_py.frame_setup import setup_frame

# Сокращения надписей для отображения оставшихся ошибок и времени
MISTAKES_LEFT_PREFIX = "Ошибок Позволено - "
TIME_LEFT_PREFIX = "Времени Осталось - "


# Меню угадывания слова
class GuessingScreen(QMainWindow, GuessingScreenUI):
    def __init__(self, prev_screen, audio_player, game_manager, right_ans, quest_id):
        super().__init__()
        # Настройка переменных-синглтонов и ссылок на другие окна
        self.audio_player = audio_player
        self.game_manager = game_manager
        self.prev_screen = prev_screen

        self.setupUi(self)
        self.initUI()

        # Текущее игровое состояние - ожидание ввода буквы от игрока
        self.cur_state = GameStates.PLAYER_LETTER_CHOICE

        # Настройка количества допустимых ошибок
        # И отключения кнопок, не удовлетворяющих
        # Типу вопроса
        self.lives_left = self.game_manager.get_player_mistakes_count()[quest_id]
        self.cur_lives_heading.setText(f"{MISTAKES_LEFT_PREFIX}{self.lives_left}")
        self.filter_buttons(quest_id)

        # Настройка таймера - минуты на ответ
        self.remaining_time = 60.0
        self.time_offset = 10
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.elapse_time)
        self.timer.start(self.time_offset)

        # Словарь для перевода английских символов
        self.letter_transfer = dict()
        with open("../texts/letter_transfer.txt", 'r', encoding='utf-8') as letter_dict:
            for transfer in letter_dict.readlines():
                orig = transfer.rstrip().split()[0]
                trans = transfer.rstrip().split()[1]
                self.letter_transfer[orig] = trans

        # Настройка правильного ответа - форматирование строки
        # Удаление неиспользуемых символов (' ', '\n', '\t')
        self.right_ans = ' '.join(right_ans[:]).upper()
        if 'Ё' in self.right_ans:
            self.right_ans.replace('Ё', 'Е')
        self.letters_left = len(self.right_ans)
        self.cur_ans = '_' * len(self.right_ans)

        extra_letters = [' ', '\n', '\t']
        for ch in extra_letters:
            self.crossout_letter(ch)

        self.guessable_word.setText(self.cur_ans)

    def initUI(self):
        # Настройки параметров окна
        setup_frame(self, self.main_frame)

        # Установка параметров аудио-проигрывателя
        filename = "../music/guessing_screen.mp3"
        self.audio_player.load(filename)
        self.audio_player.set_volume(5)
        self.audio_player.play()

        # Привязываем кнопки, отвещающие за ввод букв
        # Сохраняя их в словарь {Символ: Кнопка}
        # Отключение возможности активации кнопок через нажатие пробела
        self.buttons = dict()
        for btn in self.buttonGroup.buttons():
            btn.clicked.connect(self.check_letter)
            self.buttons[btn.text()] = btn
            btn.setFocusPolicy(Qt.NoFocus)

    # Отключаем лишние кнопки в зависимости от типа ответа на вопрос
    # Слова или числа
    def filter_buttons(self, is_num_only):
        for btn in self.buttonGroup.buttons():
            if btn.text().isdigit() != is_num_only:
                btn.setEnabled(False)

    # Вычеркивание из слова выбранного символа
    def crossout_letter(self, letter):
        for i in range(len(self.right_ans)):
            if self.right_ans[i] == letter:
                self.letters_left -= 1
                self.cur_ans = self.cur_ans[:i] + letter + self.cur_ans[i + 1:]

    # Угадывание символа (включая штраф за неправильное предположение)
    def guess_letter(self, letter):
        if letter.upper() not in self.right_ans:
            self.lives_left -= 1
            self.cur_lives_heading.setText(f"{MISTAKES_LEFT_PREFIX}{max(0, self.lives_left)}")
        else:
            self.crossout_letter(letter)
            self.guessable_word.setText(self.cur_ans)

        # Завершаем игру в случае, если слово отгадано или закончились дозволенные ошибки
        if self.is_guessed() or self.lives_left < 0:
            self.announce_results()

    # Попытка угадать символ
    # Вызывается через нажатие соответствующей кнопки
    def check_letter(self):
        # Проверка на то, завершена ли игра
        if self.cur_state != GameStates.PLAYER_LETTER_CHOICE:
            return

        self.sender().setEnabled(False)
        self.guess_letter(self.sender().text())

    # Попытка угадать символ
    # Вызывается через взаимодействие с клавиатурой
    def keyPressEvent(self, event):
        # Проверка на то, завершена ли игра
        if self.cur_state != GameStates.PLAYER_LETTER_CHOICE:
            return

        # Преобразование нажатой клавиши в заданный формат
        # По необходимости - перевод и смена регистра
        guessable_letter = self.letter_transfer.get(event.text(), event.text()).upper()

        # Проверка на то - корректен ли ввод и не был ли уже использован нажатый символ
        if (guessable_letter not in self.buttons.keys() or
                not self.buttons[guessable_letter].isEnabled()):
            return

        self.buttons[guessable_letter].setEnabled(False)
        self.guess_letter(guessable_letter)

    # Отсчёт времени на ответ
    def elapse_time(self):
        # Высчитывание прошедшего промежутка времени по оптимальной формуле
        # Вывод с двумя знаками после запятой
        self.remaining_time = self.remaining_time - self.time_offset / 400
        self.time_left_heading.setText(
            TIME_LEFT_PREFIX + "{:.2f}".format(max(0.0, self.remaining_time)))

        if self.remaining_time <= 0:
            self.timer.stop()
            self.announce_results()

    def announce_results(self):
        # Отображаем статус ответа, с задержкой возвращаясь в меню игровой сессии
        if self.is_guessed():
            self.main_heading.setText("Верно!")
        else:
            self.main_heading.setText("Не вышло!")

        # Настриваем таймер для возвращения к игре
        self.timer.stop()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.end_game)
        self.timer.start(2000)

        # Настраиваем таймер для постепенного заглушения музыки
        self.audio_volume_timer = QtCore.QTimer()
        self.audio_volume_timer.timeout.connect(self.mute_audio)
        self.audio_volume_timer.start(60)

        # Меняя игровое состояние - запрещаем игроку продолжать угадывать
        self.cur_state = GameStates.ANSWER_SHOWCASE

    def end_game(self):
        self.audio_player.stop()
        self.timer.stop()
        self.audio_volume_timer.stop()

        self.prev_screen.show()
        self.prev_screen.check_player_answer(self.is_guessed())
        self.close()

    def is_guessed(self):
        return self.cur_ans == self.right_ans

    # Постепенное заглушение фонового сопровождения
    def mute_audio(self):
        self.audio_player.set_volume(self.audio_player.get_volume() - 1)
        if self.audio_player.get_volume() == 0:
            self.audio_volume_timer.stop()
