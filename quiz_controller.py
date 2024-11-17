import json
from User import User


class QuizController:

    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.user = None

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
            return print(f'Üdvözlünk, {self.user.format_user_name()}! Kezdheted az első játékodat.')
        return print(f'Üdv újra itt, {self.user.format_user_name()}! Ideje megdönteni a rekordodat.')

    def get_questions_for_user(self):
        pass





quiz = QuizController('quiz.json')
print(quiz.get_all_label())
quiz.welcome_user()