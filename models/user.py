import json
from datetime import datetime


class User:
    def __init__(self, name, filename="data/users.json"):
        self.name = name
        self.filename = filename
        self.labels = None
        self.score = None

    def manage_file(self, mode, data=None):
        with open(self.filename, mode, encoding="utf-8") as user_file:
            if mode == "r":
                return json.load(user_file)
            elif mode == "w":
                json.dump(data, user_file, ensure_ascii=False, indent=4)

    def is_new_user(self):
        for user in self.manage_file('r'):
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
        users = self.manage_file('r')
        prefer_labels = self.get_user_labels(labels)
        users.append({
            "name": self.name,
            "labels": prefer_labels,
            "max_score": 0,
            "last_game": datetime.now().isoformat()
        })
        self.manage_file('w',users)

    def update_max_score(self, score):
        users = self.manage_file('r')

        for user in users:
            if user["name"] == self.name:
                if user["max_score"] < score:
                    user["max_score"] = score
                user["last_game"] = datetime.now().isoformat()

        self.manage_file('w',users)

    def init_user(self):
        for user in self.manage_file('r'):
            if user["name"] == self.name:
                self.labels = user["labels"]
                self.score = user["max_score"]

    def format_user_name(self):
        return self.name.split()[-1]

