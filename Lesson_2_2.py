matrix_Length = 17
border_Char = '*'
phrase = "Привет, мир!"
new_Line_Symbol = "\n"

print(f"{border_Char * matrix_Length}{new_Line_Symbol}"
      f"{border_Char}{phrase[0:(phrase.index(' '))].center(matrix_Length-2)}{border_Char}{new_Line_Symbol}"
      f"{border_Char}{phrase[(phrase.index(' ')):].center(matrix_Length-2)}{border_Char}{new_Line_Symbol}"
      f"{border_Char * matrix_Length}")