
class User:
    def __init__(self, id: str, first_name: str, last_name: str, username: str, language_code: str, is_bot: bool):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_bot = is_bot
        
    def get_id(self):
        return self.id;