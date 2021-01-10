# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести
# на экран. Например, если введено число 3486, надо вывести 6843.


def num_reverse(n):
    if n // 10 == 0:
        return f'{n % 10}'
    else:
        return f'{n % 10}{num_reverse(n // 10)}'

a = int(input('Введите целое число: '))

print(num_reverse(a))