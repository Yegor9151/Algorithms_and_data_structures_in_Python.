"""
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

abc = input('Введите три чиста (a, b, c): ')
abc = abc.split(',')
a, b, c = map(int, abc)

medium = None
if (a < b < c) or (a > b > c):
    medium = b
elif (c < a < b) or (c > a > b):
    medium = a
elif (b < c < a) or (b > c > a):
    medium = c
else:
    medium = 'нет'

print(f'Среднее число - {medium}')
