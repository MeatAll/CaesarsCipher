import unittest

import lesson_7_1

class TestStringUtil(unittest.TestCase):
    phrases_to_test_list = ["Магнус не предавал!",
                            "здравствуйте, это канал об аниме?"
                            " -- Да. -- "
                            "Как мне пропатчить KDE2 под FreeBSD?",
                            "человек человеку волк, а зомби зомби зомби."
                            ]

    def test_add_begin(self):
        input_str = self.phrases_to_test_list[1]
        expected_output = self.phrases_to_test_list[1].capitalize()
        self.assertEqual(lesson_7_1.add_begin(input_str), expected_output)

    def test_replace_symbol(self):
        input_str = self.phrases_to_test_list[0]
        input_char = '*'
        expected_output = "Магнус*не*предавал!"
        self.assertEqual(lesson_7_1.replace_symbol(input_str, input_char), expected_output)

    def test_update_string(self):
        input_str = self.phrases_to_test_list[2]
        input_char = '*'
        expected_output = 'Человек*человеку*волк,*а*зомби*зомби*зомби.'
        self.assertEqual(lesson_7_1.update_string(input_str, input_char), expected_output)


if __name__ == '__main__':
    unittest.main()