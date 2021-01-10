# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр


def sum_next_num(n):
    if n // 10 == 0:
        return n % 10
    else:
        return n % 10 + sum_next_num(n // 10)


def average_numbers_sum():
    greatest_sum = 0
    greatest_num = 0
    while True:
        current_num = int(input('Введите целое число: '))
        if current_num == 0:
            break
        current_sum = sum_next_num(current_num)
        if current_sum > greatest_sum:
            greatest_sum = current_sum
            greatest_num = current_num
    print((f'Число - {greatest_num}, его сумма - {greatest_sum}'))


average_numbers_sum()
