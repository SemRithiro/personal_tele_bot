from .User import User

class Users:
    def __init__(self):
        self.users = []
        
    def add(self, user: User):
        self.users.append(user)
        
    def get_users(self):
        return self.users
    
    def is_user_exist(self, id_: str):
        for user in self.users:
            if user.get_id() == id_:
                return user
        return None