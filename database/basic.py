import sqlite3

import sqlite3

class BaseConfigurationDataBase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("database/db.sqlite3")
        self.curs = self.conn.cursor()
    
    def create_user_table(self):
        self.curs.execute("""CREATE TABLE IF NOT EXISTS users(chat_id UNIQUE, username, fullname)""")
        return("ok")

    