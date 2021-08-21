"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

array = [random.randint(0, 100) for _ in range(random.randint(2, 7) * 2 + 1)]
print('array =', array)


def median(arr):
    for i in arr:
        less, more = [], []
        for j in arr:
            more.append(j) if j > i else less.append(j)
        if len(less) == len(more) + 1:
            return max(less)
        elif len(less) + 1 == len(more):
            return min(more)


print('median =', median(array))
