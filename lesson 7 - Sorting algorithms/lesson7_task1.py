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


def bubble_sort(arr):
    arr_len = len(arr)
    for n in range(1, arr_len):
        print(arr)
        stop = True
        for i in range(arr_len - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                stop = False
        if stop:
            break


"""
При сортировке правой части, левая может оказаться частично отсортированной,
поэтому я решил сделать перекрестную сортировку, что бы за один прогон сортировать массив как справа, так и слева.
Эта функция похожа на шейкер только не гоняет числа по массиву взад вперед, а одновременно сводит их к центру.
"""


def bubble_cross_sort(arr):
    arr_len = len(arr)
    half = arr_len // 2
    for n in range(1, half + 1 if arr_len % 2 else half):
        for i in range(arr_len - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if arr[arr_len - 1 - i] > arr[arr_len - 2 - i]:
                arr[arr_len - 1 - i], arr[arr_len - 2 - i] = arr[arr_len - 2 - i], arr[arr_len - 1 - i]
        print(arr)


"""
для эксперимента попробовал 2 вариента, перекрестная сортировка оказалась быстрее
"""
print('start >', array)
bubble_sort(array)
print('result >', array)
print()
print('start >', array)
bubble_cross_sort(array)
print('result >', array)
