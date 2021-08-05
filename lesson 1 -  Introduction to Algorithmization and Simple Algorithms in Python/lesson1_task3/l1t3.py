"""
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

a = input("Введите а: ")
b = input("Введите b: ")

data_type = None
chars = 'abcdefghijklmnopqrstuvwxyz'
if a in chars:
    a, b = map(ord, (a, b))
    data_type = 'char'
else:
    a, b = map(float, (a, b))
    data_type = 'int' if (a % 1 == 0 and b % 1 == 0) else 'float'

result = a + (b - a) * random.random()
if data_type == 'float':
    result = round(result, 2)
else:
    result = round(result)
    if data_type == 'char':
        result = chr(result)

print(result)
