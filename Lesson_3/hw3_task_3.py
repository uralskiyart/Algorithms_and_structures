# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def return_max_and_min_id(arr): # вернуть кортеж id (max, min)
    min_id = 0
    max_id = 0
    for id, item in enumerate(arr):
       if item > arr[max_id]:
           max_id = id
       if item < arr[min_id]:
           min_id = id
    return (max_id, min_id)


def replace_max_and_min(arr):
    max_id, min_id = return_max_and_min_id(arr)
    arr[max_id], arr[min_id] = arr[min_id], arr[max_id]
    return arr



print(f'max_id, min_id = {return_max_and_min_id(array)}')
print('---' * 20)
print(replace_max_and_min(array))
