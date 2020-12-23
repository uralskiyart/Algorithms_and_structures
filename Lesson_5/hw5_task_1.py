# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter, deque


def count_avg_profit_of_firms():
    quanity = int(input('Введите кол-во фирм: '))
    firms = create_firms(quanity)
    avg_for_all = 0

    for value in firms.values():
        avg_for_all += value

    avg_for_all /= quanity
    print(f'Среднее по всем фирмам = {avg_for_all}')

    less_avg = deque()
    more_avg = deque()

    for key, value in firms.items():
        less_avg.append((key, value)) if value <= avg_for_all else more_avg.append((key, value))

    print_avg_firms(less_avg, more_avg)

    pass


def create_firms(quanity):
    firms = Counter()
    for i in range(1, quanity + 1):
        firm_inp = input(f'Введите название фирмы {i}: ')
        quarters = []
        for j in range(1, 5):
            quarters_prof = input(f'Введите прибыль за квартал {j}: ')
            quarters.append(int(quarters_prof))

        firms[firm_inp] = sum(quarters) / 4

    return firms


def print_avg_firms(less_avg, more_avg):
    print('-' * 15, 'Вывод', '-' * 15)
    print(f'Предриятия чья выручка меньше или равна среднему: ')
    for i in less_avg:
        print(f'Название: {i[0]}  -  выручка: {i[1]}')
    print(f'Предриятия чья выручка больше среднего: ')
    for i in more_avg:
        print(f'Название: {i[0]}  -  выручка: {i[1]}')


count_avg_profit_of_firms()
