# Определить, какое число в массиве встречается чаще всего.
import sys
from collections import Counter


array = [1, 6, 2, 2, 5, 1, 8, 4, 4, 2]
a = 77338384
array.append(a)


def size_sum(*args):
    mem_sum = 0
    var_values = [] # добавляем посчитанные значения

    for i in args:

        if isinstance(i, dict):
            mem_sum += sys.getsizeof(i)

            for key, value in i.items():

                if key not in var_values:
                    mem_sum += sys.getsizeof(key)
                    var_values.append(key)
                if value not in var_values:
                    mem_sum += sys.getsizeof(value)
                    var_values.append(value)

        if isinstance(i, list):
            mem_sum += sys.getsizeof(i)
            for j in i:
                if j not in var_values:
                    mem_sum += sys.getsizeof(j)
                    var_values.append(j)

        else:
            if i not in var_values and not isinstance(i, dict):
                mem_sum += sys.getsizeof(i)
                var_values.append(i)

    print(f'Задействованно памяти = {mem_sum}')



def more_often_elements_1(arr): # составим массив со значениями самого частого числа или чисел (число, кол-во)
    d = {}
    for item in arr:
        if item not in d:
            d.setdefault(item, 1)
        else:
            d[item] += 1


    max_value = 0
    keys_arr = []
    for value in d.values():
        if value > max_value:
            max_value = value
    for key, value in d.items():
        if value == max_value:
            keys_arr.append(key)
    result = f'Самое частые числа: {keys_arr[0]}, встречаются {max_value} раза'
    size_sum(arr, d, max_value,keys_arr)
    return result


def more_often_elements_2(arr):
    max_value = 0
    max_element = 0
    for i in arr:
        i_count = arr.count(i)
        if i_count > max_value:
            max_element = i
            max_value = i_count

    result = f'Самое частые числа: {max_element}, встречаются {max_value} раза'
    size_sum(max_value, max_element, i_count, arr)
    return result


def more_often_elements_3(arr):
    res_d = Counter(arr)
    result = f'Самое частые числа: {res_d.most_common(1)[0][0]}, встречаются {res_d.most_common(1)[0][1]} раза'
    size_sum(arr, res_d, result)
    return result

print('1 Вариант')
print(more_often_elements_1(array)) #Задействованно памяти = 454

print('Вариант 2')
print(more_often_elements_2(array)) #Задействованно памяти = 214

print('Вариант 3')
print(more_often_elements_3(array)) #Задействованно памяти = 538

''' За краткость кода приходится платить! Вариант через Counter кушает больше всего памяти!
Чуть меньше кушает память вариант 1, который выполне через словарь и массив 
Меньше всего памяти кушает Вариант 2 через три переменные и 
метод count для списков написанный на  яп C
А почему я не смог сделать import sum_mem в файл hw6_var_1.py?
Прописав import он не находит файл sum_mem 
'''