
class Alphabet:
    '''Класс, позволяет получить алфавит.'''
    def __init__(self, language):
        self.language = language
        alphabet_iterator: iter
        if language == "ru":
            alphabet_iterator = self.get_ru_chars()
        elif language == "en":
            alphabet_iterator = self.get_en_chars()
        else:
            raise Exception('Unknown language')
        alfabet = self.get_out_chars(alphabet_iterator)
        print(alfabet)


    @staticmethod
    def get_ru_chars():
        """Вывести русский алфавит."""
        it = iter(range(ord("а"), ord('я')+1))
        return it

    @staticmethod
    def get_en_chars():
        """Вывести английский алфавит."""
        it = iter(range(97, 123))
        return it

    def get_out_chars(self, alphabet_iterator: iter):
        alf: str = ''
        try:
            while True:
                alf = alf + (chr(next(alphabet_iterator)).encode().decode())
        except StopIteration:
            None
        return alf

if __name__ == '__main__':
    language = input('Выберите язык (ru/en): ')
    alphabet = Alphabet(language)


