"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
# Preprocess
import random

A = [random.randint(0, 100) for _ in range(10)]
print(A)

min_a = A[0]
max_a = A[0]
for i in A:
    if i < min_a:
        min_a = i
    if i > max_a:
        max_a = i

# General
min_idx, max_idx = 0, 0
for i in range(len(A)):
    if A[i] == max_a:
        max_idx = i
    if A[i] == min_a:
        min_idx = i

if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx

result = 0
for i in A[min_idx + 1: max_idx]:
    result += i
print(f'Сумма чисел между {min_a} и {max_a} = {result}')
