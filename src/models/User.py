
class User:
    def __init__(self, id: str, first_name: str, last_name: str, username: str, language_code: str, is_bot: bool):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._language_code = language_code
        self._is_bot = is_bot
        
    def __str__(self):
        return f'{self._id} - {self._first_name} {self._last_name} ({self._username})'

    def get_id(self):
        return self._id;