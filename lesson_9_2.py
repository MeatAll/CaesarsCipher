import datetime

from dateutil.relativedelta import relativedelta
import random


class Card:
    """Объект - дебетовая карта."""
    def __init__(self,
                 user: str,
                 payment_system: str,
                 code: str):
        """Регистрация нового абонента.

        Args:
            user: ФИО.
            payment_system: Платежная система.
            code: Pin-код.
        """
        self.user = user
        self.payment_system = payment_system
        self.__number = self.__generate_card_number()
        self.__validity_period: datetime = (datetime.date.today() +
                                            relativedelta(years=3))
        self.__code_cv = self.__generate_ccv()
        self.__code = code
        self.is_blocked = False

    @staticmethod
    def __generate_card_number() -> str:
        """Сгенерировать номер карты.

        Returns:
            Новый уникальный 16-значный номер.
        """
        def generate_number_part():
            num_part: str = ''
            i_int = 0
            while i_int < 4:
                num = random.randint(0, 9)
                num_part = num_part + str(num)
                i_int = i_int + 1
            return num_part
        car_num = ''
        j_int = 0
        while j_int < 4:
            if car_num == '':
                car_num = generate_number_part()
            else:
                car_num = car_num + ' ' + generate_number_part()
            j_int = j_int + 1
        return car_num

    @staticmethod
    def __generate_ccv() -> str:
        """Сгенерировать ccv-код

        Returns:
            CCV-код.
        """
        int_i = 0
        ccv: str = ''
        while int_i < 3:
            ccv_part = random.randint(0, 9)
            ccv = ccv + str(ccv_part)
            int_i = int_i + 1
        return ccv

    def get_number(self):
        """Получить общедоступный номер карты.

        Returns:
            Номер со скрытыми знаками.
        """
        var_len = len(self.__number)
        return str('***' + self.__number[(var_len - 4): var_len])

    def get_validity_period(self) -> str:
        """Получить срок действия карты.

        Returns:
            Дата окончания действия.
        """
        return (str(self.__validity_period.year)[2:4] + '/'
                + str(self.__validity_period.month))

    def get_cv(self) -> str:
        """Получить CCV-код для публикации.

        Returns:
            CCV в скрытом формате.
        """
        return '***'

    def get_payment_system(self):
        """Узнать платежную систему карты.

        Returns:
            Платежная система.
        """
        return self.payment_system

    def block(self):
        """Заблокировать карту"""
        self.is_blocked = True

    def __str__(self):
        """Вывод владельца.

        Returns:
            Владелец в формате для публикации.
        """
        return 'Данная карта принадлежит: ' + self.user


if __name__ == '__main__':
    card = Card("Иванов И.И.", "МИР", "1234")
    print(card.is_blocked)
    print(card)
    print(card.user)
    print(card.get_payment_system())
    print(card.get_number())
    print(card.get_validity_period())
    print(card.get_cv())
    card.block()
    print(card.is_blocked)
    try:
        print(card.__number)
    except Exception as ex:
        print(ex)
