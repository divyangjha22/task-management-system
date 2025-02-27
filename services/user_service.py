from models.user import User

class User_Service:
    def __init__(self):
        self.users = {}

    def add_users(self, id, name,  email):
        user = User(id, name, email)
        self.users[id] = user
        return user

    def get_user(self, id):
        return self.users.get(id)