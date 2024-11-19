import json
import csv
import os
from typing import List, Dict, Any


class CalculatingGrades:
    def __init__(self, grades: List[float]):
        self.grades = grades

    def get_average(self) -> float:
        average = sum(self.grades) / len(self.grades)
        return round(average, 2)

    def sort_ascending(self) -> List[float]:
        return sorted(self.grades)

    @staticmethod
    def reverse(func):
        def wrapper(self):
            return sorted(func(self), reverse=True)

        return wrapper

    @reverse
    def sort_descending(self) -> List[float]:
        return self.grades  # Сортировка происходит через декоратор

    def get_final_grade(self) -> int:
        average = self.get_average()
        if average % 1 >= 0.5:
            return int(average) + 1
        return int(average)


class FileHandler:
    def get_info_from_json(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write_data_in_csv(self, file_path: str, data: List[Dict[str, Any]]):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Записываем заголовки
            writer.writerow(["Предмет", "Средняя оценка", "Итоговая оценка"])
            for row in data:
                writer.writerow([row['subject'], row['average'], row['final']])


def main(json_path: str, ascending_path: str, descending_path: str):
    file_handler = FileHandler()
    students_data = file_handler.get_info_from_json(json_path)

    # Создаём списки для хранения результатов
    results = []

    for student in students_data:
        for subject, grades in student['subjects'].items():
            calc = CalculatingGrades(grades)
            average_grade = calc.get_average()
            final_grade = calc.get_final_grade()
            results.append({
                'subject': subject,
                'average': average_grade,
                'final': final_grade
            })

    # Сортировка по возрастанию
    sorted_results_asc = sorted(results, key=lambda x: x['average'])
    # Сортировка по убыванию (используя декоратор)
    sorted_results_desc = sorted(results, key=lambda x: x['average'], reverse=True)

    # Запись в CSV
    student_name = students_data[0]['name']  # Предположим, что имя одно для всех.
    file_handler.write_data_in_csv(os.path.join(ascending_path, f"{student_name}.csv"), sorted_results_asc)
    file_handler.write_data_in_csv(os.path.join(descending_path, f"{student_name}.csv"), sorted_results_desc)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 4:
        print("Usage: script.py <json_path> <ascending_path> <descending_path>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    ascending_output_path = sys.argv[2]
    descending_output_path = sys.argv[3]

    main(json_file_path, ascending_output_path, descending_output_path)