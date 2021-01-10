# Напишите программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.


def left_side_res(n):
    if n == 1:
        return n
    else:
        return n + left_side_res(n - 1)


def right_side_res(n):
    return n * (n + 1) / 2


def compare(x, y):
    if x < y:
        return 'right > left'
    if x > y:
        return 'left > right'
    else:
        return 'equal'


def prove_eqaual(n):
    state = compare(left_side_res(n), right_side_res(n))
    if state == 'equal':
        return 'Доказано, уравнения равны'
    else:
        return 'Не доказано, уравнения, не равны'


a = int(input('Введите целое число: '))

a = prove_eqaual(5)

print(a)
