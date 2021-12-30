from source_py.questions.base_question import Question

from PyQt5.QtWidgets import QLabel


# Текстовый вопрос
class TextQuestion(Question):
    def __init__(self, clarification, content, right_ans, quest_id):
        Question.__init__(self, clarification, content, right_ans, quest_id)

    # Задаём вопрос, выводя на экран пояснение и текст вопроса
    def ask_question(self, clarification_label, question_label):
        clarification_label.setText(self.clarification)
        question_label.setText(self.content)
