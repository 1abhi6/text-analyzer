import json

class Database:

    def insert(self, name, email, password):

        with open('users.json', 'r', encoding='utf8') as read_file:
            users = json.load(read_file)

            if email in users:
                return False
            users[email] = [name, password]

        with open('users.json', 'w', encoding='utf8') as write_file:
            json.dump(users, write_file, indent=4)
            return True

    def fetch(self, email, password):
        with open('users.json', 'r', encoding='utf8') as read_file:
            users = json.load(read_file)
            if email in users and users[email][1] == password:
                return (True,users[email][0])
            return False