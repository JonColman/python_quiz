from abc import ABC, abstractmethod

class BaseQuestion:
    def __init__(self, data):
        self.data = data

    def get_question(self):
        return self.data['question']

    def get_difficulty(self):
        return self.data['difficulty']

    def get_type(self):
        return None

    def get_category(self):
        return self.data['category']

    def get_correct(self):
        return self.data['correct_answer']

    def get_incorrect(self):
        return self.data['incorrect_answers']

class QuestionWrapper(ABC):
    def __init__(self, base: BaseQuestion):
        self.base = base

    @abstractmethod
    def get_question(self):
        pass

    def get_difficulty(self):
        return self.base.get_difficulty()

    def get_type(self):
        return self.base.get_type()

    def get_correct(self):
        return self.base.get_correct()

    def get_incorrect(self):
        return self.base.get_incorrect()

    def get_category(self):
        return self.base.get_category()

#Decorator Class
class BooleanQuestion(QuestionWrapper):
    def __init__(self, base: BaseQuestion):
        super().__init__(base)

    def get_question(self):
        return f"{self.base.get_question()} True or False?"