from source_py.questions.base_question import Question
from source_py.audio_player import AudioPlayer

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

QUESTION_PICTURE = '../images/background_images/audio_question.png'
AUDIO_VOLUME = 70


# Аудио-вопрос
class AudioQuestion(Question):
    def __init__(self, clarification, content, right_ans, quest_id):
        Question.__init__(self, clarification, content, right_ans, quest_id)

    # Задаем вопрос, выводя на экран пояснение и картинку музыкального вопроса
    # Также запуская текущую композицию в проигрывателе
    def ask_question(self, clarification_label, question_label, audio_player):
        clarification_label.setText(self.clarification)
        question_label.setPixmap(QPixmap(QUESTION_PICTURE))
        audio_player.load(self.content)
        audio_player.set_volume(AUDIO_VOLUME)
        audio_player.play()
