list_int = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def get_iter(iterator):
    x = lambda i: [-i for i in iterator]
    return x(iterator)


print(get_iter(iter(list_int)))
