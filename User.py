import json
from datetime import datetime

class User:
    def __init__(self, name, filename="users.json"):
        self.name = name
        self.filename = filename
        self.labels = None
        self.score = None

    def open_file_for_read(self):
        with open(self.filename, 'r', encoding="utf-8") as user_file:
            return json.load(user_file)

    def is_new_user(self):
        for user in self.open_file_for_read():
            if user['name'] == self.name:
                return False
        return True

    def get_user_labels(self, available_labels):
        prefer_labels = input(
            f"Melyik témákat részesíted előnyben az alábbiak közül: {available_labels} "
            f"(Kérlek, a felsorolás elemeit szóközzel válaszd el.) "
        )
        return prefer_labels.split()

    def save_user(self, labels):
        users = self.open_file_for_read()
        prefer_labels = self.get_user_labels(labels)
        users.append({
            "name": self.name,
            "labels": [prefer_labels],
            "max_score": 0,
            "last_game": datetime.now().isoformat()
        })
        with open(self.filename, 'w', encoding="utf-8") as user_file:
            json.dump(users, user_file, ensure_ascii=False, indent=4)




    def format_user_name(self):
        return self.name.split()[-1]

