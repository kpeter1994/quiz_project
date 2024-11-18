import json
import random

from models.user import User
from models.string_question import StringQuestion
from models.integer_question import IntegerQuestion
from models.boolean_question import BooleanQuestion



class QuizController:

    def __init__(self, input_filename="data/quizzes.json"):
        self.input_filename = input_filename
        self.user = None
        self.game_score = 0

    def open_file_for_read(self):
        with open(self.input_filename, 'r', encoding="utf-8") as quiz_file:
            return json.load(quiz_file)

    def get_all_label(self):
        all_label = set()
        for quiz_item in self.open_file_for_read():
            all_label.add(quiz_item["label"])
        return all_label

    def welcome_user(self):
        name = input('Mi a neved? ')
        self.user = User(name)
        if self.user.is_new_user():
            labels_list = ', '.join(sorted(self.get_all_label()))
            self.user.save_user(labels_list)
            self.user.init_user()
            print(f'Üdvözlünk, {self.user.format_user_name()}! Kezdheted az első játékodat.')
        else:
            self.user.init_user()
            print(f'Üdv újra itt, {self.user.format_user_name()}! Ideje megdönteni a rekordodat, ami {self.user.score} pont')


    def get_questions_for_user(self):
        selected_question = []
        for question in self.open_file_for_read():
            if question['type'] == 'boolean' or question['type'] == 'boolean':
                selected_question.append(question)
        return random.sample(selected_question, min(len(selected_question), 10))

    def play_quiz(self):
        question_classes = {
            'string': StringQuestion,
            'integer': IntegerQuestion,
            'boolean': BooleanQuestion
        }

        for question in self.get_questions_for_user():
            question_type = question['type']
            if question_type in question_classes:
                extra_args = {}
                if question_type == 'string':
                    extra_args['acceptable'] = question.get('acceptable', [])

                quiz_item = question_classes[question_type](
                    question['type'],
                    question['label'],
                    question['level'],
                    question['question'],
                    question['score'],
                    question['answer'],
                    **extra_args
                )
                score, message = quiz_item.ask_question()
                self.game_score += score
                print(message)

        self.user.update_max_score(self.game_score)
        self.close_game()

    def close_game(self):
        print(f'Gratulálok az eredményedhez: {str(self.game_score)}')
        new_game = input('Készen állsz a következő játékra? (igen/nem) ')
        if new_game == 'igen':
            self.play_quiz()



quiz = QuizController()
quiz.welcome_user()
quiz.play_quiz()
