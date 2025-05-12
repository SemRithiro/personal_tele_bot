from src.controllers.sqliteDB import SqliteDB

from src.models.User import User

class Users:
    users = []
    
    datasource = None
    
    def __init__(self):
        pass
    
    def set_datasource(self, datasource: SqliteDB):
        """Set custom datasource"""
        self.datasource = datasource
        users = self.datasource.execute_select_query('SELECT * FROM users')
        for user in users:
            self.users.append(User(user[0], user[1], user[2], user[3], user[4], user[5]))
        
    def add(self, user: User):
        """Add new user to list and datasource"""
        self.users.append(user)
        if self.datasource != None:
            self.datasource.execute_query('INSERT OR REPLACE INTO users (id, first_name, last_name, username, language_code, is_bot) VALUES (?, ?, ?, ?, ?, ?)', (
                user.id,
                user.first_name,
                user.last_name or "",
                user.username or "",
                user.language_code or "",
                user.is_bot or False
            ))
        
    def get_users(self):
        """List all users"""
        return self.users
    
    def is_user_exist(self, id_: str):
        """Check if user id already exist"""
        for user in self.users:
            if user.get_id() == id_:
                return user
        return None