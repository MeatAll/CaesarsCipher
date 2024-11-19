import csv
import json
import math
from os import getcwd, path
from tkinter.filedialog import askopenfilename, askdirectory
from statistics import mean


class FileHandler:
    '''Класс для работы с файлами и директорияими.'''
    @staticmethod
    def _get_path_to_json():
        """Задать путь к JSON.

        Returns:
            Путь в формате string.
        """
        title = 'Путь к файлу с учениками в формате json'
        file = askopenfilename(title= title,
                              initialdir=getcwd())
        return file

    @staticmethod
    def get_info_from_json(file):
        """Десериализовать JSON."""
        with open(path.abspath(file), encoding='utf8') as file:
            try:
                data: dict = json.load(file)
                return data
            except FileNotFoundError as ex:
                print(ex)


    @staticmethod
    def _get_path_to_directory(title: str):
        """Получить директорию."""
        directory = askdirectory(title=title, initialdir=getcwd())
        return directory

    @staticmethod
    def write_data_in_csv(path, student_name, data):
        """Записать данные в CSV."""
        new_path = path + f'/{student_name}.csv'
        with open(new_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            for i in data:
                writer.writerow([i.name] + [i.average] + [i.final])
        return


class CalculatingGrades:
    """Класс для работы с оценками."""
    def __init__(self, grades_list: list):
        self.grades = grades_list

    def get_average(self):
        """ДПолучить среднее арифметическое оценок."""
        return round(mean(self.grades), 2)

    def sort_ascending(self):
        """Сортировка по возрастанию."""
        return sorted(self.grades)

    @staticmethod
    def reverse(func):
        def wrapper(self):
            return sorted(func(self), reverse=True)
        return wrapper

    @reverse
    def sort_descending(self):
        return self.grades  # Сортировка происходит через декоратор

    def get_final_grade(self):
        """Получить итоговую оценку."""
        if self.get_average() % 1 >= 0.5:
            return math.ceil(self.get_average())
        else:
            return math.floor(self.get_average())


class Student:
    """Обертка над экземпляром ученика."""
    def __init__(self, name: str):
        self.name = name
        self.disciplines = []

    def sort_disciplines_increment(self):
        """Сортировка по возрастанию."""
        return list(sorted(self.disciplines, key=lambda x: x.average))

    def sort_disciplines_decrement(self):
        """Сортировка по убыванию."""
        new_lst = []
        for i in self.sort_disciplines_increment():
            new_lst.insert(0, i)
        return new_lst


class Discipline:
    """Обертка над экземпляром предмета."""
    def __init__(self, discipline_name: str, grades: list):
        self.discipline_name = discipline_name
        self.grades = grades
        self.__calc = CalculatingGrades(grades)
        self.average = self.__calc.get_average()
        self.final_grade = self.__calc.get_final_grade()
        self.srt_ascend = self.__calc.sort_ascending()
        self.srt_descend = self.__calc.sort_descending()


class AnalyzeData:
    """Иницализация анализа и вывода данных."""
    def __init__(self):
        var_a = FileHandler._get_path_to_json()
        electronic_dicts = FileHandler.get_info_from_json(var_a)
        self.students = []
        for student in electronic_dicts.keys():
            new_student = Student(student)
            self.students.append(new_student)
            for disciplines in (
                    electronic_dicts)[student]:
                new_discipline = Discipline(disciplines['object'],
                                            disciplines['grades'])
                new_student.disciplines.append(new_discipline)
        for student in self.students:
            list_1 = student.sort_disciplines_increment()
            data_1 = []
            for discipline in list_1:
                data_scv = DataToCSV(discipline.discipline_name,
                                     discipline.average,
                                     discipline.final_grade)
                data_1.append(data_scv)
            list_2 = student.sort_disciplines_decrement()
            data_2 = []
            for discipline in list_2:
                data_scv = DataToCSV(discipline.discipline_name,
                                     discipline.average,
                                     discipline.final_grade)
                data_2.append(data_scv)
            path_1 = FileHandler._get_path_to_directory(
                'Путь к директории, в которую будут '
                'записаны файлы с сортировкой по возрастанию')
            FileHandler.write_data_in_csv(path_1, student.name, data_1)
            path_2 = FileHandler._get_path_to_directory(
                'Путь к директории, в которую будут '
                'записаны файлы с сортировкой по убыванию')
            FileHandler.write_data_in_csv(path_2, student.name, data_2)


class DataToCSV:
    """Обертка для записи в CSV."""
    def __init__(self, name, average, final):
        self.name = name
        self.average = average
        self.final = final


if __name__ == '__main__':
    analyze_data = AnalyzeData()
