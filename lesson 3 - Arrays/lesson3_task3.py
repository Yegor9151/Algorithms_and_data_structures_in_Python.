"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

# Preprocess
import random

A = [random.randint(0, 100) for _ in range(10)]
print(A)

min_a = A[0]
max_a = A[0]
for i in A:
    if min_a > i:
        min_a = i
    if max_a < i:
        max_a = i
print(min_a, max_a)

# General
B = A[:]
for i in range(len(A)):
    if B[i] == min_a:
        A[i] = max_a
    if B[i] == max_a:
        A[i] = min_a
print(A)
