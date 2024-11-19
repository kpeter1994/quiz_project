from models.question import Question
from difflib import SequenceMatcher

class SelectQuestion(Question):

    def __init__(self, question_type, label, level, question, score, answer, options):
        super().__init__(question_type, label, level, question, score)
        self.answer = answer
        self.options = options
        self.user_answer = None



    def ask_question(self):
        options_dict = {chr(ord('A') + i): option for i, option in enumerate(self.options)}

        print(self.question)
        for key, value in options_dict.items():
            print(f"{key}: {value}")

        self.user_answer = input('A válaszod: ').upper()

        if self.user_answer in options_dict and options_dict[self.user_answer] == self.answer:
            score = self.score
            message = "A válasz helyes! \n"
            return score, message

        score = 0
        message = f'A válsz helytelen. A helyes válsz: {self.answer}\n'
        return score, message
