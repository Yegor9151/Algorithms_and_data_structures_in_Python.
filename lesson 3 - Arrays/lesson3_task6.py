"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
# Preprocess
import random

A = [random.randint(0, 100) for _ in range(10)]
print(A)

min_i = 0
max_i = 0
for i in range(len(A)):
    if A[min_i] > A[i]:
        min_i = i
    if A[max_i] < A[i]:
        max_i = i

print(A[max_i], A[min_i])

# General
if min_i > max_i:
    min_idx, max_idx = max_i, min_i

result = 0
for i in A[min_i + 1: max_i]:
    result += i
print(f'Сумма чисел между {A[min_i]} и {A[max_i]} = {result}')
