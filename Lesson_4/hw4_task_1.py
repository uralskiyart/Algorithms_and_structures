# Найти сумму четных чисел ряда фибоначи.

import cProfile
import timeit


def fib_even_sum_1(limit):  # limit кол во чисел фибоначи
    arr = [1, 2]
    while len(arr) < limit:
        arr.append(arr[-2] + arr[-1])
    evens = filter(lambda x: x % 2 == 0, arr)

    return (sum(evens))


def fib_even_sum_2(limit):
    arr = [1, 2]
    for i in range(2, limit):
        arr.append(arr[-2] + arr[-1])
    even_sum = 0
    for i in arr:
        if i % 2 == 0:
            even_sum += i
        for j in arr:
            pass
    return even_sum


def fib_even_sum_3(limit):
    first = 1
    second = 2
    evens_sum = 2

    for i in range(2, limit - 2):
        first, second = second, first + second
        if second % 2 == 0:
            evens_sum += second

    return evens_sum


# https://docs.google.com/spreadsheets/d/11ZKz578WErxtYEQXovRRwfVUTnxkdZU_5xNtZb0ob64/edit?usp=sharing
print(' 1-ый вариант ***' * 5)
print(timeit.timeit('fib_even_sum_1(10)', number=100, globals=globals()))  # 0.00033089999999999856
print(timeit.timeit('fib_even_sum_1(20)', number=100, globals=globals()))  # 0.0006917999999999994
print(timeit.timeit('fib_even_sum_1(40)', number=100, globals=globals()))  # 0.0014930000000000013
print(timeit.timeit('fib_even_sum_1(80)', number=100, globals=globals()))  # 0.003218000000000002
print(timeit.timeit('fib_even_sum_1(160)', number=100, globals=globals()))  # 0.007083299999999997
print(timeit.timeit('fib_even_sum_1(320)', number=100, globals=globals()))  # 0.016790099999999995
print(timeit.timeit('fib_even_sum_1(640)', number=100, globals=globals()))  # 0.0407817
print(timeit.timeit('fib_even_sum_1(1080)', number=100, globals=globals()))  # 0.0845247
print(timeit.timeit('fib_even_sum_1(2160)', number=100, globals=globals()))  # 0.26397570000000004
print('----' * 10)

print(' 2-ой вариант ***' * 5)
print(timeit.timeit('fib_even_sum_2(10)', number=100, globals=globals()))  # 0.0003402999999999601
print(timeit.timeit('fib_even_sum_2(20)', number=100, globals=globals()))  # 0.0008793000000000273
print(timeit.timeit('fib_even_sum_2(40)', number=100, globals=globals()))  # 0.0024947000000000163
print(timeit.timeit('fib_even_sum_2(80)', number=100, globals=globals()))  # 0.007697000000000009
print(timeit.timeit('fib_even_sum_2(160)', number=100, globals=globals()))  # 0.025768199999999963
print(timeit.timeit('fib_even_sum_2(320)', number=100, globals=globals()))  # 0.09268230000000005
print(timeit.timeit('fib_even_sum_2(640)', number=100, globals=globals()))  # 0.40382320000000005
print(timeit.timeit('fib_even_sum_2(1080)', number=100, globals=globals()))  # 1.0731967999999998
print(timeit.timeit('fib_even_sum_2(2160)', number=100, globals=globals()))  # 4.7641649
print('----' * 10)

print(' 3-ий вариант ***' * 5)
print(timeit.timeit('fib_even_sum_3(10)', number=100, globals=globals()))  # 8.9099999999398e-05
print(timeit.timeit('fib_even_sum_3(20)', number=100, globals=globals()))  # 0.00019649999999948875
print(timeit.timeit('fib_even_sum_3(40)', number=100, globals=globals()))  # 0.0005372999999995187
print(timeit.timeit('fib_even_sum_3(80)', number=100, globals=globals()))  # 0.001334199999999619
print(timeit.timeit('fib_even_sum_3(160)', number=100, globals=globals()))  # 0.003249900000000139
print(timeit.timeit('fib_even_sum_3(320)', number=100, globals=globals()))  # 0.008650399999999614
print(timeit.timeit('fib_even_sum_3(640)', number=100, globals=globals()))  # 0.025254100000000612
print(timeit.timeit('fib_even_sum_3(1080)', number=100, globals=globals()))  # 0.059957100000000096
print(timeit.timeit('fib_even_sum_3(2160)', number=100, globals=globals()))  # 0.20543639999999996
print('----' * 10)




cProfile.run('fib_even_sum_1(1000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#   1000    0.000    0.000    0.000    0.000 hw4_task_1.py:11(<lambda>)
#      1    0.001    0.001    0.001    0.001 hw4_task_1.py:7(fib_even_sum_1)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#    999    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.sum}
#    998    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('fib_even_sum_1(2000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      2000    0.001    0.000    0.001    0.000 hw4_task_1.py:11(<lambda>)
#         1    0.001    0.001    0.003    0.003 hw4_task_1.py:7(fib_even_sum_1)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1999    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.sum}
#      1998    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('fib_even_sum_1(4000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#     4000    0.004    0.000    0.004    0.000 hw4_task_1.py:11(<lambda>)
#        1    0.003    0.003    0.009    0.009 hw4_task_1.py:7(fib_even_sum_1)
#        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#     3999    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.001    0.001    0.005    0.005 {built-in method builtins.sum}
#     3998    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('fib_even_sum_2(1000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#        1    0.009    0.009    0.009    0.009 hw4_task_1.py:16(fib_even_sum_2)
#        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#      998    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('fib_even_sum_2(2000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.035    0.035 <string>:1(<module>)
#         1    0.035    0.035    0.035    0.035 hw4_task_1.py:16(fib_even_sum_2)
#         1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
#      1998    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('fib_even_sum_2(4000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.148    0.148 <string>:1(<module>)
#        1    0.147    0.147    0.148    0.148 hw4_task_1.py:16(fib_even_sum_2)
#        1    0.000    0.000    0.148    0.148 {built-in method builtins.exec}
#     3998    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('fib_even_sum_3(1000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 hw4_task_1.py:29(fib_even_sum_3)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('fib_even_sum_3(2000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#        1    0.002    0.002    0.002    0.002 hw4_task_1.py:29(fib_even_sum_3)
#        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('fib_even_sum_3(4000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#      1    0.006    0.006    0.006    0.006 hw4_task_1.py:29(fib_even_sum_3)
#      1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
Вывод
1ый Вариант: квадратичная сложность O(2n)
2ой Вариант: кубическа сложность O(2n)
3ий Вариант:квадратичная сложность O(2n)


'''