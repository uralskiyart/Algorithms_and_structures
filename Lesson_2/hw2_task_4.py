# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


def sum_numbers_1(n, x=1):
    if n == 1:
        return x
    else:
        return x + sum_numbers_1(n - 1, x / -2)


def sum_numbers_2(n):
    now_num = 1
    sum_of_nums = 0
    while n > 0:
        sum_of_nums += now_num
        now_num /= -2
        n -= 1
    return sum_of_nums


num = int(input('Введите целое число: '))

a = sum_numbers_1(num)
b = sum_numbers_2(num)

print(f'рекурсией = {a} |||| циклом = {b}')
