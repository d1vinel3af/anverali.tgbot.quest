import sqlite3

class UserDataBase:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("database/db.sqlite3")
        self.curs = self.conn.cursor()
    
    #TODO: Добавить функцию создания пользователя
    def create(self, chat_id, username, fullname):
        ...


    #FIXME: Отредактировать получение информации о пользователе
    def get(self, obj, value):
        sql_str = f"SELECT * FROM users WHERE {obj}='{value}'"
        responce = self.curs.execute(sql_str)
        record = None if responce.fetchone() == [] else responce.fetchone()
        return record

    