# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
# элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 8
MIN_ITEM = -10
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def return_min_and_max_id(arr): # вернуть кортеж id (max, min)
    min_id = 0
    max_id = 0
    for id, item in enumerate(arr):
       if item > arr[max_id]:
           max_id = id
       if item < arr[min_id]:
           min_id = id
    return (min_id, max_id)


def sum_beetween_min_max(arr):
    min_id, max_id = return_min_and_max_id(arr)
    res = 0
    if min_id < max_id:
        for i in range(min_id + 1, max_id):
            res += array[i]
    else:
        for i in range(max_id + 1, min_id):
            res += array[i]
    return f'min = {array[min_id]} max = {array[max_id]} сумма чисел между ними = {res}'


print(sum_beetween_min_max(array))
