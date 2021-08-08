"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

matrix = [[random.randint(0, 100) for _ in range(5)] for _ in range(5)]
for row in matrix:
    for column in row:
        print(f'{column:>4}', end='')
    print()

min_column = []
for column in range(len(matrix[0])):
    row_from_column = [row[column] for row in matrix]
    min_num = row_from_column[0]
    for num in row_from_column:
        if min_num > num:
            min_num = num
    min_column.append(min_num)
print(f'Список минимальных значений из каждого столбца: {min_column}')

result = min_column[0]
for num in min_column:
    if result < num:
        result = num
print(f'Максимальное значение из минимальных значений в кадом столбце = {result}')
