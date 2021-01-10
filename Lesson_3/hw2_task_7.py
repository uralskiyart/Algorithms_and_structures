# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 8
MIN_ITEM = -5
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array[0] = -10
array.append(-9)
print(array)


# def two_min_nums_in_arr_1(arr):
#     most_min_id = 0
#     next_min_id = 1
#     for id, item in enumerate(arr):
#         if item < arr[most_min_id] and most_min_id != 0:
#             next_min_id = most_min_id
#             most_min_id = id
#         elif item < arr[next_min_id] and id != next_min_id - 1:
#             next_min_id = id
#     return most_min_id, next_min_id


def two_min_nums_in_arr_2(arr):
    most_min_id = 0
    next_min_id = 1
    i = 1
    while i < len(arr):
        if arr[i] < arr[most_min_id]:  # -1 проверка
            next_min_id = most_min_id
            most_min_id = i
        elif arr[i] < arr[next_min_id]:  # -1 проверка
            next_min_id = i
        i += 1  # + 1 действие
    return most_min_id, next_min_id


# a, b = two_min_nums_in_arr_1(array)
# print(f'Наименьшие числа {array[a]} и {array[b]} на позициях {a} и {b}')

a, b = two_min_nums_in_arr_2(array)
print(f'Наименьшие числа {array[a]} и {array[b]} на позициях {a} и {b}')
