from models.question import Question


class IntegerQuestion(Question):
    def __init__(self, question_type, label, level, question, score, answer):
        super().__init__(question_type, label, level, question, score)
        self.answer = answer
        self.user_answer = None

    def full_match(self):
        return self.user_answer == self.answer

    def is_difference_within_limit(self):
        relative_difference = abs(self.answer - self.user_answer) / self.answer
        return relative_difference < 0.1

    def ask_question(self):
        self.user_answer = int(input(f'{self.question} '))

        if self.full_match():
            score = self.score
            message = f'A válsz helyes'
            return score, message

        if self.is_difference_within_limit():
            score = self.score - 3
            message = f'A válszod helytelen. A helyes válsz: {self.answer} de mert kevesebb mint 10%-ot tévedtél jár {score} pont'
            return score, message

        score = 0
        message = f'A válsz helytelen. A helyes válsz: {self.answer}'
        return score, message
