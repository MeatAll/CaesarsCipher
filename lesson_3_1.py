var_string = input('Введите строку:\n\t')
var_char = input('Введите символ:\n\t')

def add_begin(v_string):
    return v_string.capitalize()

def replace_symbol(v_string, v_char):
    return v_string.replace(' ', v_char)

def update_string():
    temp_string = add_begin(var_string)
    print(replace_symbol(temp_string, var_char))

update_string()
