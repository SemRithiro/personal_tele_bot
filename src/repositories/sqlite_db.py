import sqlite3

class Sqlite_DB:
    connection = None
    cursor = None
    
    def __init__(self):
        """Initialize the SQLiteDatabase instance"""
        self.connection = sqlite3.connect('sqlite.db')
        self.cursor = self.connection.cursor()

        self._create_user_table()
        
    def execute_select_query(self, query: str):
        """Execute SELECT Query only"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def execute_query(self, query: str, parameter):
        """Execute INSERT and UPDATE Query"""
        self.cursor.execute(query, parameter)
        self.connection.commit()

    def _create_user_table(self):
        columns = {'id': 'VARCHAR(20) PRIMARY KEY', 'first_name': 'VARCHAR(255)', 'last_name': 'VARCHAR(255)', 'username': 'VARCHAR(255)', 'language_code': 'VARCHAR(10)', 'is_bot': 'BOOLEAN'}
        self._create_table('users', columns=columns)

    def _create_table(self, table_name: str, columns: dict):
        """Create a table with dynamic columns."""
        columns_str = ', '.join([f'{col} {type_}' for col, type_ in columns.items()])
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})'
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
