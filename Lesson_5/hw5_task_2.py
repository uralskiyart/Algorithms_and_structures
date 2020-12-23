# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque, Counter


def hexadecimal_sum(a, b):
    numbers16 = '0123456789ABCDEF0123456789ABCDEF'
    c = deque()
    k = 0
    average = len(a) if len(a) >= len(b) else len(b)

    for i in range(1, average + 1):
        try:
            a_digit_idx = numbers16.index(a[-i]) # находим первое вхождение символа в массиве данных
            b_digit_idx = numbers16.index(b[-i])
            c.appendleft(numbers16[a_digit_idx + b_digit_idx + k])
            k = 1 if a_digit_idx + b_digit_idx + k > 15 else 0

            if k == 1 and average == i:
                c.appendleft(k)

        except IndexError:
            if len(a) > len(b):
                a_digit_idx = numbers16.index(a[-i])
                c.appendleft(numbers16[a_digit_idx + k])
                k = 1 if a_digit_idx + k > 15 else 0

            else:
                b_digit_idx = numbers16.index(b[-i])
                c.appendleft(numbers16[b_digit_idx + k])
                k = 1 if b_digit_idx + k > 15 else 0

            if k == 1 and average == i:
                c.appendleft(k)

    return list(c)


# def hexadecimal_mul(a, b):
#     numbers16 = '0123456789ABCDEF'
#     spam = deque()
#     dict_for_sum = {}
#     k = 0
#
#     for i in range(1, len(b) + 1):
#         for j in range(1, len(a) + 1):
#             a_digit_idx = numbers16.index(a[-j])
#             b_digit_idx = numbers16.index(b[-i])
#             spam.appendleft(numbers16[(a_digit_idx * b_digit_idx + k) % 16])
#             k = (a_digit_idx * b_digit_idx) // 16 if a_digit_idx * b_digit_idx + k > 15 else 0
#
#         if k > 0:
#             spam.appendleft(numbers16[k])
#
#         dict_for_sum[i] = deque(spam)
#         print(dict_for_sum)
#         spam.clear()
#         k = 0
#         print(len(dict_for_sum))
#
#         for i in range(1, len(dict_for_sum) + 1):
#             pass
#
#     return dict_for_sum




print(hex(int('fa2', 16) + int('ffA', 16)))
print(hex(int('A2', 16) * int('C4F', 16)))

a = ['A', '2']
b = ['C', '4', 'F']

print(hexadecimal_sum(a, b))


# a = ['0','9', '7', 'E']
# b = ['0', '8', '8', '0']
# c = hexadecimal_sum(a, b)
# a = ['7', '9', '8']
#
# print(c)
# print(hexadecimal_sum(c, a))

