class Gemstone:
    """Клаас-обертка типа драгоценный камень."""
    def __init__(self, name: str, carat: float):
        """Базовый конструктор.

        Args:
            name: Название камня.
            carat: Вес камня в каратах.
        """
        self._name = name
        self._carat = carat

    @property
    def name(self) -> str:
        """Геттер атрибута.

        Returns:
            Название камня.
        """
        return self._name

    @name.setter
    def name(self, new_name: str):
        """Задать название каминя."""
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError('Uncorrected type')

    @property
    def carat(self) -> float:
        """Геттер атрибута.

        Returns:
            object: Вес камня в каратах.
        """
        return self._carat

    @carat.setter
    def carat(self, new_carat: int):
        """Задать вес камня в каратах"""
        if isinstance(new_carat, int):
            self._carat = new_carat
        else:
            raise ValueError('Uncorrected type')


class Diamond(Gemstone):
    """Клаас-обертка типа алмаз."""
    def __init__(self, name: str, carat: float):
        """Базовый конструктор.

        Args:
            name: Название камня.
            carat: Вес в каратах.
        """
        Gemstone.__init__(self, name, carat)
        self._name = name
        self._carat = carat

    def get_info(self) -> str:
        """Краткая информация о камне.

        Returns:
            Информация на Олбанском.
        """
        gem_descr = (f'{self._name} эта харошый и '
                     f'кросивый камишек аж на {self.carat} корат!')
        return gem_descr.capitalize()


class Emerald(Gemstone):
    """Клаас-обертка типа изумруд."""
    def __init__(self, name: str, carat: float, durability: int):
        """Базовый конструктор.

        Args:
            name: Название камня.
            carat: Вес в каратах.
            durability: Долговечность.
        """
        Gemstone.__init__(self, name, carat)
        self._name = name
        self._carat = carat
        self._durability = durability

    @property
    def durability(self) -> int:
        """Геттер атрибута.

        Returns:
            Долговечность камня.
        """
        return self._durability

    @durability.setter
    def durability(self, new_durability):
        """Задает долговечность новую долговечность камня.

        Args:
            new_durability: Новая долговечность.
        """
        self._durability = new_durability


class Tourmaline(Emerald):
    """Клаас-обертка типа турмалин."""
    def __init__(self, name: str, carat: float, durability: int, color: str):
        """Базовый конструктор.

        Args:
            name: Название камня.
            carat: Вес в каратах.
            durability: Долговечность.
            color: Цвет.
        """
        Emerald.__init__(self, name, carat, durability)
        self._name = name
        self._carat = carat
        self._durability = durability
        self._color = color

    @property
    def color(self) -> str:
        """Геттер атрибута.

        Returns:
            Цвет камня.
        """
        return self._color


if __name__ == '__main__':
    gemstone = Gemstone('Сапфир', 1)
    diamond = Diamond('Алмаз', 2)
    emerald = Emerald('Изумруд', 1.5, 20)
    tourmaline = Tourmaline('Турмалин', 3, 40, 'red')

    print(gemstone.name, gemstone.carat)
    gemstone.name = 'Аметист'
    print(gemstone.name, gemstone.carat)

    print(diamond.name, diamond.carat)
    print(diamond.get_info())

    emerald.durability = 25
    print(emerald.name, emerald.carat, emerald.durability)

    print(tourmaline.name, tourmaline.carat,
          tourmaline.durability, tourmaline.color)
    try:
        tourmaline.color = 'black'
    except AttributeError as ex:
        print(ex)
