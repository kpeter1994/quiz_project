from models.question import Question


class BooleanQuestion(Question):
    def __init__(self, question_type, label, level, question, score, answer):
        super().__init__(question_type, label, level, question, score)
        self.answer = answer
        self.user_answer = None

    def full_match(self):
        if self.answer:
            if self.user_answer.lower() in ["igaz", "igen"]:
                return True
        return False


    def ask_question(self):
        self.user_answer = input(f'{self.question} ')

        if self.full_match():
            score = self.score
            message = f'A válsz helyes'
            return score, message


        score = 0
        message = f'A válsz helytelen.'
        return score, message
