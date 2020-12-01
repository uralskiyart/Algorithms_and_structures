# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def nums_cnt_1(n):  # Вариант через while условие:
    even_cnt = 0
    odd_cnt = 0
    while n != 0:
        next_num = n % 10
        n //= 10
        if next_num % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    return f'Вариант_1 : {even_cnt} - четных | {odd_cnt} - нечетных'


def nums_cnt_2(n):
    even_cnt = 0
    odd_cnt = 0
    for i in str(n):
        if int(i) % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    return f'Вариант_2 : {even_cnt} - четных | {odd_cnt} - нечетных'

num = int(input('Введите целое число: '))

a = nums_cnt_1(num)
b = nums_cnt_2(num)

print(a)
print(b)
