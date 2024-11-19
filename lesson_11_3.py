def create_generator(start: int, end: int):
    list_keys = list(range(start, end+1))
    var_dict = {x: [i**list_keys.index(x) for i in list_keys] for x in list_keys}
    return var_dict

def create_generator_v2(start: int, end: int):
    list_keys = list(range(start, end+1))
    var_dict = {x: [i ** list_keys.index(x) for i in range(start, start+11)] for x in list_keys}
    return var_dict


print(create_generator(2,4))
print(create_generator_v2(2,4))
