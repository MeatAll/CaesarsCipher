
def get_phase_input():
    longphrase = ''
    print('Введите фразу')
    phrase = str(input())
    while phrase != 'end':
        if phrase != 'end':
            longphrase = longphrase + '\n' + phrase[::-1]
        print('Введите фразу')
        phrase = str(input())
    print(longphrase[1:-1])


get_phase_input()