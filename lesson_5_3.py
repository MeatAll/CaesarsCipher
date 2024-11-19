import re


def set_data_to_tuple():
    temp_data = input('Введите температурные данные: \n')
    temp_tuple = tuple(map(to_float_and_round, (re.split(r'[,\s]\s*', temp_data))))
    target_tuple = (get_average_temp(temp_tuple).__str__(), get_unic_datas(temp_tuple).__str__())
    print('Среднее значение температуры: ' + target_tuple[0])
    print('Отчет о температуре: ' + target_tuple[1])

def to_float_and_round(x):
    y = float(x).__round__(2)
    z = '%.2f' % y
    return z

def get_average_temp(data):
    var_t = 0.00
    for t in data:
        var_t = var_t + float(t)
    average_temp = var_t / len(data)
    return average_temp.__round__(2).__str__()

def get_unic_datas(data : tuple):
    sorted_data = sorted(data)
    list_data = []
    str_data = ''
    for dat in sorted_data:
        if not (list_data.__contains__(dat)):
            list_data.append(dat)
            if str_data == '':
                str_data = dat
            else:
                str_data = str_data + ' ' + dat
    return str_data

set_data_to_tuple()