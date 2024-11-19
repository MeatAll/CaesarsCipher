alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

#char_ja = alphabet[32]
#char_i = alphabet[9]
#char_z = alphabet[8]
#char_y = alphabet[20]
#char_ch = alphabet[24]

# Вариант с промежуточной переменной
# phrase =  (f"{alphabet[32]} {alphabet[9]}{alphabet[8]}{alphabet[20]}{alphabet[24]}{alphabet[0]}{alphabet[31]}"
#              f" {alphabet[16]}{alphabet[9]}{alphabet[19]}{alphabet[15]}{alphabet[14]}"
#              )
# print(phrase.capitalize())

# Вариант без промежуточной переменной
print(f"{alphabet[32].upper()} {alphabet[9]}{alphabet[8]}{alphabet[20]}{alphabet[24]}{alphabet[0]}{alphabet[31]}"
             f" {alphabet[16]}{alphabet[9]}{alphabet[19]}{alphabet[15]}{alphabet[14]}"
      )