# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 3
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array.append(array[0])


def count_elements_dict(arr): # Составим словарь с подсчетом всех элементов
    d = {}
    for item in arr:
        if item not in d:
            d.setdefault(item, 1)
        else:
            d[item] += 1
    return d


def more_often_elements(arr): # составим массив со значениями самого частого числа или чисел (число, кол-во)
    d = count_elements_dict(arr)
    max_value = 0
    keys_arr = []
    for value in d.values():
        if value > max_value:
            max_value = value
    for key, value in d.items():
        if value == max_value:
            keys_arr.append(key)
    return keys_arr, max_value


def more_often_el_in_arr_output(arr):
    numbers_arr, value = more_often_elements(arr)
    print(f'В массиве {arr}')
    print(f'Самый частый элемент(ы) - ({", ".join(str(number) for number in numbers_arr)}) - '
          f' кол-во в массиве {value} раз(а)')
    pass

more_often_el_in_arr_output(array)
