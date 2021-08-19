"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random

array = [random.randint(-100, 99) for _ in range(random.randint(5, 15))]


def bubble_rock_sort(arr):
    arr_len = len(arr)
    half = arr_len // 2
    for n in range(1, half + 1 if arr_len % 2 else half):
        for i in range(arr_len - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if arr[arr_len - 1 - i] < arr[arr_len - 2 - i]:
                arr[arr_len - 1 - i], arr[arr_len - 2 - i] = arr[arr_len - 2 - i], arr[arr_len - 1 - i]
        print(arr)


print('start >', array)
bubble_rock_sort(array)
print('result >', array)
