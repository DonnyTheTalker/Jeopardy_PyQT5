from source_py.questions.base_question import Question

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap


# Вопрос-картинка
class PhotoQuestion(Question):
    def __init__(self, clarification, content, right_ans, quest_id):
        Question.__init__(self, clarification, content, right_ans, quest_id)

    # Задаём вопрос, выводя на экран пояснение и загружая картинку
    def ask_question(self, clarification_label, question_label):
        clarification_label.setText(self.clarification)
        question_label.setPixmap(self.content)
