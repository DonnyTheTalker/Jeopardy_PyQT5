from source_py.game_participants.game_member import GameMember
import random


# Компьютерный противник
# Содержит набор переменных, составляющих основу ИИ
# Время на ответ; вероятность ответа и участия в ходе
# Также содержит time_offset - случайное число - отклонение от стандартного времени ответа

class Enemy(GameMember):
    def __init__(self, name, mistake_possibility, answer_possibility, thinking_time, time_offset):
        GameMember.__init__(self, name)
        self.mistake_possibility = mistake_possibility
        self.answer_possibility = answer_possibility
        self.thinking_time = thinking_time
        self.time_offset = time_offset
        self.moving = False

    def move(self):
        self.moving = True

    def stop(self):
        self.moving = False

    def is_moving(self):
        return self.moving

    # Проверка на то, будет ли противник пытаться отвечать на текущем ходе
    def is_answering(self):
        return random.randint(0, 100) * random.randint(0, 100) % 100 <= self.answer_possibility

    # Получение случайного времени на 'раздумие' - задержку перед попыткой ответа
    def get_thinking_time(self):
        return int((self.thinking_time + random.uniform(0.0, float(self.time_offset))) * 1000)

    # Получение ответа противника на вопрос с учетом возможной ошибки
    def get_answer(self, right_ans):
        if random.randint(0, 100) * random.randint(0, 100) % 100 <= self.mistake_possibility:
            return self.get_mistake()
        return right_ans
