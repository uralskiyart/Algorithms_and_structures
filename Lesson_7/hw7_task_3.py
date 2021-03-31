'''3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался
на уроках (сортировка слиянием также недопустима).'''


import random


m = 100000
array = [random.randint(0, 1000) for i in range(2 * m + 1)]

def mid_point_finder_2(arr):

    max_num = min_num = arr[0]
    count_arr = []
    max_min_diff = 0

    for i in range(1, len(arr) - 1):
        if max_num < arr[i]:
            max_num = arr[i]
        if min_num > arr[i]:
            min_num = arr[i]

    for i in range (min_num, max_num + 1):
        if i in arr:
            count_arr.append([i, arr.count(i)])

    # если тут поменять действия в цикле на число * его_колво то получится сортировка
    # если знаете, подскажите название аггоритма?
    i = 0
    while count_arr[i] != count_arr[-1]:
        if count_arr[i][1] >= count_arr[-1][1]:
            count_arr[i][1] = count_arr[i][1] - count_arr[-i - 1][1]
            count_arr.pop()


        else:
            count_arr[-1][1] = count_arr[-1][1] - count_arr[i][1]
            count_arr[i][1] = 0

        if count_arr[i][1] == 0:
            i += 1


    return f'Медиана = {count_arr[-1][0]}'

print(mid_point_finder_2(array))
