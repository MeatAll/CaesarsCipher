import enum


class Priority(enum.IntEnum):
    """Возможныe варианты приоритета задачи."""

    low = 0,
    """Низкий приоритет задачи."""

    normal = 1,
    """Нормальный приоритет задачи."""

    high = 2
    """Высокий приоритет задачи."""


class Task:
    """Класс - обертка для представления задачи."""

    def __init__(self,
                 name: str,
                 description: str = "",
                 priority: int = Priority(1)):
        """Задание атрибутов класса Task.

        Args:
            name: Имя задачи.
            description: Описание задачи (по умол. пустая строка).
            priority: Приоритет задачи (по умол. нормальный).
        """
        self.name = name
        self.description = description
        try:
            self.priority = Priority(priority)
        except IndexError:
            self.priority = Priority(1)

    def update_name(self, new_name: str):
        """
        Обновление имени задачи.

        Args:
            new_name: Новое имя задачи.
        """
        self.name = new_name

    def update_description(self, new_description: str):
        """Обновление описания.

        Args:
            new_description: Новое описание задачи.
        """
        self.description = new_description

    def update_priority(self, new_priority: int):
        """Обновление приоритета.

        Args:
            new_priority: Новый приоритет.
        """
        try:
            self.priority = Priority(new_priority)
        except IndexError:
            self.priority = Priority(1)

    def delete_description(self):
        """
        Удаление описания задачи.
        Удаление означает замену описания задачи на пустую строку.
        """
        self.description = ""

    def delete_priority(self):
        """
        Удаление приоритета задачи.
        Удаление означает замену приоритета задачи
        на приоритет по умолчанию, то есть на 1.
        """
        self.priority = Priority(1)


class Todo:
    """Класс описывает список задач."""
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        """Добавить задачу в список задач.

        Args:
            task: Объект Task.
        """
        self.tasks.append(task)

    def del_task(self, task_index: int):
        """Удалить задачу из списка задач.

        Args:
            task_index: Индекс задачи в списке, которую нужно удалить.
        """
        try:
            self.tasks.remove(task_index)
        except IndexError:
            self.print_error(task_index)

    def sort_priority(self, is_incr_priority: bool = False) -> list[Task]:
        """Сортировать список по приоритету задачи.
        По умолчанию аргумент имеет значение сортировки по возрастанию.

        Args:
            is_incr_priority: Порядок сортировки
            (по возрастанию приоритета или по убыванию).

        Returns:
            Отсортированный список задач.
        """
        temp_tasks = sorted(self.tasks, key=lambda x: getattr(x, "priority"))
        if is_incr_priority is False:
            return temp_tasks
        if is_incr_priority is True:
            return reversed(temp_tasks)

    def get_tasks(self, tasks_num: int) -> list[Task]:
        """Получить список задач.

        Args:
            tasks_num: Количество задач для получения.

        Returns:
            Список задач в том количестве, в котором указано в аргументе.
        """

        try:
            if tasks_num < 1:
                raise IndexError('Неверный аргумент')
        except IndexError as ex:
            print(ex)
        except Exception:
            print('Unknown error')
        if tasks_num <= len(self.tasks):
            return self.tasks[0:tasks_num]
        else:
            self.__print_error(tasks_num)

    def pop_task(self) -> Task:
        """Возвращает первую задачу из списка.

        Returns:
            Первая задача.
        """
        try:
            return self.tasks[0]
        except IndexError:
            self.__print_error(0)

    def __print_error(self, index: int):
        """
        Выводит несуществующий индекс при обращении к списку задач.

        Args:
            index: Индекс задачи.
        """
        print(f"Index must be less than {index}")


if __name__ == "__main__":
    task1: Task = Task("Умыться")
    task2: Task = Task("Почистить зубы", "Купил новую щетку", 0)
    task3: Task = Task("Позавтракать", priority=2)
    task4: Task = Task("Сходить на дейлик", "В 9:30")
    task5: Task = Task("Налить чашечку кофе", priority=0)

    todo: Todo = Todo()
    print(todo.get_tasks(-1))

    """
    todo.add_task(task1)
    todo.add_task(task2)
    todo.add_task(task3)
    todo.add_task(task4)
    todo.add_task(task5)

    for task in todo.get_tasks(5):
        print(task.name)
    print()

    for task in todo.sort_priority():
        print(task.name, task.priority)
    print()

    for task in todo.sort_priority(True):
        print(task.name, task.priority)
    print()

    for task in todo.get_tasks(2):
        print(task.name)
    print()

    print(todo.pop_task().name)

    todo.get_tasks(6)"""
