import sqlite3

from lesson_15_1 import PhoneBook


phonebook: PhoneBook()

def create_database():
    connection = sqlite3.connect('phonebook.db') #Cоздать подключение к базe данных
    cursor = connection.cursor() #Установить соединение с базой данных
    global phonebook
    phonebook = PhoneBook(connection, cursor)


    # Создание таблицы persons
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    number TEXT UNIQUE NOT NULL
    )
    ''')


    connection.commit() #Сохранить изменения
    connection.close() #Закрыть соединение


if __name__ == '__main__':
    create_database()
