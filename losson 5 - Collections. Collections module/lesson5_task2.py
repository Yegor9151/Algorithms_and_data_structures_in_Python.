"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.

Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в
несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.

Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""
from collections import deque

array16 = deque('0123456789ABCDEF')

action = input("Введите действие")
# action = 'A2 * C4F'

operator = '+' if '+' in action else '*'

left, right = action.split(operator)
left = deque([array16.index(i) for i in left if i != ' '])
right = deque([array16.index(i) for i in right if i != ' '])

if len(left) != len(right):
    left.appendleft(0) if len(left) < len(right) else right.appendleft(0)

left.reverse()
right.reverse()

result = deque()
rank = 0

if operator == '+':
    idx = 0
    while idx < len(left) or rank > 0:

        idx_result = left[idx] + right[idx] + rank
        rank = idx_result // 16
        idx_result %= 16

        result.append(array16[idx_result])

        idx += 1
else:
    for_sum = []
    for i, a in enumerate(left):
        nums = [0 for _ in range(i)]

        for j, b in enumerate(right):
            idx_result = a * b + rank
            rank = idx_result // 16
            idx_result %= 16

            nums.append(idx_result)

        if rank > 0:
            nums.append(rank)
            rank = 0

        for_sum.append(nums)

    max_len = max([len(i) for i in for_sum])

    idx = 0
    while idx < max_len or rank > 0:

        idx_result = rank
        for i in for_sum:
            idx_result += i[idx] if idx < len(i) else 0

        rank = idx_result // 16
        idx_result %= 16

        result.append(array16[idx_result])

        idx += 1

result.reverse()
print(result)
