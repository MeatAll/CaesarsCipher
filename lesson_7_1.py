var_string: str = input('Введите строку:\n\t')
"""str: Строка, в которой пробелы будут заменены на
указанный пользователем символ.
"""


var_character: str = input('Введите символ:\n\t')
"""str: Символ, выступающий разделителем."""


def add_begin(v_string: str) -> str:
    """Возвращает строку, изменив регистр первого символа на заглавный.

    Args:
        v_string: Исходная строка.

    Returns:
        Отформатированная строка.
    """
    return v_string.capitalize()


def replace_symbol(v_string: str, v_char: str) -> str:
    """Заменить пробелы в строке на символ.

    Args:
        v_string: Исходная строка.
        v_char: Символ, на который будет заменён пробел.

    Returns:
        Отформатированная строка.
    """
    return v_string.replace(' ', v_char)


def update_string(var_str: str, var_char: str):
    """В фразе заменить пробелы на символ.
    Сделать первую букву заглавной.
    Вывести результат в консоль.

    Args:
        var_str: Исходная строка.
        var_char: Символ, который выступает разделителем.
    """
    temp_string = add_begin(var_str)
    print(replace_symbol(temp_string, var_char))


update_string(var_string, var_character)
