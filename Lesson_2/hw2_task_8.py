# Посчитать, сколько раз встречается определенная цифра в введенной последовательности
# чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются
# вводом с клавиатуры.

def num_searcher(amount_times, n_to_find, n_counter=0):
    next_num = input('Введите целое число: ')
    for i in next_num:
        if i == n_to_find:
            n_counter += 1
    if amount_times == 1:
        return n_counter
    else:
        return num_searcher((amount_times - 1), n_to_find, (n_counter))


amount = int(input('введите количество вводов: '))
n = input('введите число которыое будем искать: ')

print(num_searcher(amount, n))
