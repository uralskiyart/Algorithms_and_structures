# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимал

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def find_max_negative(arr):
    for idx, item in enumerate(arr):
        if item < 0:
           res_item = item
           res_idx = idx
           break
    else:
        return f'в массиве отсутсвуют отрицательные значения'
    i = 1
    while i < len(arr):
        if arr[i] < 0 and arr[i] > res_item:
            res_item = arr[i]
            res_idx = i
        i += 1
    return f'Число {res_item} на позиции {res_idx}'


print(find_max_negative(array))
