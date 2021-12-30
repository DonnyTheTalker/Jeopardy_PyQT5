import source_py.game_manager as game_modes
from source_py.game_participants.enemy import Enemy


# Класс-создатель компьютерного противника
# На основании выбранной сложности игры
class EnemyBuilder:
    @staticmethod
    def get_enemy(difficulty, id):
        mistakes_possibilities = {game_modes.EASY: 40, game_modes.MEDIUM: 20, game_modes.HARD: 10}
        answer_possibilities = {game_modes.EASY: 45, game_modes.MEDIUM: 50, game_modes.HARD: 60}
        thinking_time = {game_modes.EASY: 6, game_modes.MEDIUM: 5, game_modes.HARD: 3}
        time_offsets = {game_modes.EASY: 5, game_modes.MEDIUM: 5, game_modes.HARD: 5}

        name = {game_modes.EASY: ["Б.С. Бояршинов", "Ю. С. Рыбников"],
                game_modes.MEDIUM: ["Лосяш", "Совунья"],
                game_modes.HARD: ["А.А. Друзь", "А.А. Вассерман"]}

        return Enemy(name[difficulty][id], mistakes_possibilities[difficulty],
                     answer_possibilities[difficulty],
                     thinking_time[difficulty], time_offsets[difficulty])
