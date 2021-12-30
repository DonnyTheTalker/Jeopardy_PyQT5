from source_py.questions.audio_question import AudioQuestion
from source_py.questions.text_question import TextQuestion
from source_py.questions.photo_question import PhotoQuestion

from PyQt5.QtGui import QPixmap

TEXT_QUESTION = 0
PHOTO_QUESTION = 1
AUDIO_QUESTION = 2


# Класс-создатель всех вопросов
class QuestionBuilder:
    @staticmethod
    def get_question(clarification, content, right_ans, quest_id, quest_type):
        if quest_type == TEXT_QUESTION:
            return TextQuestion(clarification, content, right_ans, quest_id)
        if quest_type == PHOTO_QUESTION:
            return PhotoQuestion(clarification, QPixmap(content), right_ans, quest_id)
        if quest_type == AUDIO_QUESTION:
            return AudioQuestion(clarification, content, right_ans, quest_id)
        return None
