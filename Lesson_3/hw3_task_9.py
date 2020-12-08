# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [
[2, 2, 1, 5],
[1, 4, 5, 11],
[3, 5, 6, 6],
[2, 5, 7, 14],
[2, 3, 6, 10]
]

max_item = matrix[0][0]

for i in range(0, len(matrix) - 1):
    min_item_col = matrix[0][i]
    for j in range(1, len(matrix) - 1):
        if matrix[j][i] < min_item_col:
            min_item_col = matrix[j][i]
    if min_item_col > max_item:
        max_item = min_item_col

print(f'Максимальный элемент среди минимальных элементов столбцов: {max_item}')
