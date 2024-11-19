import unittest

from lesson_11_3 import create_generator, create_generator_v2

class TestGeneratorFunctions(unittest.TestCase):

    def test_create_generator(self):
        expected_output = {2: [1, 1, 1], 3: [2, 3, 4], 4: [4, 9, 16]}
        self.assertEqual(create_generator(2, 4), expected_output)

    def test_create_generator_v2(self):
        expected_output_v2 = {2: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                              3: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                              4: [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]}
        self.assertEqual(create_generator_v2(2, 4), expected_output_v2)

if __name__ == '__main__':
    unittest.main()