from models.question import Question


class FloatQuestion(Question):
    def __init__(self, question_type, label, level, question, score, answer, tolerance):
        super().__init__(question_type, label, level, question, score)
        self.answer = answer
        self.tolerance = tolerance
        self.user_answer = None

    def is_acceptance_range(self):
        return self.answer - self.tolerance < self.user_answer < self.answer + self.tolerance

    def ask_question(self):

        try:
            self.user_answer = float(input(f'{self.question} '))

            if self.is_acceptance_range():
                score = self.score
                message = f'A válszod helyesen az elfogadási tartományon belül van {self.answer - self.tolerance} - {self.answer + self.tolerance}'
                return score, message

            score = 0
            message = f'A válsz helytelen. A helyes válsz: {self.answer}'
            return score, message

        except ValueError:
            score = 0
            message = "Érvénytelen válasz. Számot kell megadnod."
            return score, message