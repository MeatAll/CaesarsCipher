import unittest

from lesson_11_1 import Alphabet

class TestAlphabet(unittest.TestCase):


    def test_get_ru_chars(self):
        language = 'ru'
        alphabet = Alphabet(language)
        it = alphabet.get_ru_chars()
        out_chars = alphabet.get_out_chars(it)
        expected_output = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.assertEqual(out_chars, expected_output)


    def test_get_en_chars(self):
        language = 'en'
        alphabet = Alphabet(language)
        it = alphabet.get_en_chars()
        out_chars = alphabet.get_out_chars(it)
        expected_output = 'abcdefghijklmnopqrstuvwxyz'
        print('adadadad')
        self.assertEqual(out_chars, expected_output)

    def test_invalid_language(self):
        with self.assertRaises(Exception) as context:
            Alphabet('fr')
        self.assertEqual(str(context.exception), 'Unknown language')

if __name__ == '__main__':
    unittest.main()