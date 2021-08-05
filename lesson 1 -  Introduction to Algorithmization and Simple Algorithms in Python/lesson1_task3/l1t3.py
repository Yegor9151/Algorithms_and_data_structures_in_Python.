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

chars = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

data_type = None
if a in chars:
    data_type = 'char'
    a, b = a.lower(), b.lower()
    a = chars.index(a)
    b = chars.index(b)
else:
    a, b = map(float, (a, b))
    data_type = 'int' if (a % 1 == 0 and b % 1 == 0) else 'float'

result = a + (b - a) * random.random()
if data_type == 'float':
    result = round(result, 2)
else:
    result = round(result)
    if data_type == 'char':
        result = chars[result]

print(result)
