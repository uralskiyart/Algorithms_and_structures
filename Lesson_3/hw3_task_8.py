# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
# в последнюю ячейку строки. В конце следует вывести полученную матрицу.


matrix = []
str_sum = 0

for i in range(0, 5):
    matrix_string = (input('Ведите 3 числа через пробел: ')).split()
    matrix.append([int(item) for item in matrix_string])
    for j in matrix[i]:
        str_sum += j
    matrix[i].append(str_sum)
    str_sum = 0

print(*matrix, sep='\n')
