import random

from operator import contains


class BasePerson:
    """Базовый класс, представляющий персонажа."""

    def __init__(self, max_hitpoints: int, base_damage: int):
        self._max_hitpoints = max_hitpoints
        self._hitpoints = self._max_hitpoints
        self._experience = 0
        self._base_damage = base_damage
        self._ability_1_cooldown = 0
        self._ability_2_cooldown = 0
        self._level = 1

    def attack(self) -> int:
        """Базовая атака."""
        return self._base_damage

    def ability(self):
        """Абилка 1."""
        pass

    def ability_2(self):
        """Абилка 2."""
        pass

    @property
    def hitpoints(self):
        """Получить текущие хп."""
        return self._hitpoints

    def damage(self, damage: int):
        """Получить урон."""
        self._hitpoints = self._hitpoints - damage
        print(f'  Получил {damage} урона и у него '
              f'осталось {self._hitpoints} хп!')
        if self._hitpoints > 0:
            return False
        if self._hitpoints <= 0:
            return True

    def add_experience(self, exp: int):
        """Добавить опыт."""
        print('  ' + self.__repr__() + ' получает ' + str(exp) + ' опыта')
        self._experience = self._experience + exp
        if self._experience >= 50:
            self.__add_level()
        print(f'  До следующего уровня еще {50 - self._experience}')

    def __add_level(self):
        """Поднять уровень"""
        self._level = self._level + 1
        self._max_hitpoints = self._max_hitpoints + 5
        self._hitpoints = self._max_hitpoints
        self._experience = 50 - self._experience
        print(("  " + type(self).__name__ + ' получает новый уровень!'))

    def set_ability_1_cooldown(self):
        """Вызывается после использоввания абилки 1.
        Выставляет кулдаун в 2 хода."""
        self._ability_1_cooldown = 2

    def tick_ability_1_cooldown(self):
        """Вызывается каждый новый ход.
        Понижает счетчик кулдауна абилки."""
        if self._ability_1_cooldown > 0:
            self._ability_1_cooldown = self._ability_1_cooldown - 1

    def set_ability_2_cooldown(self):
        """Вызывается после использоввания абилки 2.
        Выставляет кулдаун в 2 хода."""
        self._ability_2_cooldown = 2

    def tick_ability_2_cooldown(self):
        """Вызывается каждый новый ход. Понижает счетчик кулдауна абилки."""
        if self._ability_2_cooldown > 0:
            self._ability_2_cooldown = self._ability_2_cooldown - 1

    def choose_attack(self):
        """Выбор и вызов атаки или абилки."""
        if self._hitpoints <= int(self._max_hitpoints * 0.5):
            if self._ability_2_cooldown == 0:
                if self.ability_2() is not None:
                    self.set_ability_2_cooldown()
                    return self.ability_2()
            if self._ability_1_cooldown == 0:
                self.set_ability_1_cooldown()
                return self.ability()
        if self._hitpoints <= int(self._max_hitpoints * 0.7):
            if self._ability_1_cooldown == 0:
                self.set_ability_1_cooldown()
                return self.ability()
            if self._ability_2_cooldown == 0:
                if self.ability_2() is not None:
                    self.set_ability_2_cooldown()
                    return self.ability_2()
        print(f'  {type(self).__name__} совершает ход "Руби и кромсай"')
        return self.attack()

    def __repr__(self):
        """Получить имя персонажа в игровом формате."""
        return (type(self).__name__ +
                (f'(HP:{self._hitpoints}/'
                 f'{self._max_hitpoints} LVL:{self._level})'))


class Wizard(BasePerson):
    """Класс волшебник."""

    def __init__(self, max_hitpoints: int, base_damage: int):
        BasePerson.__init__(self, max_hitpoints, base_damage)
        self._max_hitpoints = max_hitpoints
        self._hitpoints = self._max_hitpoints
        self._experience = 0
        self._base_damage = base_damage
        self._ability_1_cooldown = 0
        self._level = 1

    def ability(self):
        """Абилка 1 - вихрь."""
        return self._vortex()

    def ability_2(self):
        """Абилка 2 - отсутсвует."""
        return None

    def _vortex(self):
        """Механика абилки 'вихрь'"""
        print(f'  {type(self).__name__} вызывает магический вихрь')
        return int(self._base_damage * 1.5)


class Warrior(BasePerson):
    """Класс воин."""

    def __init__(self, max_hitpoints: int, base_damage: int):
        BasePerson.__init__(self, max_hitpoints, base_damage)
        self._max_hitpoints = max_hitpoints
        self._hitpoints = self._max_hitpoints
        self._experience = 0
        self._base_damage = base_damage
        self._ability_1_cooldown = 0
        self._level = 1

    def _rage(self):
        """Механика абилки 'ярость'."""
        print(f'  {type(self).__name__} впадает в ярость')
        self._hitpoints = int(float(self._hitpoints / 100) * 30.0
                              + self._hitpoints)
        return self._base_damage * 2

    def ability(self):
        """Абилка 1 - ярость."""
        return self._rage()

    def ability_2(self):
        """Абилка 2 - отсутсвует."""
        return None


class Rogue(BasePerson):
    """Класс вор."""

    def __init__(self, max_hitpoints: int, base_damage: int):
        BasePerson.__init__(self, max_hitpoints, base_damage)
        self._max_hitpoints = max_hitpoints
        self._hitpoints = self._max_hitpoints
        self._experience = 0
        self._base_damage = base_damage
        self._ability_1_cooldown = 0
        self._ability_2_cooldown = 0
        self._level = 1

    def _multishot(self):
        """Механика абилки 'мультивыстрел.'"""
        print(f'  {type(self).__name__} выпускает град стрел')
        return self._base_damage * 5

    def ability(self):
        """Абилка 1 - выстрел."""
        return self._multishot()

    def ability_2(self):
        """Абилка 2 - отстутсвует."""
        return None


class FireWizard(Wizard):
    """Класс огненный маг."""

    def __init__(self, max_hitpoints: int, base_damage: int):
        Wizard.__init__(self, max_hitpoints, base_damage)
        self._max_hitpoints = max_hitpoints
        self._hitpoints = self._max_hitpoints
        self._experience = 0
        self._base_damage = base_damage
        self._ability_1_cooldown = 0
        self._ability_2_cooldown = 0
        self._level = 1

    def _fire_vortex(self):
        """Механика абилки 'огненный вихрь'."""
        print(f'  {type(self).__name__} вызывает огенный вихрь')
        return int(self._base_damage * 2)

    def ability(self):
        """Абилка 1 - огненный вихрь."""
        return self._fire_vortex()

    def ability_2(self):
        """Абилка 1 - отсутсвует."""
        return None


class WaterWizard(Wizard):
    """Класс водяной маг."""

    def __init__(self, max_hitpoints: int, base_damage: int):
        Wizard.__init__(self, max_hitpoints, base_damage)
        self._max_hitpoints = max_hitpoints
        self._hitpoints = self._max_hitpoints
        self._experience = 0
        self._base_damage = base_damage
        self._ability_1_cooldown = 0
        self._ability_2_cooldown = 0
        self._level = 1

    def _tsunami(self):
        """Механика обилки 'цунами'."""
        print(f'  {type(self).__name__} вызывает цунами')
        return int(self._base_damage * 1.7)

    def ability(self):
        """Абилка 1 - цунами."""
        return self._vortex()

    def ability_2(self):
        """Абилка 2 - отсутсвует."""
        return self._tsunami()


class Samurai(Warrior):
    """Класс самурай"""

    def __init__(self, max_hitpoints: int, base_damage: int):
        Warrior.__init__(self, max_hitpoints, base_damage)
        self._max_hitpoints = max_hitpoints
        self._hitpoints = self._max_hitpoints
        self._experience = 0
        self._base_damage = base_damage
        self._ability_1_cooldown = 0
        self._ability_2_cooldown = 0
        self._level = 1

    def _regeneration(self):
        """Механика абилки 'регенарция'."""
        temp_points = int(self._hitpoints * 0.8) + self._hitpoints
        if temp_points > self._max_hitpoints:
            self._max_hitpoints = self._max_hitpoints
        else:
            self._hitpoints = int(self._hitpoints * 0.8) + self._hitpoints
        print(f'  {type(self).__name__} впадает в транс и залечивает раны')
        return int(self._base_damage * 0.9)

    def ability(self):
        """Абилка 1 - регенерация."""
        return self._rage()

    def ability_2(self):
        """Абилка 1 - отсутсвует."""
        return self._regeneration()


class Tabletop:
    """Класс для имитации игрового стола."""
    chars = []
    move_queue = []
    active_char: int
    attacked_char: int

    @classmethod
    def start_game(cls):
        """Запуск игры."""
        cls.create_chars()
        cls.create_queue()
        int_i = 1
        while len(cls.chars) != 1:
            print('Ход ' + str(int_i))
            cls.increment_ability_cooldown()
            int_i = int_i + 1
            cls.move_step()
        else:
            print('Игра окончена')
            print(f'{cls.get_name_by_int(0)} побеждает!')

    @classmethod
    def increment_ability_cooldown(cls):
        """Уменьшение счетчика кулдаунов абилок у персонажей."""
        for char in cls.chars:
            char.tick_ability_1_cooldown()
            char.tick_ability_2_cooldown()

    @staticmethod
    def get_name_by_type(tp: BasePerson):
        """Получить имя персонажа по экземпляру."""
        return tp.__repr__()

    @classmethod
    def get_name_by_int(cls, char: int):
        """Получить имя персонажа по индексу."""
        return cls.chars[char].__repr__()

    @classmethod
    def move_step(cls):
        """Большой ход. Описывает ход всех игровых персонажей."""
        for ch_queue in cls.move_queue:
            try:
                active_char = ch_queue
                cls.active_char = active_char
                attacked_char = cls.choose_attacked_char()
                cls.attacked_char = attacked_char
                cls.move_tick()
            except Exception:
                None

    @classmethod
    def move_tick(cls):
        """Малый ход. Описывает взаимодействие двух персонажей."""
        act_char = cls.active_char
        attacked_char = cls.attacked_char
        print(f'Персонаж {cls.get_name_by_int(act_char)} атакует '
              f'{cls.get_name_by_int(attacked_char)}:')
        damage_in_d10 = cls.try_attack()
        if damage_in_d10 != 0:
            attack = cls.chars[act_char].choose_attack()
            damage = attack + damage_in_d10
            print('  Наносит ' + str(damage) + ' урона' +
                  f' ({attack} + {damage_in_d10})')
            cls.chars[act_char].add_experience(15)
            is_dead: bool = cls.char_damage(damage)
            if is_dead is True:
                cls.char_dead()
        else:
            print('  Провал!\n  Завершает ход')

    @classmethod
    def create_queue(cls):
        """Создать рандомную очередь хождения персонажей."""

        def get_queue():
            queue = random.randint(0, (len(cls.chars)) - 1)
            return queue

        int_i = len(cls.chars)
        while int_i > 0:
            var_q = get_queue()
            while (contains(cls.move_queue, var_q)) is True:
                var_q = get_queue()
            cls.move_queue.append(var_q)
            int_i = int_i - 1

    @classmethod
    def char_dead(cls):
        """Метод описывает смерть персонажа."""
        print(f'{cls.get_name_by_int(cls.attacked_char)} умирает')
        cls.chars.remove(cls.chars[cls.attacked_char])
        print(f'Осталось {len(cls.chars)} бойцов')

    @classmethod
    def create_chars(cls):
        """Создание списка рандомных персонажей."""
        chars_count = random.randint(2, 4)
        while chars_count != 0:
            ch = cls.get_char()
            cls.chars.append(ch)
            print(f'Персонаж {cls.get_name_by_type(ch)} пришёл на битву.')
            chars_count = chars_count - 1

    @staticmethod
    def get_char():
        """Получить новго рандомного персонажа."""
        int_i = random.randint(2, 6)
        char_type: type
        match int_i:
            case 1:
                char_type = Wizard(50, 10.0)
                return char_type
            case 2:
                char_type = Warrior(80, 7, )
                return char_type
            case 3:
                char_type = Rogue(60, 6)
                return char_type
            case 4:
                char_type = FireWizard(45, 12)
                return char_type
            case 5:
                char_type = WaterWizard(40, 14)
                return char_type
            case 6:
                char_type = Samurai(70, 11)
                return char_type

    @staticmethod
    def roll_dice_d6():
        """Бросок куба д6."""
        int_i = random.randint(1, 6)
        print(f'  Выбрасывает {int_i} на d6')
        return int_i

    @staticmethod
    def roll_dice_d10():
        """Бросок куба д10."""
        int_i = random.randint(1, 10)
        print(f'  Выбрасывает {int_i} на d10')
        return int_i

    @classmethod
    def char_damage(cls, damage: int):
        """Описывает попытку персонажа защитится."""
        attacked_char: BasePerson = cls.chars[cls.attacked_char]
        print(f'{cls.get_name_by_type(attacked_char)} защищается:')
        d6 = cls.roll_dice_d6()
        match d6:
            case 1:
                print('  Провал! Получает х1.5 урона')
                damage = int(damage * 1.5)
                attacked_char.add_experience(5)
                return attacked_char.damage(damage)
            case 6:
                print('  Успех! Получает х0.5 урона')
                damage = int(damage * 0.5)
                return attacked_char.damage(damage)
            case _:
                return attacked_char.damage(damage)

    @classmethod
    def try_attack(cls):
        """Персонаж пытается провести атаку."""
        int_i = cls.roll_dice_d6()
        if int_i > 3:
            return cls.roll_dice_d10()
        else:
            return 0

    @classmethod
    def choose_active_char(cls) -> int:
        """Рандомный выбор активного персонажа."""
        act_char = random.randint(0, (len(cls.chars) - 1))
        return act_char

    @classmethod
    def choose_attacked_char(cls):
        """Выбор рандомного атакуемого персонажа."""
        active_char = cls.active_char
        attacked_char = random.randint(0, (len(cls.chars)) - 1)
        if attacked_char == active_char:
            while attacked_char == active_char:
                attacked_char = random.randint(0, (len(cls.chars)) - 1)
        return attacked_char


if __name__ == '__main__':
    Tabletop.start_game()
