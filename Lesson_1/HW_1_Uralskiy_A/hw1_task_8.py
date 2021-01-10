# Определить, является ли год, который ввел пользователь, високосным или не високосным.
import datetime

year = int(input('ведите год: '))

if datetime.date(year, 12, 31) - datetime.date(year, 1, 1) == datetime.timedelta(365):
    print('Год високосный')
else:
    print('Год не високосный')
