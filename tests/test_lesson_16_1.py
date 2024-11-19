import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lesson_16_1


class TestCaesarsCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = lesson_16_1.CaesarsCipher()

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt("HELLO", 3), "KHOOR")
        self.assertEqual(self.cipher.encrypt("hello", 3), "khoor")

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt("KHOOR", 3), "HELLO")
        self.assertEqual(self.cipher.decrypt("khoor", 3), "hello")
        self.assertEqual(self.cipher.decrypt("456", 3), "123")

    def test_encrypt_decrypt_consistency(self):
        message = "Hello World 123!?"
        key = 5
        encrypted = self.cipher.encrypt(message, key)
        decrypted = self.cipher.decrypt(encrypted, key)
        self.assertEqual(decrypted, message)

    def test_encrypt_with_invalid_character(self):
        self.assertEqual(self.cipher.encrypt("Hello@World", 5), "Mjqqt%Btwqi")

    def test_decrypt_with_invalid_character(self):
        self.assertEqual(self.cipher.decrypt("Mjqqt%Tzywj", 5), "Hello@World")


if __name__ == "__main__":
    unittest.main()