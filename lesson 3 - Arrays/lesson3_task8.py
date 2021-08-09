"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
import random

matrix = []
for _ in range(4):
    row = []
    sum_row = 0
    for column in range(5):
        if column < 4:
            # num = random.randint(0, 10)
            num = int(input())
            sum_row += num
            row.append(num)
        else:
            row.append(sum_row)
    matrix.append(row)

for row in matrix:
    for column in row:
        print(f'{column:>4}', end='')
    print()
