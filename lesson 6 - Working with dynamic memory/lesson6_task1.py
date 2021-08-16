"""
TASK:
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили
творчество, фантазию и создали универсальный код для замера памяти.


EXAMPLE:
Написать программу сложения двух шестнадцатеричных чисел.
"""
import sys
from collections import deque


def sum1():
    array16 = deque('0123456789ABCDEF')

    left = deque([array16.index(i) for i in 'A2'])
    right = deque([array16.index(i) for i in 'C4F'])

    while len(left) != len(right):
        left.appendleft(0) if len(left) < len(right) else right.appendleft(0)

    left.reverse()
    right.reverse()

    result = deque()
    rank = 0
    idx = 0
    while idx < len(left) or rank > 0:
        idx_result = left[idx] + right[idx] + rank
        rank = idx_result // 16
        idx_result %= 16

        result.append(array16[idx_result])
        idx += 1

    result.reverse()
    print(f'sum = {result}')

    return vars()


def sum2():
    hex_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   'A', 'B', 'C', 'D', 'E', 'F']

    bin_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    first = deque('A2')
    second = deque('C4F')

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0
    for i in range(len(first) - 1, -1, -1):
        first_num = bin_numbers[first[i]]
        second_num = bin_numbers[second[i]]

        result_num = first_num + second_num + overflow

        if result_num >= 16:
            overflow = 1
            result_num -= 16
        else:
            overflow = 0

        result.appendleft(hex_numbers[result_num])

    if overflow == 1:
        result.appendleft('1')

    print(f'sum = {result}')

    return vars()


def sum3():
    array16 = [i for i in '0123456789ABCDEF']

    left = [array16.index(i) for i in 'A2']
    right = [array16.index(i) for i in 'C4F']

    left.reverse()
    right.reverse()

    while len(left) != len(right):
        left.append(0) if len(left) < len(right) else right.append(0)

    result = []
    rank = 0
    idx = 0
    while idx < len(left) or rank > 0:
        idx_result = left[idx] + right[idx] + rank
        rank = idx_result // 16
        idx_result %= 16

        result.append(array16[idx_result])
        idx += 1

    result.reverse()
    print(f'sum = {result}')

    return vars()


def calc_memory(f):
    f = f()
    total_memory = 0
    for i, v in f.items():
        memory = sys.getsizeof(v)
        total_memory += memory
        print(f'\t{i}\t({memory} bytes)\t= {v}')

    print(f'TOTAL MEMORY = {total_memory} bytes\n')

    return total_memory


calc_memory(sum1)
"""
left        (624 bytes)	= deque([2, 10, 0])
right       (624 bytes)	= deque([15, 4, 12])
result      (624 bytes)	= deque(['C', 'F', '1'])
rank        (24 bytes)	= 0
idx         (28 bytes)	= 3
idx_result  (28 bytes)	= 12
array16     (624 bytes)	= deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])

TOTAL MEMORY = 2576 bytes
"""

calc_memory(sum2)
"""
hex_numbers (184 bytes)	= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
bin_numbers (640 bytes)	= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
first       (624 bytes)	= deque(['C', '4', 'F'])
second      (624 bytes)	= deque(['0', 'A', '2'])
result      (624 bytes)	= deque(['C', 'F', '1'])
overflow    (24 bytes)  = 0
i           (24 bytes)	= 0
first_num   (28 bytes)	= 12
second_num  (24 bytes)	= 0
result_num  (28 bytes)	= 12

TOTAL MEMORY = 2824 bytes
"""

calc_memory(sum3)
"""
left        (88 bytes)  = [2, 10, 0]
right       (88 bytes)	= [15, 4, 12]
result      (88 bytes)	= ['C', 'F', '1']
rank        (24 bytes)	= 0
idx         (28 bytes)	= 3
idx_result  (28 bytes)	= 12
array16     (184 bytes)	= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

TOTAL MEMORY = 528 bytes

Самый дешевый по памяти вариант - 3й, всего 528 байт, что в 5 раз меньше чем два предыдущих варианта.
Затраты по памяти удалось уменьшить за счет:
1. Использование list вместо deque.
2. Применение одних и тех же переменных вместо создания новых.
3. Перезаписывание переменных вместо создания новых.

SYSTEM:
sys.version     = 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)]
sys.platform    = win32
"""
