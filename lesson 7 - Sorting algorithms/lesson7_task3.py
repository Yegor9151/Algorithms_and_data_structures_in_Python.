"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

array = [random.randint(0, 100) for _ in range(random.randint(2, 7) * 2 + 1)]


def shaker_sort(arr):
    arr_len = len(arr)
    half = arr_len // 2

    for n in range(1, half + 1 if arr_len % 2 else half):
        for i in range(arr_len - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        for j in range(arr_len - 1 - n, n - 1, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        print(arr)


print('start >', array)
shaker_sort(array)
print('result >', array)

print(array[len(array) // 2])
