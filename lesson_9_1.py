import random


class Animal:
    """Класс, представляющий объект типа Animal"""

    animals = []

    def __init__(self,
                 name: str):
        """Базовый конструктор, для создания экземпляра типа Animal.

        Args:
            name: Имя животного.
        """
        self.name = name
        self.id = self.__generate_id()
        self.animals.append(self)

    @staticmethod
    def __generate_id() -> int:
        """Генрация уникального Id для экзмпляра Animal.

        Returns:
            Уникальный Id.
        """
        return random.randint(10000, 100000)

    @classmethod
    def first_animal(cls):
        """Получить первое животное из animals[], если оно есть.

        Returns:
            Экземпляр Animal.
        """
        try:
            return cls.animals[0]
        except IndexError:
            print('No animals')

    @classmethod
    def last_animal(cls):
        """Получить последнее животное из animals[], если оно есть.

        Returns:
            Экземпляр Animal.
        """
        try:
            return cls.animals[len(cls.animals)-1]
        except IndexError:
            print('No animals')

    @classmethod
    def count_animals(cls) -> int:
        """Количество животных.

        Returns:
            Количество экземпляров в animals[].
        """
        return len(cls.animals)

    @staticmethod
    def get_rules() -> str:
        """Получить правила по уходу за животным.

        Returns:
            Список правил.
        """
        RULES = [
            'Посещение ветеринарного врача.',
            'Прививки.',
            'Правильные идентификационные данные.',
            'Стерилизация/кастрация.',
            'Здоровое питание домашних животных.',
            'Уход в домашних условиях.',
            'Комфортное жильё.',
            'Дрессировка и социализация.',
            'Соблюдение правил во время прогулки.',
            'Время для безопасных игр.'
        ]
        rules_len: int = len(RULES)
        rules_count: int = random.randint(1, rules_len)
        rules_strings = []
        int_i = 1
        while int_i <= rules_count:
            rule_number = random.randint(1, rules_len)
            if (RULES[rule_number-1] in rules_strings) is False:
                rules_strings.append(RULES[rule_number - 1])
            int_i = int_i + 1
        out_rules: str = None
        rule_index: int = 1
        rule_t: str = 'Правило '
        for rul in rules_strings:
            if out_rules is None:
                out_rules = rule_t + str(rule_index) + '. ' + rul
            else:
                out_rules = (out_rules + '\n' +
                             rule_t + str(rule_index) + '. ' + rul)
            rule_index = rule_index + 1
        return out_rules

    @staticmethod
    def get_animal_info(animal_view_name: str):
        """Информация о животном.

        Args:
            animal_view_name: Название животного.

        Returns:
            Поведение животного.
        """
        int_i: int = random.randint(1, 5)
        match int_i:
            case 1:
                return (f'{animal_view_name} с радостью обглодает '
                        f'кости своего владельца.').capitalize()
            case 2:
                return (f'{animal_view_name} может переварить '
                        f'взрослого человека за одну неделю.').capitalize()
            case 3:
                return (f'{animal_view_name} обожает откармливать '
                        f'своих детенышей мясом хозяина.').capitalize()
            case 4:
                return (f'{animal_view_name} заставляет своего '
                        f'владельца писать на').capitalize() + ' PHP.'
            case 5:
                return (f'{animal_view_name} покупает курсы по '
                        f'программированию '.capitalize() +
                        'на GeekBrains и SkillFactory.')


if __name__ == '__main__':
    animal = Animal('Ослик')
    animal = Animal('Кролик')
    animal = Animal('Белочка')
    print(Animal.first_animal().name, Animal.first_animal().id)
    print(Animal.last_animal().name, Animal.last_animal().id)
    print(Animal.count_animals())
    print(Animal.get_rules())
    print(animal.get_animal_info('Кролик'))
