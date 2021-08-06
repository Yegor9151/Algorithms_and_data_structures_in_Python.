"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

count = int(input('Сколько чисел вы хотите ввести?'))
to_find = input('Какое число нужно искать?')

all_nums = 0
for i in range(count):
    num = input('Введите число')
    result = 0
    for j in num:
        if to_find in j:
            result += 1
    print(f'В числе {num} найдено {result} числа {to_find}')
    all_nums += result
    
print(f'Всего найдено {all_nums} чисел {to_find}')
