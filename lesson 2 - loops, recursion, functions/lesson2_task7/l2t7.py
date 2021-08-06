"""
7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""

n = int(input("Введите число"))

right = int(n * (n + 1) / 2)
left = 0
for i in range(1, n + 1):
    left += i


def write_eq(eq):
    for j in range(1, n + 1):
        print(f'{j} + ' if j < n else f'{j} = {eq}', end='')


write_eq(left)

r = 'n(n + 1) / 2'
print(f'\n{r} = {right}')
print(f'{left} = {right}')

write_eq(r)
