# Базовый абстрактный класс, наследующий общие
# Атрибуты для всех типов вопросов

# .clarification - пояснение к вопросу
# .content - содержимое вопроса (текст/фото/аудио)
# .right_ans - ответ на вопрос
# .quest_id - тип вопроса (0 - ответ - слово, 1 - ответ - число)


class Question:
    def __init__(self, clarification, content, right_ans, quest_id):
        self.clarification = clarification
        self.content = content
        self.right_ans = right_ans
        self.quest_id = quest_id

    def get_right_answer(self):
        return self.right_ans

    def get_question_id(self):
        return self.quest_id
