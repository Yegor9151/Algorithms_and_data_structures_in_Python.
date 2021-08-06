"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

count = int(input('Сколько чисел вы хотите ввести?'))

num_last = None
sum_last = 0
for i in range(count):
    num_now = input('Введите число')
    sum_now = 0
    for n in num_now:
        sum_now += int(n)
    print(f'Сумма цифр числа {num_now} = {sum_now}')
    if sum_last < sum_now:
        sum_last = sum_now
        num_last = num_now

print(f'Число с наибольшей суммой цифр - {num_last} = {sum_last}')
