class User:
    """
    Класс представляет собой человека.
    """
    def __init__(self,
                 name: str,
                 age: int,
                 male: str,
                 lease: str = "",
                 key: bool = False):
        """Устанавливает атрибуты для объекта User.

        Args:
            name: Имя.
            age: Возраст.
            male: Пол.
            lease: Контракт (по умол. пустая строка).
            key: Ключ (по умол. ключа нет).
        """
        self.name = name
        self.age = age
        self.male = male
        self.lease = lease
        self.key = key

    def terminate_lease(self):
        """Расторжение договора."""
        self.lease = ""

    def subscribe_lease(self, text: str, sign: str = ""):
        """Подписание контракта.

        Args:
            text: Текст договора.
            sign: Подпись.
        """
        self.lease = text + " " + sign

    def increase_age(self):
        """Увеличение возраста."""
        self.age += 1

    def add_key(self):
        """Добавление ключа пользователю."""
        self.key = True


class Home:
    """
    Класс представляет собой дом.
    """
    def __init__(self,
                 count_rooms: int,
                 basement: str = "black",
                 heating: bool = True):
        """
        Args:
            count_rooms: Количество комнат.
            basement: Фундамент (по умол. black).
            heating: Отопление (по умол. есть).
            is_unlock: Открыт ли дом (по умол. True).
            bed: Количество кроватей (по умол. 3).
            users: Список пользователей (по умол. пустой).
        """
        self.count_rooms = count_rooms
        self.basement = basement
        self.heating = heating
        self.is_unlock = True
        self.bed = 3
        self.users = []

    def close(self):
        """Закрывает дом на ключ."""
        self.is_unlock = False

    def open(self):
        """Открывает дом"""
        self.is_unlock = True

    def add_room(self):
        """Добавление комнаты."""
        self.count_rooms += 1

    def add_beds(self, count_bed: int):
        """Добавляет кровати.

        Args:
            count_bed: Количество кроватей.
        """
        self.bed += count_bed

    def add_user(self, user: User):
        """Добавляет жителя дома.

        Args:
            user: Житель.
        """
        self.users.append(user)

    def sort_users(self, key: str) -> list[User]:
        """Сортирует список жителей.

        Args:
            key: Ключ, по которому сортируется список жителей.

        Returns:
            Отсортированный список жителей.
        """
        try:
            return sorted(self.users, key=lambda x: getattr(x, key))
        except AttributeError:
            raise AttributeError(f"Атрибута {key} не существует.")
        except Exception as ex:
            raise Exception(f"Unknown error: {ex}")


if __name__ == "__main__":
    wife: User = User("Анна", 30, "Ж")
    husband: User = User("Олег", 30, "М")
    girl: User = User("Катя", 16, "Ж")
    man: User = User("Евлампий", 8, "М")

    # подписание договора
    husband.subscribe_lease("Договор", "ОГ")
    wife.subscribe_lease("", "АА")

    # выдача ключей
    husband.add_key()
    wife.add_key()
    girl.add_key()
    man.add_key()

    # строим дом
    my_home: Home = Home(3)
    my_home.open()
    my_home.add_user(husband)
    my_home.add_user(wife)
    my_home.add_user(girl)
    my_home.add_user(man)

    for user in my_home.sort_users("age"):
        print(user.name, user.age, user.male)
