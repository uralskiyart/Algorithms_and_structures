'''2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
 отсортированный массивы.'''

import random

array = [random.randint(0, 1000) for i in range(1000)]


def merge_sort(arr):

    if len(arr) == 1:
        return arr

    pivot = len(arr) // 2
    left = merge_sort(arr[:pivot])
    right = merge_sort(arr[pivot:])
    arr = []
    i = j = 0

    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    if len(left) > i:
        arr += left[i:]
    if len(right) > j:
        arr += right[j:]

    return arr


print(merge_sort(array))
