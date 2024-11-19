from models.question import Question
from difflib import SequenceMatcher

class StringQuestion(Question):
    DEDUCTION_FOR_PARTIAL_MATCH = 2

    def __init__(self, question_type, label, level, question, score, answer, acceptable=None):
        super().__init__(question_type, label, level, question, score)
        self.answer = answer
        self.acceptable = acceptable
        self.user_answer = None

    def full_match(self):
        return self.user_answer == self.answer.lower()

    def acceptable_match(self):
        if self.acceptable:
            return self.user_answer in self.acceptable

    def sub_match(self):
        similarity = SequenceMatcher(None, self.user_answer, self.answer).ratio()
        if similarity > 0.7:
            return True

        if self.acceptable:
            for acceptable_answer in self.acceptable:
                acceptable_similarity = SequenceMatcher(None, self.user_answer, acceptable_answer.lower()).ratio()
                if acceptable_similarity > 0.7:
                    return True

        return False

    def ask_question(self):
        self.user_answer = input(f'{self.question} ').lower()

        if self.full_match():
            score = self.score
            message = f'A válsz helyes'
            return score, message

        if self.acceptable_match():
            score = self.score
            message = f'A válsz helyes'
            return score, message

        if self.sub_match():
            score = (self.score - self.DEDUCTION_FOR_PARTIAL_MATCH)
            message = f'A válsz részben helyes. A teljesen helyes válsz: {self.answer}'
            return score, message

        score = 0
        message = f'A válsz helytelen. A helyes válsz: {self.answer}'
        return score, message
