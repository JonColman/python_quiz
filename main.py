from question_manager import QuestionManager

QM = QuestionManager()

while True:
    choice = input("Welcome to Jon\'s quiz! Would you like to play? Y or N: ")
    if choice.upper() == 'Y':
        if QM.default_request_questions():
            while QM.ask_question():
                if not QM.answer_question(input()):
                    break
        else:
            break
    else:
        print("That's a shame :(\nGoodbye!")
        break