"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []
for _ in range(4):
    row = []
    for column in range(5):
        if column < 4:
            row.append(int(input()))
        else:
            sum_row = 0
            for i in row:
                sum_row += i
            row.append(sum_row)
    matrix.append(row)

for row in matrix:
    for column in row:
        print(f'{column:>4}', end='')
    print()
