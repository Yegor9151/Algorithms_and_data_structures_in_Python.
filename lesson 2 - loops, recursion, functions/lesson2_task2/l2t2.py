"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = input("Введите любое натуральное число: ")
even_nums = ''
odd_nums = ''
even, odd = 0, 0

for i in num:
    if int(i) % 2 == 0:
        even += 1
        even_nums += i
    else:
        odd += 1
        odd_nums += i

print(f'четных чисел - {even} ({", ".join(even_nums)})\n'
      f'нечетных чисел - {odd} ({", ".join(odd_nums)})')
