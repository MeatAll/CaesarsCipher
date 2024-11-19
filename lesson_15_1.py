import sqlite3
import re

from sqlalchemy import Integer, Column, String

import db

class PhoneBook(db):
    __abstract__ = True

    id = Column(Integer, Nullable = False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String, unique= True)
    number = Column(String, unique= True)

    def add(self, name: str, phone: str):
        if not re.match("^\d+$", phone):
            raise ValueError("Номер должен содержать только цифры.")
        try:
            self.cursor.execute("INSERT INTO persons (name, number) VALUES (?, ?)", (name, phone))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Запись с таким именем или номером уже существует.")

    def get(self, name):
        self.cursor.execute("SELECT id, number FROM persons WHERE name=?", (name,))
        return self.cursor.fetchone()

    def get_all(self):
        self.cursor.execute("SELECT id, name, number FROM persons")
        return self.cursor.fetchall()

    def delete(self, id):
        self.cursor.execute("DELETE FROM persons WHERE id=?", (id,))
        self.connection.commit()

    def close(self):
        self.connection.close()