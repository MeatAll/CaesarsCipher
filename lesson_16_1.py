import enchant

class CaesarsCipher:
    """Класс для шифрования и дешифрования
    сообщений с использованием шифра Цезаря."""

    def __init__(self):
        self.coding_symbols = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                               "abcdefghijklmnopqrstuvwxyz"
                               "1234567890 !?.")

    def decrypt(self, message: str, key: int) -> str:
        """Расшифровывание с помощью шифра Цезаря.

        Args:
            message: Сообщение для расшифровывания.
            key: Ключ для расшифровывания.

        Returns:
            object: Расшифрованное сообщение.
        """
        decrypted_message = ""
        length = len(self.coding_symbols)
        for char in message:
            if char in self.coding_symbols:
                index = self.coding_symbols.index(char) - key
                if index < 0:
                    index += length
                decrypted_message += self.coding_symbols[index]
        return decrypted_message

    def encrypt(self, message: str, key: int) -> str:
        """шифрование с использованием шифра Цезаря.

        Args:
            message: Сообщение для шифрования.
            key: Ключ для шифрования.

        Returns:
            object: Зашифрованное сообщение.
        """
        encrypted_message = ""
        for char in message:
            if char in self.coding_symbols:
                index = ((self.coding_symbols.index(char) + key)
                         % len(self.coding_symbols))
                encrypted_message += (
                    self.coding_symbols)[index]
            else:
                encrypted_message += char
        return encrypted_message

    @staticmethod
    def validate_decrypted_message(message):
        d = enchant.Dict("en_US")
        count = 0
        words = message.split()
        for word in words:
            if not d.check(word):
                pass
            else:
                count = count + 1
        if count > 1:
            return True



if __name__ == '__main__':
    encrypted_password = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    decrypted_password = "The vacation was a success"
    cipher = CaesarsCipher()
    for key in range(len(cipher.coding_symbols)):
        decrypted_message = cipher.decrypt(encrypted_password, key)
        if ' ' in decrypted_message and decrypted_message.isascii():
            if cipher.validate_decrypted_message(decrypted_message) is True:
                print(f'{key}: {decrypted_message}')
    print('Доп проверка:')
    key = 3
    decrypted_message = cipher.encrypt(decrypted_password, key)
    print(f'{key}: {decrypted_message}')
    encrypted_password = cipher.decrypt(decrypted_message, key)
    print(f'{key}: {encrypted_password}')
