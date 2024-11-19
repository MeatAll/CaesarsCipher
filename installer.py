import os
from pathlib import Path

directory_user = Path(input('Введите путь к папке: '))

if not directory_user.exists():
    print(f'Папка {str(directory_user)} не существует')
    exit()

folder_path = str(directory_user)

os.chdir(folder_path)
print(f'Создание шаблона директории в папке {os.getcwd()}')

os.makedirs("Конфигурация")
os.makedirs("Управление")
os.makedirs("Шаблоны")

with open(f'{os.getcwd()}/Шаблоны/README.txt', 'w', encoding='utf-8') as file:
    file.write('Документация\nКонфигурация:\nУправление:')
