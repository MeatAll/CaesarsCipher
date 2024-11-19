n = int(input())


def get_even(num):
    while num <= 2:
       num = get_num(num)
       print(num)

def get_num(num_temp : int):
    return int(num_temp/2)

get_even(n)