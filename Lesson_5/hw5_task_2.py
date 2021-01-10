# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

HEX_NUMBERS = '0123456789ABCDEF'

DEC_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}


BASE = 16

def sum_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0

    while len(first) != 0:
        first_num = DEC_NUMBERS[first.pop()]
        second_num = DEC_NUMBERS[second.pop()]

        result_num = first_num + second_num + overflow

        if result_num >= BASE:
            overflow = 1
            result_num -= BASE
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_num])

    if overflow == 1:  # is_overflow = True or False
        result.appendleft('1')

    return result


def mult_hex(first, second):

    if len(second) > len(first):
        first, second = second, first

    overflow = 0
    spam = deque()
    result = deque('0' * len(first))

    for i in range(1, len(second) +1):
        second_num = DEC_NUMBERS[second[-i]]
        overflow = 0

        for j in range(1, len(first) + 1):
            first_num = DEC_NUMBERS[first[-j]]
            result_num = first_num * second_num + overflow

            if result_num >= BASE:
                overflow = result_num // 16
                result_num %= 16
            else:
                overflow = 0
            spam.appendleft(HEX_NUMBERS[result_num])

        if overflow > 0:
            spam.appendleft(HEX_NUMBERS[overflow])

        spam.extend('0' * (i - 1))
        result.extendleft('0' * (i-1))

        result = sum_hex(result, spam)
        spam.clear()

    return result

print(hex(int('fa2', 16) + int('ffA', 16)))
print(hex(int('A2', 16) * int('C4F', 16)))

a = deque(['A', '2'])
b = deque(['C', '4', 'F'])

print(sum_hex(a, b))
print(mult_hex(a, b))



