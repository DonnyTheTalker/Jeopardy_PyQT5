import random


# Базовый абстрактный класс участника игры
# От него будут наследоваться класс Игрока и Противника
class GameMember:
    def __init__(self, name):
        self.cur_points = 0
        self.n_mistakes = 0
        self.n_right_ans = 0
        self.name = name

        try:
            with open("../texts/members_mistakes.txt", 'r', encoding='utf-8') as mistakes:
                self.mistakes = [mistake.rstrip('\n') for mistake in mistakes.readlines()]
        except FileNotFoundError:
            self.mistakes = ['Не знаю']

    def increase_points(self, amount):
        self.cur_points += amount

    def decrease_points(self, amount):
        self.cur_points -= amount

    def add_mistake(self):
        self.n_mistakes += 1

    def get_mistakes_count(self):
        return self.n_mistakes

    def add_right_answer(self):
        self.n_right_ans += 1

    def get_right_answers_count(self):
        return self.n_right_ans

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_points(self):
        return self.cur_points

    def get_mistake(self):
        return random.choice(self.mistakes)
