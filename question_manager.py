from request_manager import RequestManager
from question import *
from bs4 import BeautifulSoup
from random import randint

class QuestionManager:
    def __init__(self):
        self.amount = 10
        self.type = 'boolean'
        self.rm = RequestManager()
        self.current_question = None
        self.score = 0
        self.question_bank = None

    def default_request_questions(self):
        self.question_bank = []
        request_dict = {'size': self.amount, 'type': self.type}
        response = self.rm.make_request(request_dict)
        if response:
            for element in response['results']:
                self.question_bank.append(BooleanQuestion(BaseQuestion(element)))
            return True
        else:
            return False

    def ask_question(self):
        if self.question_bank:
            self.current_question = self.question_bank.pop(randint(0,len(self.question_bank)-1))
            print(BeautifulSoup(self.current_question.get_question(), 'html.parser').get_text())
            return True
        else:
            print("Congratulations, you've completed the quiz!")
            return False

    def answer_question(self, answer: str):
        if self.current_question.get_correct() == answer.title():
            self.score += 1
            print("Correct answer!")
            return True
        else:
            print(f"Incorrect answer! The answer was: {self.current_question.get_correct()}")
            print(f"You got {self.score} questions correct!\n\n")
            return False